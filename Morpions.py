t = [None,None,None],[None,None,None],[None,None,None];
player = False;
game_win = False;
compteur = 0;
i=0;
j=0;
x=0;
y=0;

for i in (0,1,2):
        for j in (0,1,2):
            t[i][j] = ' ';

while game_win == False:
    i=0;
    for i in (0,1,2):
        print(t[i][0],t[i][1],t[i][2]);
    x = input("entrez une valeur de x : ");
    x = int(x)-1;
    y = input("entrez une valeur de y : ");
    y = int(y)-1;
    if t[x][y] is ' ':
        if player is False:
            t[x][y] = 'x';
            player = True;
        elif player is True:
            t[x][y] = 'y';
            player = False;
    while i<3:
        if (t[i][0]=='x') and (t[i][1]=='x') and (t[i][2]=='x'):
            game_win = True;
            break;
        elif (t[i][0]=='y') and (t[i][1]=='y') and (t[i][0]=='y'):
            game_win = True
            break;
        i = i+1;
    i=0;
    while i<3:
        if (t[0][i]=='y') and (t[1][i]=='y')  and (t[2][i]=='y'):
            game_win = True;
            break;
        elif (t[0][i]=='x') and (t[1][i]=='x') and (t[2][i]=='x'):
            game_win = True;
            break;
        i = i+1;
    i=0;
    while i<3:
        if(t[0][0]=='y' or t[0][2]=='y') and (t[1][1]=='y') and (t[2][2]=='y' or t[2][0]=='y'):
            game_win = True;
            break;
        elif(t[0][0]=='x' or t[0][2]=='x') and (t[1][1]=='x') and (t[2][2]=='x' or t[2][0]=='x'):
            game_win = True;
            break;
        i = i+1;
if player == True:
    print("félicitation X");
else:
    print("félicitation Y");