import dearpygui.dearpygui as dpg

from Lsys import Pifagor_tree
from Lsys import Dragon_Line
from Lsys import Serpinsky_treangle

BLACK = (0, 0, 0)




#---Menu------------------------------------------------------------------------------------------------------------


Item_List = ["Pifagor Tree", "Dragon Line", "Serpinsky's treangle"]
    
def Start_Callback(sender):
    print("You Cliced Start!!!")
    print("Starting ", dpg.get_value("combo_box"))
    
    
    if dpg.get_value("combo_box") == "Pifagor Tree":
        interation = dpg.get_value("slider_int")
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

#---Menu------------------------------------------------------------------------------------------------------------

#---Node-Editor-----------------------------------------------------------------------------------------------------

def add_node(sender, app_data):
    with dpg.node_editor(label="Node Editor", parent="nod"):
        with dpg.node(label="node"):
            with dpg.node_attribute(label="Node A1"):
                dpg.add_input_float(label="F1", width=150)

#---Node-Editor-----------------------------------------------------------------------------------------------------




dpg.create_context()
dpg.create_viewport(title='L-system Vizualizer', width=1115, height=690)



with dpg.window(label="Setup L-system Vizualizer", width=300, height=650, no_title_bar=True):

    dpg.add_combo(label="L-system", items=Item_List, tag="combo_box")
    dpg.add_slider_int(label="interations", default_value=1, min_value=1, max_value=8, tag="slider_int")
    dpg.add_slider_int(label="angle", default_value=1, min_value=1, max_value=360, tag="angle")
    dpg.add_button(label="Start ", callback=Start_Callback)
    dpg.add_button(label="Repeat", callback=Repeat_Callback)
    dpg.add_button(label="Stop  ", callback=Stop_Callback)
    dpg.add_button(label="Add Node  ")




with dpg.window(label="Draw", width=800, height=650, pos=[300, 0], no_title_bar=True, tag="Draw"):
    dpg.add_button(label="Add Node", callback=add_node)

        
    dpg.add_node_editor(tag="nod")
        
        
        
            
                 


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()


 



