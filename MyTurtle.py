import math
import dearpygui.dearpygui as dpg


class MyTurtle:

    def __init__(self, X0, Y0, angle):

        self.angle = angle
        self.X0 = X0
        self.Y0 = Y0
        
        
    def Forward(self, lenth):

        X1 = self.X0 + lenth * math.cos(math.radians(self.angle))
        Y1 = self.Y0 + lenth * math.sin(math.radians(self.angle))
        
        dpg.draw_line((self.X0, self.Y0), (int(X1), int(Y1)))

        self.X0 = X1
        self.Y0 = Y1



    def Raight(self, ang):
        self.angle += ang



    def Left(self, ang):
        self.angle -= ang



    def Set_Pos(self, Arr):
        self.X0 = Arr[0]
        self.Y0 = Arr[1]



    def Set_Angle(self, angl):
        self.angle = angl




    def Get_Pos(self):
        Arr = [self.X0, self.Y0]
        return Arr



    def Get_Angle(self):
        return self.angle

        
