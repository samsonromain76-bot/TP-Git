import matplotlib.pyplot as plt
import numpy as np


coef_ue1={
    'R101':10,
    'R102':10,
    'R103':7,
    'R104':7,
    'R105':0,
    'R106':5,
    'R107':0,
    'R108':6,
    'R109':0,
    'R110':5,
    'R111':4,
    'R112':2,
    'R113':5,
    'R114':5,
    'R115':0,
    'SAE11':20,
    'SAE12':20,
    'SAE13':0,
    'SAE14':0,
    'SAE15':0,
    'SAE16':7}
notes1={
    'R101':18,
    'R102':18,
    'R103':18,
    'R104':18,
    'R105':18,
    'R106':18,
    'R107':18,
    'R108':18,
    'R109':18,
    'R110':18,
    'R111':18,
    'R112':18,
    'R113':18,
    'R114':18,
    'R115':18,
    'SAE11':18,
    'SAE12':18,
    'SAE13':18,
    'SAE14':18,
    'SAE15':18,
    'SAE16':18}
coef_ue2={
    'R101':4,
    'R102':0,
    'R103':2,
    'R104':8,
    'R105':6,
    'R106':0,
    'R107':0,
    'R108':0,
    'R109':0,
    'R110':5,
    'R111':5,
    'R112':2,
    'R113':9,
    'R114':9,
    'R115':3,
    'SAE11':0,
    'SAE12':0,
    'SAE13':29,
    'SAE14':0,
    'SAE15':0,
    'SAE16':7}

notes2={
    'R101':9,
    'R102':9,
    'R103':9,
    'R104':9,
    'R105':9,
    'R106':9,
    'R107':9,
    'R108':9,
    'R109':9,
    'R110':9,
    'R111':9,
    'R112':9,
    'R113':9,
    'R114':9,
    'R115':9,
    'SAE11':9,
    'SAE12':9,
    'SAE13':9,
    'SAE14':9,
    'SAE15':9,
    'SAE16':9}

coef_ue3={
    'R101':4,
    'R102':0,
    'R103':2,
    'R104':0,
    'R105':0,
    'R106':5,
    'R107':15,
    'R108':6,
    'R109':4,
    'R110':5,
    'R111':5,
    'R112':2,
    'R113':0,
    'R114':0,
    'R115':3,
    'SAE11':0,
    'SAE12':0,
    'SAE13':0,
    'SAE14':20,
    'SAE15':20,
    'SAE16':7}

notes3={
    'R101':3,
    'R102':3,
    'R103':3,
    'R104':3,
    'R105':3,
    'R106':3,
    'R107':3,
    'R108':3,
    'R109':3,
    'R110':3,
    'R111':3,
    'R112':3,
    'R113':3,
    'R114':3,
    'R115':3,
    'SAE11':3,
    'SAE12':3,
    'SAE13':3,
    'SAE14':3,
    'SAE15':3,
    'SAE16':3}

#https://stackoverflow.com/questions/29330792/weighted-averaging-a-list

somme=0#calcul de la moyenne de l'ue 1
for element in coef_ue1:
    somme = somme+coef_ue1[element]*notes1[element]
somme1=0
for element in coef_ue1:
    somme1=somme1 + coef_ue1[element]
moyenne1=0
moyenne1=somme/somme1
moyenne1

somme2=0#calcul de la moyenne de l'ue 2
for element in coef_ue2:
    somme2 = somme2+coef_ue2[element]*notes2[element]
somme21=0
for element in coef_ue1:
    somme21=somme21 + coef_ue2[element]
moyenne2=0
moyenne2=somme2/somme21
moyenne2

somme3=0#calcul de la moyenne de l'ue 3
for element in coef_ue3:
    somme3 = somme3+coef_ue3[element]*notes3[element]
somme31=0
for element in coef_ue3:
    somme31=somme31 + coef_ue3[element]
moyenne3=0
moyenne3=somme3/somme31
moyenne3

def get_color(value):#fonction qui change la couleur de la courbe en fonction des notes des ue
    if value>=10:
        return "green"
    elif 8<=value<10:
        return "orange"
    else:
        return "red"


colors=[get_color(val) for val in [moyenne1, moyenne2, moyenne3]]
plt.bar(["ue1", "ue2", "ue3"], [moyenne1, moyenne2, moyenne3], color=colors)

fenetre = tk.Tk()
fenetre.title("Affichage des coefficients")
fenetre.geometry("740x580")

# Création d'un Frame pour placer les labels
frm = ttk.Frame(fenetre)
frm.grid()

# Dictionnaire pour stocker les zones d'entrée par matière
note_matiere = {}

        

# Création des labels et zones de saisie
for i, element in enumerate(coef_ue1.keys()):
    matiere = ttk.Label(frm, text=element)
    matiere.grid(column=0, row=i)

    zone1 = ttk.Entry(frm)
    zone1.grid(column=1, row=i)

    note_matiere[element] = zone1  

image_label = tk.Label(fenetre)
image_label.grid(row=0, column=1, padx=20, pady=10)


def valider():
    for matiere, zone1 in note_matiere.items():
        notes[matiere] = float(zone1.get())


    # Calcul des moyennes
    list_value = (
        moyenne_ue(coef_ue1, "UE1"),
        moyenne_ue(coef_ue2, "UE2"),
        moyenne_ue(coef_ue3, "UE3")
    )

    print("Moyennes :", list_value)

     # Affichage du graphique dans Tkinter
    img = Image.open("graph.png")
    img = img.resize((500, 400))
    photo = ImageTk.PhotoImage(img)
    image_label.configure(image=photo)
    image_label.image = photo  # Important pour éviter le garbage collector

        
    fig, ax = plt.subplots()
    UE = ['UE1', 'UE2', 'UE3']
    counts = list_value
    bar_colors = get_colors(counts)
    ax.bar(UE, counts, color=bar_colors)
    ax.set_ylabel('notes')
    ax.set_title('valide ou pas')
    ax.set_ylim(0, 20)
    plt.show()


fig.savefig("graph.png")
plt.close(fig)

bouton1 = tk.Button(frm, text="Valider", command=valider)
bouton1.grid(column=0, row=len(coef_ue1)+1, columnspan=2, pady=10)




fenetre.mainloop()