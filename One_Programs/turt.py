from turtle import *
import itertools

interation = 8
Arr = ["0"]
Final_Arr = []


for a in range(interation):
    for i in range(len(Arr)):
        if Arr[i] == "":
            Final_Arr.append("0")

        elif Arr[i] == "0":
            Final_Arr += list("1[0]0")

        elif Arr[i] == "1":
            Final_Arr += list("11")

        elif Arr[i] == "[":
            Final_Arr += list("[")
        
        elif Arr[i] == "]":
            Final_Arr += list("]")
        
        Arr[i] = Final_Arr
        Final_Arr = []

    
    
    Arr = list(itertools.chain(*Arr))



angle = 45
stac_pos = []
stac_angle = []

stic = 2
leaf = 3

# for draw speed(0)
tracer(0, 0)  
up()
sety(-300)
left(90)
hideturtle()
down()

for g in range(len(Arr)):
    if Arr[g] == "":
        pass

    elif Arr[g] == "0":
        forward(leaf)

    elif Arr[g] == "1":
        forward(stic)

    elif Arr[g] == "[":
        stac_pos.append(pos())
        stac_angle.append(heading())
        left(angle)
        
    elif Arr[g] == "]":
        up()
        goto(stac_pos[-1])
        down()
        del stac_pos[-1]
        setheading(stac_angle[-1]) 
        del stac_angle[-1]
        right(angle)

update()

mainloop()