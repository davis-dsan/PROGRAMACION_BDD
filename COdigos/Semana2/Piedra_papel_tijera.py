player = input("piedra, papel o tijera? :").lower()

computer = "Piedra".lower()

#Logica del juego
if player == computer:
        print("Empate")
elif player == "piedra":
        if computer == "papel":
            print("Perdiste! ", computer, " > ", player)
        else:
            print("Ganaste !", player, " < ", computer)
elif player == "papel":
        if computer == "tijera":
            print("Perdiste! ", computer, " > ", player)
        else:
            print("Ganaste! ", player, " < ", computer)
elif player == "tijera":
        if computer == "piedra":
            print("Perdiste! ", computer, " > ", player)
        else:
            print("Ganaste! ", player, " < ", computer)
