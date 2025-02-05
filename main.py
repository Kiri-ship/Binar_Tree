import dearpygui.dearpygui as dpg

from Lsys import Pifagor_tree
from Lsys import Dragon_Line
from Lsys import Serpinsky_treangle

from MyTurtle import MyTurtle

BLACK = (0, 0, 0)

Item_List = ["Pifagor Tree", "Dragon Line", "Serpinsky's treangle"]
    
def Start_Callback(sender):
    print("You Cliced Start!!!")
    print("Starting ", dpg.get_value("combo_box"))
    
    
    if dpg.get_value("combo_box") == "Pifagor Tree":
        interation = dpg.get_value("slider_int")
        print(interation)
        Tree = Pifagor_tree(BLACK, interation)
        String = Tree.Generate_String()
        Tree.Draw(String)

    elif dpg.get_value("combo_box") == "Dragon Line":
        interation = dpg.get_value("slider_int")
        DragonLine = Dragon_Line(BLACK, interation)
        String = DragonLine.Generate_String()
        DragonLine.Draw(String)

    elif dpg.get_value("combo_box") == "Serpinsky's treangle":
        interation = dpg.get_value("slider_int")
        Serpinsky = Serpinsky_treangle(BLACK, interation)
        String = Serpinsky.Generate_String()
        Serpinsky.Draw(String)

    
def Repeat_Callback(sender):
    print("You Cliced Repeat!!!")

def Stop_Callback(sender):
    print("You Cliced Stop!!!")

dpg.create_context()
dpg.create_viewport(title='L-system Vizualizer', width=1100, height=650)



with dpg.window(label="Setup L-system Vizualizer", width=300, height=650):

    dpg.add_combo(label="L-system", items=Item_List, tag="combo_box")
    dpg.add_slider_int(label="interations", default_value=1, min_value=1, max_value=8, tag="slider_int")
    dpg.add_slider_int(label="angle", default_value=1, min_value=1, max_value=360, tag="angle")
    btn1 = dpg.add_button(label="Start ", callback=Start_Callback)
    btn2 = dpg.add_button(label="Repeat", callback=Repeat_Callback)
    btn3 = dpg.add_button(label="Stop  ", callback=Stop_Callback)




with dpg.window(label="Draw", width=800, height=650, pos=[300, 0], no_title_bar=True):

    with dpg.drawlist(label="Draw", width=800, height=650):

        Turtle = MyTurtle(50, 50, 0)
        Turtle.Forward(50)
        Turtle.Raight(45)
        Turtle.Forward(50)
        Turtle.Forward(50)
        Turtle.Forward(50)
        Turtle.Forward(50)
        Turtle.Forward(50)
        Turtle.Forward(50)
        Turtle.Forward(50)
        Turtle.Left(20)
        Turtle.Forward(50)
        Turtle.Forward(50)
                 


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()


 



