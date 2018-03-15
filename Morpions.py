import os;

t = [None,None,None],[None,None,None],[None,None,None];
player = False;
nombre_de_manche = 0;
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
    os.system("cls");
    i=0;
    print("    1   2   3")
    for i in (0,1,2):
        print(i+1,"|",t[i][0],"|",t[i][1],"|",t[i][2],"|");
    x = input("entrez une valeur de x : ");
    x = int(x)-1;
    while (x<0) or (x>2):
        x = input("erreur, entrez un nombre entre 1 et 3 : ");
        x = int(x)-1;
    y = input("entrez une valeur de y : ");
    y = int(y)-1;
    while (y<0) or (y>2):
        y = input("erreur, entrez un nombre entre 1 et 3 : ");
        y = int(x)-1;
    if t[x][y] is ' ':
        if player is False:
            t[x][y] = 'x';
            player = True;
        elif player is True:
            t[x][y] = 'y';
            player = False;
    i=0;
    while i<3:
        if ((t[i][0]=='x') and (t[i][1]=='x') and (t[i][2]=='x')) or ((t[0][i]=='x') and (t[1][i]=='x') and (t[2][i]=='x')) or ((t[0][0]=='x' or t[0][2]=='x') and (t[1][1]=='x') and (t[2][2]=='x' or t[2][0]=='x')):
            game_win = True;
            break;
        elif ((t[i][0]=='y') and (t[i][1]=='y') and (t[i][2]=='y')) or ((t[0][i]=='y') and (t[1][i]=='y')  and (t[2][i]=='y')) or ((t[0][0]=='y' or t[0][2]=='y') and (t[1][1]=='y') and (t[2][2]=='y' or t[2][0]=='y')):
            game_win = True;
            break;
        i = i+1;
    nombre_de_manche = nombre_de_manche+1;
    if nombre_de_manche == 9:
        break;

if player == True and nombre_de_manche < 9:
    print("félicitation X");
elif player == False and nombre_de_manche < 9:
    print("félicitation Y");
if nombre_de_manche == 9:
    print("match nul");
