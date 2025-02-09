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


    def Draw(self, Arr, turtle_screen):
        
        t = RawTurtle(turtle_screen)
        angle = 45
        stac_pos = []
        stac_angle = []

        stic = 2
        leaf = 3

        t.speed(0)  
        t.up()
        t.sety(-300)
        t.left(90)
        t.hideturtle()
        t.down()

        for g in range(len(Arr)):
            if Arr[g] == "":
                pass

            elif Arr[g] == "0":
                t.forward(leaf)

            elif Arr[g] == "1":
                t.forward(stic)

            elif Arr[g] == "[":
                stac_pos.append(t.pos())
                stac_angle.append(t.heading())
                t.left(angle)
        
            elif Arr[g] == "]":
                t.up()
                t.goto(stac_pos[-1])
                t.down()
                del stac_pos[-1]
                t.setheading(stac_angle[-1]) 
                del stac_angle[-1]
                t.right(angle)

        



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
    

    def Draw(self, Arr, turtle_screen):

        t = RawTurtle(turtle_screen)

        angle = 90
        stac_pos = []
        stac_angle = []

        stic = 5

        # for draw speed(0)
        t.speed(0)
        t.hideturtle()

        for g in range(len(Arr)):
            if Arr[g] == "":
                pass

            elif Arr[g] == "F":
                t.forward(stic)

            elif Arr[g] == "H":
                t.forward(stic)

            elif Arr[g] == "-":
                t.left(angle)

            elif Arr[g] == "+":
                t.right(angle)

            else:
                pass
        
        





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



    def Draw(self, Arr, turtle_screen):

        t = RawTurtle(turtle_screen)

        angle = 120
        stac_pos = []
        stac_angle = []

        stic = 8

        t.speed(0)
        t.up()
        t.sety(-200)
        t.setx(-200)
        t.hideturtle()
        t.down()


        for g in range(len(Arr)):
            if Arr[g] == "":
                pass

            elif Arr[g] == "F":
                t.forward(stic)

            elif Arr[g] == "G":
                t.forward(stic)

            elif Arr[g] == "-":
                t.left(angle)

            elif Arr[g] == "+":
                t.right(angle)

            else:
                pass
        
