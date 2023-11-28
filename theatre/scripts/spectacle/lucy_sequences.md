
## Scene 5

### Préparation

Changer la langue de QT en Anglais.

```bash
ssh qtrobot@192.168.100.1
qtrobot
rosservice call /qt_robot/speech/config "language: 'en_US'"
```

### Séquence

```
Je commence.

Attendre que Nao s'arrête

[&][1] Hi NAO, how are you ?

[c] Look at Nao
[q] Look at the audience

[é][2] Do you know what I can do ?

[c] Look at Nao

Attendre que Nao s'arrête

[q] Look at the audience

["][3] How about you ?

[c] Look at Nao

While Nao speaks :

- [p] SURPRISE 
- [o] YAWN 

[q] Look at the audience

['][4] Do you have sensors ?

[=] NEUTRAL to get hands down

[c] Look at Nao

While Nao speaks :

- [o] YAWN

[q] Look at the audience

[(][5] How many computers do you have ?

[c] Look at Nao

While Nao speaks :

[b] RASPBERRY

[q] Look at the audience

[-][6] Let's go !
```

## Scene 6

### Préparation

```
[h] happy
[p] surprise
[f] afraid
[j] shy
[y] angry
[b] raspberry
```

### Sequence

```
ANDREA : Sai che lavvoreremo assieme ?
[1] of course 
ANDREA : Mi chiamo Andrea.
[2] nice to 
SARAH : Si puoi sentire, QT ?
[3] yes
SARAH : Sono Sarah.
[2] nice to
JEREMY : E puoi parlare piu lingue ?
[4] maybe
SARAH : E mettere della musica ?
[5] no
JEREMY : Prima parlavi... meglio!
PREDRAG : Prima parlava grazie a Chat GPT.
JEREMY : Puoi camminare ?
[5] no
SARAH : E devi essere sempre collegato per funzionare ?
[3] yes
ANDREA : Io non ho mai lavorato con dei robot
[5] no
SARAH : Faremo del teatro assieme!
[6] great
JEREMY : Credi che Nao reciti meglio di te ?
[7] no no no
ANDREA : Si chiama QT!
[3] yes
```

## Scene 10 Masque blanc

### Préparation

Changer les états dans `qt_play.py`.

### Sequence

```
bras
N

pied
N

ventre
O

bras en haut
O ensemble

coucou raté
i

coucou
i ensemble

bouge
N

bouge
N

sort
P
```

Quand le masque sort dialogue immediatement [&].

```
[&] where are you going
[r]
[é] i'm having some communication problems

Nao entre

QT regarde Nao

["] Nao, Nao, come here!



```

## Scene 11 Claire Heggen

## Scene 12 Short dialogue

apres so big compared to us [n] neutral

## Scene 14 Audition

### Préparation

Commenter ROS IP
Verifier l'IP de Nao.
Verifier mon IP.
`ifconfig`
`rosrun naoqi_driver naoqi_driver_node --qi-url=tcp://192.168.1.100:9559 --roscore_ip=192.168.1.103 --network_interface wlp2s0`

## Scene 18 Autonomie

## Préparation

ROS IP
close other terminals
WIFI
camera
qt_play

## Scene 20 L'adoption

## Scene 21 Photos famille

TODO : fusionner avec scene 20

---




---------------

Préparation
- Naoqi
- QT ssh
- qt_behave
- qt_play
- nao_behave
- nao_play
- Choreographe

QT
- QT ssh
- QT behave
- QT play

- Scene 1 Ampoules
- Scene 2 Ampoules
- Scene 3 Scene sans robots
- Scene 4 Ampoules
    Charger scene 5 QT
    Konstantinos pose QT sur le cube moyen.
    Nao marche sur scene et s'arrete à moitié

- SCENE 5 ChatGPT -> QT (Predrag) + Nao (Anis)
    Premiere replique de QT
    Nao continue de marcher
    Dialogue entre les deux robots commence
- SCENE 6 La premiere rencontre -> QT (Predrag) + Nao (Anis)
    Charger SCENE 6 QT
    Andrea entre en scene et tourne autour de QT
    Predrag parle pendant cette scene
    Philippo parle
    Preparer la SCENE 10
- SCENE 7 Ampoules
    QT posé par terre
    Nao posé sur le pupitre
- SCENE 8 Nao un simple telephone -> Nao (éteint)
- SCENE 9 Ampoules
    Léandre entre en scene
    Predrag allume l'UV
- SCENE 10 QT et son ami blanc -> QT (Predrag) + Nao (Anis)
    QT + Léandre
    Léandre quitte la scene
    Predrag éteint UV
    QT parle
    Nao entre en scene
    QT parle
    QT voit Nao
- SCENE 10bis QT et NAO sur les acteurs -> QT (Predrag) + Nao (Anis)
    Dialogue QT + Nao
    Nao rejoins sa position en diagonale cour
- SCENE 11 Claire Heggen
    En fin de scene, Nao tourne la tete et le corps en direction des écrans
    QT lance la vidéo
- Video de Saeed
- Scene 12 Les acteurs ces êtres compliques -> QT + Nao
    Court dialogue
- Scene 13 Ampoules -> Nao
    Nao illustre les mouvements pendant que AMPOULE G parle
    QT est éteint quand l'AMPOULE S parle
    Predrag prend contrôle de Nao
        1. Connexion routeur
        2. .bashrc
        3. Choreographe
        4. Naoqi : rosrun naoqi_driver naoqi_driver_node --qi-url=tcp://192.168.1.111:9559 --roscore_ip=192.168.1.107 --network_interface wlp2s0
        5. nao_behave
        6. nao_play
    Changer sur QT
    Charger scene 18 
- Scene 14 L'audition -> Nao
    Fin de scene
    Scene acteurs
    Predrag parle
    Predrag allume la lumiere
    Predrag répond
    Anis reprend contrôle de Nao
    Eteindre la lumiere
- Scene 15 Ampoules
- Scene 16 Amour, dance -> Nao (Anis)
- Scene 17 Ampoules
* Scene 18 QT metteur en scene -> QT (Predrag, autonome)
- Scene 19 Ampoules
* Scene 20 Adoption -> QT (Predrag)
    Changer de script pendant la pluie
- Scene 21 Les photos de famille -> Tout le monde
  Photo 1 QT
  Photo 2 QT
  Photo 3 QT
  Photo 4 QT + Nao
  Photo 5 QT + Nao
  Photo 6 QT + Nao
  Photo 7 QT + Nao
  Photo 8 QT + Nao
  Photo 9 QT + Nao + Predrag
  Photo 10 Anis entre, Tout le monde
  
