from turtle import *
import itertools



class Lsys:
    def __init__(self, color, interations):
        self.color = color
        self.interations = interations


    def Generate_String(self):
        pass


    def Draw(self):
        pass




class Pifagor_tree(Lsys):
    def __init__(self, color, interations):
        super().__init__(color, interations)



    def Generate_String(self):
        
        self.Arr = ["0"]
        Final_Arr = []

        for a in range(self.interations):
            for i in range(len(self.Arr)):
                if self.Arr[i] == "":
                    Final_Arr.append("0")

                elif self.Arr[i] == "0":
                    Final_Arr += list("1[0]0")

                elif self.Arr[i] == "1":
                    Final_Arr += list("11")

                elif self.Arr[i] == "[":
                    Final_Arr += list("[")
        
                elif self.Arr[i] == "]":
                    Final_Arr += list("]")
        
                self.Arr[i] = Final_Arr
                Final_Arr = []

            self.Arr = list(itertools.chain(*self.Arr))

        return self.Arr


    def Draw(self, Arr):

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



class Dragon_Line(Lsys):
    def __init__(self, color, interations):
        super().__init__(color, interations)


    def Generate_String(self):
        Arr = ["F"]
        Final_Arr = []


        for a in range(self.interations):
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

        return Arr
    

    def Draw(self, Arr):
        angle = 90
        stac_pos = []
        stac_angle = []

        stic = 5

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





class Serpinsky_treangle(Lsys):
    def __init__(self, color, interations):
        super().__init__(color, interations)


    def Generate_String(self):
        Arr = ["F", "-", "G", "-", "G"]
        Final_Arr = []


        for a in range(self.interations):
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

        return Arr



    def Draw(self, Arr):
        angle = 120
        stac_pos = []
        stac_angle = []

        stic = 8

        # for draw speed(0)
        tracer(0, 0)
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
        
        update()
        mainloop()