import random

player = input("piedra, papel o tijera? :").lower()

my_random = ["Piedra", "papel", "tijera"]

my_random = random.choice(my_random)
print(my_random)

#Logica del juego
if player == my_random:
        print("Empate")
elif player == "piedra":
        if my_random == "papel":
            print("Perdiste! ", my_random, " > ", player)
        else:
            print("Ganaste !", player, " < ", my_random)
elif player == "papel":
        if my_random == "tijera":
            print("Perdiste! ", my_random, " > ", player)
        else:
            print("Ganaste! ", player, " < ", my_random)
elif player == "tijera":
        if my_random == "piedra":
            print("Perdiste! ", my_random, " > ", player)
        else:
            print("Ganaste! ", player, " < ", my_random)
