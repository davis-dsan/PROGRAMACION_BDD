player = input("Piedra, Papel o Tijera? :")
computer = input("Piedra, Papel o Tijera? :")

#Logica del juego
if player == computer:
        print("Empate")
elif player == "Piedra":
        if computer == "Papel":
            print("Perdiste! ", computer, " > ", player)
        else:
            print("Ganaste !", player, " < ", computer)
elif player == "Papel":
        if computer == "Tijera":
            print("Perdiste! ", computer, " > ", player)
        else:
            print("Ganaste! ", player, " < ", computer)
elif player == "Tijera":
        if computer == "Piedra":
            print("Perdiste! ", computer, " > ", player)
        else:
            print("Ganaste! ", player, " < ", computer)
else:
        print("Opción no valida, Intentar escribir las opciones como se las ve.")