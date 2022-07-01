import logic_base as logic 

"""This program is used to simulaite a copy of the original enigma machine. It was originaly made by Dr Arthur Scherbius and upgraded by the germans before WW2 and cracked by french and polish secret services before WW2"""

enigma = logic.rotors(2)
enigma.encode()