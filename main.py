import logic_base as logic 

"""This program is used to simulaite a copy of the original enigma machine. It was originaly made by Dr Arthur Scherbius and upgraded by the germans before WW2 and cracked by french and polish secret services before WW2"""

end = False 

enigma = logic.rotors(1)

while not end:
    action = input("Do you want to encrypt (E) or decrypt (D) ? ")
    if action == "E":
        enigma.encode()
        end =  True 
    elif action == "D":
        enigma.decode()
        end = True 
    else:
        print("Unknown action")
        end = False 
        continue 