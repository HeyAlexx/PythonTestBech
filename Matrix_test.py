import os
import os.path
from os.path import isdir,isfile
import pathlib


DPath = ("E:\\Descargas\\PruebasAnime")
DPath2 = ("E:\\Descargas\\Anime")
Paths = ("E:\\Descargas")
DPath3 = (r"E:\Descargas\Anime\Anime 2024-3\(4032)Katsute Mahou Shoujo to Aku wa Tekitai shiteita\[4032]Katsute Mahou Shoujo to Aku wa Tekitai shiteita 9.mp4")
matrix = [[]]



ans = os.path.isfile(DPath3)
print(ans) 

ans1 = os.path.isdir(DPath3)
print(ans1)

ans2 = os.path.exists(DPath3)    
print(ans2)

list_files = os.listdir(DPath2)
if list_files is not None or ("Thumbs.db"):
    for file_name in list_files:
        for r in matrix[:]:
            if file_name.isdir:
                matrix[r] = file_name
                  

