global TCase
TCase = [[0,0,0],[0,0,0],[0,0,0]]
global tour
tour = 1
print "c'est votre tour"
def setup():
    size(640, 360)
def PlayerPlay(key):
    key = key-1
    Y = floor(key/3)
    X = key-Y*3
    if TCase[Y][X]==0:
        TCase[Y][X] = 1
        print TCase
        Victoire()
def keyPressed():
    if key=="1" or key=="2" or key=="3" or key=="4" or key=="5" or key=="6" or key=="7" or key=="8" or key=="9":
        print key
        PlayerPlay(int(key))
def draw():
    pass
def VictoryScreen(who):
    global TCase
    print TCase
    if who==1:
        print "player win"
    elif who==2:
        print "try again"
    else:
        print "match nulle"
    print "1 to replay"
    print "2 to stop"




#Véritable partie du code tout ce qui est avant et uniquement utile pour les tests
#intelligence artificielle
def IA():
    global TCase
    RobotAJouer = False
    #analyse des lignes horizontales
    for i in range(3):
        countO = 0
        countX = 0
        for j in range(3):
            if TCase[i][j]==1:
                countX += 1
            elif TCase[i][j]==2:
                countO += 1
        if countO==2 or countX==2:
            for j in range(3):
                if TCase[i][j]==0 and RobotAJouer==False:
                    RobotAJouer = True
                    TCase[i][j] = 2
    #analyse des lignes verticales
    for j in range(3):
        countO = 0
        countX = 0
        for i in range(3):
            if TCase[i][j]==1:
                countX += 1
            elif TCase[i][j]==2:
                countO += 1
        if countO==2 or countX==2:
            for i in range(3):
                if TCase[i][j]==0 and RobotAJouer==False:
                    RobotAJouer = True
                    TCase[i][j] = 2
    #Gestion des diagonales
    countLX = 0
    countLO = 0
    countRX = 0
    countRO = 0
    for a in range(3):
        if TCase[a][a]==1:
            countLX += 1
        elif TCase[a][a]==2:
            countLO += 1
        if TCase[a][2-a]==1:
            countRX += 1
        elif TCase[a][2-a]==2:
            countRO += 1
    if countLX==2 or countLO==2:
        for a in range(3):
            if TCase[a][a]==0:
                TCase[a][a]==2
    if countRX==2 or countRO==2:
        for a in range(3):
            if TCase[a][a]==0:
                TCase[a][a]==2
    #Jeu au hasard
    if RobotAJouer==False:
        if TCase[1][1]==0:
            TCase[1][1] = 2
        else:
            option = []
            for i in range(3):
                for j in range (3):
                    if TCase[i][j]==0:
                        option.append(i+j)
            choix = floor(random(0,len(option)))
            print option[choix]
            choixI = floor(option[choix]/3)
            choixJ = floor(option[choix]-(option[choix]/3)*3)
            TCase[choixI][choixJ] = 2
    print TCase
    Victoire()
#Analyse de la victoire
def Victoire():
    global tour
    global TCase
    count = 0
    for i in range(3):
        countO = 0
        countX = 0
        for j in range(3):
            if TCase[i][j]==1:
                countX += 1
                count += 1
            elif TCase[i][j]==2:
                countO += 1
                count += 1
        if countO==3:
            VictoryScreen(2)
        elif countX==3:
            VictoryScreen(1)
    for j in range(3):
        countO = 0
        countX = 0
        
        for i in range(3):
            if TCase[i][j]==1:
                countX += 1
            elif TCase[i][j]==2:
                countO += 1
        if countO==3:
            VictoryScreen(2)
        elif countX==3:
            VictoryScreen(1)
    #Gestion des diagonales
    countLX = 0
    countLO = 0
    countRX = 0
    countRO = 0
    for a in range(3):
        if TCase[a][a]==1:
            countLX += 1
        elif TCase[a][a]==2:
            countLO += 1
        if TCase[a][2-a]==1:
            countRX += 1
        elif TCase[a][2-a]==2:
            countRO += 1
    if countLX==3 or countRX==3:
        VictoryScreen(1)
    elif countLO==3 or countRO==3:
        VictoryScreen(2)
    if count==9:
        VictoryScreen(0)
    if tour==1:
        tour = 2
        IA()
    else:
        tour = 1
        print "A toi de Jouer"
