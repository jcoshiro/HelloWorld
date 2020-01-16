ipAdress = input("Por favor ingrese un numero IP: ")

segment = 1
segment_lenght = 0
character = ""
for character in ipAdress:
    if character == ".":
        print("segment {} contains {} characters ".format(segment, segment_lenght))
        segment += 1
        segment_lenght = 0
    else:
        segment_lenght += 1

if character != '.':
    print("segment {} contains {} characters ".format(segment, segment_lenght))

