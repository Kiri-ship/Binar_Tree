from turtle import *
import itertools


interation = 6
Arr = ["F", "-", "G", "-", "G"]
Final_Arr = []


for a in range(interation):
    for i in range(len(Arr)):
        if Arr[i] == "":
            Final_Arr.append("F")

        elif Arr[i] == "F":
            Final_Arr += list("F-G+F+G-F")

        elif Arr[i] == "G":
            Final_Arr += list("GG")

        elif Arr[i] == "-":
            Final_Arr += list("-")

        elif Arr[i] == "+":
            Final_Arr += list("+")

        else:
            pass
        
        Arr[i] = Final_Arr
        Final_Arr = []

    Arr = list(itertools.chain(*Arr))


#print(Arr)



angle = 120
stac_pos = []
stac_angle = []

stic = 8

speed(0)
up()
sety(-200)
setx(-200)
hideturtle()
down()


for g in range(len(Arr)):
    if Arr[g] == "":
        pass

    elif Arr[g] == "F":
        forward(stic)

    elif Arr[g] == "G":
        forward(stic)

    elif Arr[g] == "-":
        left(angle)

    elif Arr[g] == "+":
        right(angle)

    else:
        pass
        

mainloop()
