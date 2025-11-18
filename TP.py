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
notes1=[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18]  # on test pour une UE dans le vert

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

notes2=[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9] # on teste avec une UE en orange


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

notes3=[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3] # on teste avec une UE en rouge


#https://stackoverflow.com/questions/29330792/weighted-averaging-a-list

l=coef_ue1.values()
print(l)
moyenne1=np.average(notes1,l)



