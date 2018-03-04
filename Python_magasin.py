import string

student = [
    ("a","b","TB",20),
    ("c","d","B",16),
    ("e","f","B",18),
    ("g","h","A",12),
    ("i","j","E",8),
    ("k","l","I",9),
];
student_inversed = [(nom,prenom,note,nombre) for nombre,prenom,note,nom in student];

student_inversed.sort(reverse=True);

student = [(nom,prenom,note,nombre) for nombre,prenom,note,nom in student_inversed];

for i,j in enumerate(student):
    print("voici {} ".format(student[i]));