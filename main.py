#!usr/bin/python

import os

G = '\033[32m'
R = '\033[31m'
W = '\033[0m'
os.system('clear')

print(G + '''
 ____       _           _ _   _           _____
|  _ \ _ __(_)_ __ ___ (_) |_(_)_   _____|___ /
| |_) | '__| | '_ ` _ \| | __| \ \ / / _ \ |_ \ 
|  __/| |  | | | | | | | | |_| |\ V /  __/___) |
|_|   |_|  |_|_| |_| |_|_|\__|_| \_/ \___|____/
                    herramientas para hackear
''')

print("")


print("1 - precione 1 para actualizar sus repos")

print("2 - precione 2 para instalar Nmap")

print("3 - precione 3 para clonar PyPhysher")

print("4 - precione 4 para instalar Hulk para hacer ataques dos")

print("5 - precione 5 para salir")

def menu():
    print("1 - precione 1 para actualizar sus repos")
    print("2 - precione 2 para instalar Nmap")

while True:
    opcionMenu = input(G + "escriba una opcion de arriba: " + G)
    if opcionMenu=="1":
        print("")
        os.system('pkg update && pkg upgrade -y')
        os.system('clear')
        print("")
    elif opcionMenu=="2":
        print("")
        os.system('pkg install nmap')
        os.system('clear')
        print("")
    elif opcionMenu=="3":
        print("")
        os.system("git clone https://github.com/KasRoudra/PyPhisher")
        os.system('clear')
        print("")
    elif opcionMenu=="4":
        print("")
        os.system("git clone https://github.com/grafov/hulk")
        os.system('clear')
    elif opcionMenu=="5":
        print("")
        break

    else:
        print("")
        input("precione enter para volver a eleguir un numero")
        print("")


