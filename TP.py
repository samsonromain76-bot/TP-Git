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