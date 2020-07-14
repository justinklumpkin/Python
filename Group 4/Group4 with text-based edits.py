import Group4
from tkinter import* 



def calc_dist():
    Group4.measurements_file("F:/Pythonprojects/Group 4/experiment dimensions.txt")
    Group4.calculate_distance(bat_mass.get(), ball_mass.get(), bat_type.get(), "F:\Pythonprojects\Group 4\efficiency.txt")

ans='0'

while ans!='3':
    ans =input("1)Run with default dimensions\n2)Customize dimensions\n3)Exit\n\n")
    if ans == '1':
        Group4.dist_file("F:/Pythonprojects/Group 4/group 4.txt")
        Group4.clean_data()
            #uses the distances variable stores distances
            #separatelly for each bat
            #and adds the average as the last element
        Group4.measurements_file("F:/Pythonprojects/Group 4/experiment dimensions.txt")
        Group4.calc_bat_stats(Group4.abat)
        Group4.calc_bat_stats(Group4.wbat)
        Group4.calc_bat_stats(Group4.pbat)
    if ans == '2':
        master = Tk()
        bat_lab=Label(master, text="Bat Mass (kg)")
        bat_lab.pack()
        bat_mass = Scale(master, from_=0.0, to=3.0, resolution =.001,orient = HORIZONTAL, length= 800)
        bat_mass.pack()
        ball_lab=Label(master, text="Ball Mass (kg)")
        ball_lab.pack()
        ball_mass=Scale(master, from_=0.0, to=1.0, resolution =.001,orient = HORIZONTAL, length= 800)
        ball_mass.pack()
        type_lab=Label(master, text="Bat Material")
        type_lab.pack()
        bat_type = StringVar(master)
        bat_type.set("Aluminum") # default value
        material = OptionMenu(master, bat_type, "Aluminum", "Wood", "Plastic")
        material.pack()
        Button(master, text='Calculate Distance', command=calc_dist).pack()
        master.mainloop() 
