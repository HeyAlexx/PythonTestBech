import os
import os.path
from os.path import isdir
import string
import pathlib
import time



FilePath1 = (r"E:\Descargas\Anime")
FilePath = (r"E:\Descargas\PruebasAnime")
fff = ("(2370)Gate; Jieitai Kanochi nite, Kaku Tatakaeri - Enryuu-hen")
#Ex =("2370")
origin = ("")
Destiny = ("")
conteo = 0


def UserInput():
    value = input("Write a number to search")
    while not value.isnumeric():
        print("enter a number")
        value = input("enter again")
        int(value)
        print(value.type)
    NValue = str(value)
    return value        



def walking(directory,func,*args):
    list_Files = os.listdir(directory)
    if list_Files is not None:
        for file_name  in list_Files:
            file_path = os.path.join(directory, file_name)# Construct the full path of the file or directory
            if os.path.isdir(file_path):
                #print("** " + file_name)
                #WriteFiles(file_name)
                #Checker(x, y)  #Funcion que verifica coincidencia con dato solicitado
                func(file_name,*args) # Funcion pasada como argumento
                walking(file_path, func,*args) # Recursively walk through subdirectories
            else:
                func(file_name,*args) # Funcion pasada como argumento
                #print("- " + file_name)3966
                


def Checkers(name, need):
    found = need in name
    
    if found is True:# Check if the string "need" is in the file_name
        namePath = os.path.join(FilePath,name)
        print(namePath)
        #conteo = conteo += 1
        #print() 
        # Uncomment the line below if you want a delay
        time.sleep(2)
    else:
        print("not coincidence")              




Ex = UserInput()

# Call the walking function with the directory path, the Checkers function, 
# and the string to search for
walking(FilePath,Checkers,Ex)
#Checkers(fff,"2370")       