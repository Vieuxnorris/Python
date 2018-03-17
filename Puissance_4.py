import os

t = [[None,None,None,None,None,None,None],
     [None,None,None,None,None,None,None],
     [None,None,None,None,None,None,None],
     [None,None,None,None,None,None,None],
     [None,None,None,None,None,None,None],
     [None,None,None,None,None,None,None]];

game_win = False;
player = False;

print("    1    2    3    4    5    6    7  ");
for i in range(0,len(t)):
        for j in range(0,len(t[i])):
                        t[i][j] = ' ';
        print(i+1,t[i]);
while game_win == False:
    j=0;
    nombre = input("entrez un nombre : ");
    nombre = int(nombre)-1;
    while j < 6:
        if t[5][nombre] == ' ' and player == False:
            t[5][nombre] = 'x';
            player = True;
            break;
        elif (t[j][nombre] == 'y' or t[j][nombre] == 'x') and player == False:

            if t[j-1][nombre] == ' ':
                t[j-1][nombre] = 'x';
            else:
                break;
            player = True;
            break;
        if t[5][nombre] == ' ' and player == True:
            t[5][nombre] = 'y';
            player = False;
            break;
        elif (t[j][nombre] == 'y' or t[j][nombre] == 'x') and player == True:
            if t[j-1][nombre] == ' ':
                t[j-1][nombre] = 'y';
            else:
                break;
            player = False;
            break;
        j = j+1;
    compteur=0;
    for l in range(0,len(t)):
            for m in range(0,len(t[l])):
                if (t[l][m]=='x' and t[l-1][m]=='x' and t[l-2][m]=='x' and t[l-3][m]=='x') or (t[l][m]=='y' and t[l-1][m]=='y' and t[l-2][m]=='y' and t[l-3][m]=='y'):
                    game_win = True;
                if (t[l][m]=='x' and t[l][m+1]=='x' and t[l][m+2]=='x' and t[l][m+3]=='x') or (t[l][m]=='y' and t[l][m+1]=='y' and t[l][m+2]=='y' and t[l][m+3]=='y'):
                    game_win = True;
                if (t[l][m]=='x' and t[l-1][m+1]=='x' and t[l-2][m+2]=='x' and t[l-3][m+3]=='x') or (t[l][m]=='y' and t[l-1][m+1]=='y' and t[l-2][m+2]=='y' and t[l-3][m+3]=='y'):
                    game_win = True;
                if (t[l][m]=='x' and t[l-1][m-1]=='x' and t[l-2][m-2]=='x' and t[l-3][m-3]=='x') or (t[l][m]=='y' and t[l-1][m-1]=='y' and t[l-2][m-2]=='y' and t[l-3][m-3]=='y'):
                    game_win = True;
    os.system("cls");
    print("    1    2    3    4    5    6    7  ");
    for k in range(0,len(t)):
            print(k+1,t[k]);
print("win");
