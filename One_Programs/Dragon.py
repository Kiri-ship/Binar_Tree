from turtle import *
import itertools

interation = 15
Arr = ["F"]
Final_Arr = []


for a in range(interation):
    for i in range(len(Arr)):
        if Arr[i] == "":
            Final_Arr.append("F")

        elif Arr[i] == "F":
            Final_Arr += list("F-H")

        elif Arr[i] == "H":
            Final_Arr += list("F+H")

        elif Arr[i] == "-":
            Final_Arr += list("-")

        elif Arr[i] == "+":
            Final_Arr += list("+")

        else:
            pass
        
        Arr[i] = Final_Arr
        Final_Arr = []

    Arr = list(itertools.chain(*Arr))



angle = 90
stac_pos = []
stac_angle = []

stic = 2

# for draw speed(0)
tracer(0, 0)

hideturtle()


for g in range(len(Arr)):
    if Arr[g] == "":
        pass

    elif Arr[g] == "F":
        forward(stic)

    elif Arr[g] == "H":
        forward(stic)

    elif Arr[g] == "-":
        left(angle)

    elif Arr[g] == "+":
        right(angle)

    else:
        pass

update()
        

mainloop()