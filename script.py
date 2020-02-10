import math

def convertDecToHex(decimal):
    values = []
    while True:
        decimal = decimal / 16
        if int(decimal) == 0:
            values.append(decimal * 16)
            break
        else:
            values.append((decimal % int(decimal)) * 16)
        decimal = int(decimal)
    hex_values = []
    for num in reversed(values):
        if num >= 0 and num < 10:
            hex_values.append(int(num))
        elif num == 10:
            hex_values.append("A")
        elif num == 11:
            hex_values.append("B")
        elif num == 12:
            hex_values.append("C")
        elif num == 13:
            hex_values.append("D")
        elif num == 14:
            hex_values.append("E")
        elif num == 15:
            hex_values.append("F")
    hex_num = ""
    for x in hex_values:
        hex_num += str(x)
    print("This is your number in hex: " + hex_num)

def convertHexToDec(hexadecimal):
    decimal = 0
    power = 0
    for x in reversed(hexadecimal):
        if (x.isalpha()):
            if (x == 'A'):
                x = 10
            elif (x == 'B'):
                x = 11
            elif (x == 'C'):
                x = 12
            elif (x == 'D'):
                x = 13
            elif (x == 'E'):
                x = 14
            elif (x == 'F'):
                x = 15
        else:
            x = int(x)

        decimal += x * pow(16, power)
        power += 1
    print(decimal)

user_txt = input("Give me a hexadecimal number: ")

convertHexToDec(user_txt)