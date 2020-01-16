# __author__ = 'dev'
#
# name = input("please enter your name: ")
# age = int(input("How old are you {0}? ".format(name)))
# print(age)
#
# if age >= 18:
#    print("You are old enough to vote")     # The conditional is true !
#    print("pleas put an X in the Box")
# else:
#    print("Please come back in {0} , Years! ".format(18-age))   # Minor to 18
from datetime import date  #Libreria de Tiempos

#Hay que traducir los meses en Ingles al espaniol
anio = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
today = date.today()
mes = today.strftime("%B , %m")
nombre_mes = anio[int(today.strftime("%m"))-1] #Le resto uno ya que en el index cero tengo el mes de enero
dia = today.strftime("%d")

print("Es el mes de {0} {1} !!!!! ".format(nombre_mes, dia))

# Textual month, day and year
d2 = today.strftime("%B %d, %Y")
print("Hoy es ", d2)
print(mes)
print(dia)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)



print("Please guess a number between 1 to 10: ")
guess = int(input())

if guess < 5:
    print("Please guess higher ")
    guess = int(input())
    if guess == 5:
        print("Well done, you guess it ")
    else:
        print("Sorry, you have not guessed correctly")
elif guess > 5:
    print("Please guess Lower")
    guess = int(input())
    if guess == 5:
        print("Well done, you guess it ")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time")
