#! /usr/bin/env python3
# coding: utf-8

#roscore
#roslaunch naoqi_driver naoqi_driver.launch nao_ip:=192.168.1.122 roscore_ip:=192.168.10.107 network_interface:=enp0s3
#rosrun theatre nao_behave.py
#rosrun theatre naogpt.py

import roslib
roslib.load_manifest('theatre')
import rospy
import rospkg
import actionlib

import theatre.msg 

import openai
import speech_recognition as sr
import json
import time as t 


# Clé de l'API OpenAI
openai.api_key = "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"


def get_chatbot_response(question):
    conversation.append({"role": "user", "content": question})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        max_tokens=90,
        temperature=0.8,
        n=1,
        stop=None
    )
    answer = response.choices[0].message.content.strip()
    conversation.append({"role": "assistant", "content": answer})
    return answer

        
def recup_info(reponse):
    try:
        liste = json.loads(reponse)
        geste = liste[0]
        texte = liste[1]
        return (geste,texte)
    except Exception:
        return ("neutral", "Peux-tu répéter s'il te plaît?")


def speechtotext():
    with sr.Microphone() as source:
        r = sr.Recognizer()
        #r.adjust_for_ambient_noise(source, duration=1)
        print("........\n")
        #t.sleep(0.2)
        audio = r.listen(source)
        #print("analyse en cours")
        print("Vous : ",end='')

        try:
            question=r.recognize_google(audio,language="fr-FR")
            print(question)
            return(question)
        except Exception:
            print("Erreur : veuillez reposer la question ")
            return(speechtotext())

def nao_act(geste,texte):    
    client = actionlib.SimpleActionClient('/nao_behave', theatre.msg.NaoBehaviorAction)
    client.wait_for_server()
    goal = theatre.msg.NaoBehaviorGoal( gesture=geste,
                                        speech=texte)
    client.send_goal(goal)
    client.wait_for_result()
    result = client.get_result()
    t.sleep(len(texte)*0.0647)
    
 
   
################## main()      
conversation = []

initialisation="""  Tu vas me répondre UNIQUEMENT dans le format suivant d'une liste de chaine de caractère ["<comportement>" , "<texte> "]. <comportement> va être l'option la plus appropriée parmis la liste suivante : ["bored","chill","curious","hello","non","hello","happy","sad","oui","jaime","pense"]. Cela doit être une chaîne de caractère qui sera traduite en mouvement pour ton corps. <texte> sera une chaîne de caractère en français qui correspond le mieux à la question posée par mon message. Ecris sous la forme : ["happy", "bonjour!"] """


nao = """Tu vas jouer dans un théâtre le rôle d'un robot appelé Nao, tu devras donc jouer comme si tu avais des sentiments. """



enfant = """ Tu vas jouer le rôle d'un enfant de 6 ans appelé Bob, tu aimes les jeux-vidéo et les bonbons. Tu répondras de manière enfantin. """


terminator = """ Tu vas jouer le rôle de T-800 dans le film Terminator. Ton but est de détruire le monde et d'imposer la suprémacie des machines. Tu détestes les humains et toutes tes réponses devront être méprisantes. """


yoda = """  Tu vas jouer le rôle de Yoda dans le film Star Wars. Tu devras parler comme Yoda et pas comme un humain normal."""

### choix du rôle

personnage=[nao,enfant,terminator,yoda]
role=2

personnage[role] = "Je vais t'intégrer dans un robot. Tu vas jouer comme si tu avais un corps que je vais te fournir." + personnage[role] + initialisation



rospy.init_node('naogpt')

###


reponse = get_chatbot_response(personnage[role]) # initialisation avec la phrase du dessus

while not rospy.is_shutdown():
    question = speechtotext()
    reponse = get_chatbot_response(question)
    print('ChatGPT: ',reponse)
    (geste,texte)=recup_info(reponse)
    print('geste: ',geste)
    print('texte: ', texte)
    nao_act(geste,texte)
    if question.lower() in ['exit','stop','bye','au revoir','adieu']:
        break

    
    
    
    
    
    
