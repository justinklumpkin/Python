import statistics, numpy, math



distances=[]#stores all of the distances that the ball was hit
            #first is aluminum, then wood, then plastic. there are 15
            #trials per bat

#the following 3 variables are the same as distances,
#but with the values separated by bat type
alum=[0]
wood=[0]
plas=[0]

#these will store the average distance for each bat and their mass
abat= None
wbat= None
pbat= None

class Bat():#a bat contains the average distance that the ball was hit and its mass
    def __init__(self,n='bat', average=0, mass=0):
        self.name =n.title()
        self.avg = average
        self.mass = mass
    def momentum(self, velocity):#easily calculates momentum given velocity
        return self.mass*velocity
    
    def kinetic(self, velocity):#easily calculates kinetic energy
                                #of the bat given velocity
        return 0.5*self.mass*(velocity**2)

    def potential(self, height):#easily calculates potential energy of
                                #the bat given a height
        return 9.8*self.mass*height
    
    def __str__(self): #prints a string representation of the bat (measurements accurate to 4 decimals)
        return('\n'+self.name +" hit an average distance of "+
              str('%.4f'%self.avg)+" m. It has a mass of "+str('%.4f'%self.mass)+" kg.\n")
    #def calc_avg():
#Measurements
DATA={'string_length':None, 'tee_height':None, 'bat_xpos_0':None, 'ball_mass':None} 
def dist_file(filename):
    with open(filename) as f:
        for num in f:
            d = float(num)
            distances.append(d)
    '''print(distances)'''
def clean_data():
    global alum, wood, plas
    alum = distances[:15]
    wood = distances[15:30]
    plas = distances[30:]

    alum.append(sum(alum)/len(alum))
    wood.append(sum(wood)/len(wood))
    plas.append(sum(plas)/len(plas))


def measurements_file(filename):
    global alum, wood, plas, abat, wbat, pbat, DATA
    with open(filename) as f:
        for line in f:
            if line.find('mass_')==-1:
                dimension =line[:line.find(' ')]#the dimension that is being set
                value=float(line[line.find(' ')+1:])#the value to set it to
                DATA[dimension]=value
            elif line.find('aluminum')!=-1:
                abat = Bat(n='aluminum',average = alum[-1],mass = float(line[line.find(' '):]))
            elif line.find('wood')!=-1:
                wbat = Bat(n='wood',average = wood[-1],mass = float(line[line.find(' '):]))
            elif line.find('plastic')!=-1:
                pbat = Bat(n='plastic',average = plas[-1],mass = float(line[line.find(' '):]))


def calc_bat_stats(bat):
    global DATA
    print('-------------------------------------------',bat)
    #calculate the height change from top to bottom of swing using pythagorean theorem
    DATA['bat_height_change']=DATA['string_length']-math.sqrt(DATA['string_length']**2-DATA['bat_xpos_0']**2)
    print("Height change is: " +str('%.4f'%DATA['bat_height_change'])+" m.")

    #calculate the velocity of the bat just before it hits the ball using mgh=.5mv**2 -> v=sqrt(2gh)
    bat_velocity_precollision = math.sqrt(19.6*DATA['bat_height_change'])
    print(bat.name+"'s velocity just before hitting the ball is: " +str('%.4f'%bat_velocity_precollision)+" m/s.")

    #calculate the time it takes the ball to hit the ground y=4.9*t**2 -> t=sqrt(y/4.9)
    time= math.sqrt(DATA['tee_height']/4.9)
    print('The ball takes '+str('%.4f'%time)+' s to hit the ground.')

    #calculate the velocity of the ball v=dist/time
    ball_velocity = bat.avg/time
    print("The ball's horizontal velocity after collision is "+str('%.4f'%ball_velocity)+' m/s.')
    
    #calculate all of the momentums momentum = mass*velocity
    ball_momentum= ball_velocity*DATA['ball_mass']
    print("Momentums (in kg m/s): ")
    print("\tBat before collision: "+str('%.4f'%bat.momentum(bat_velocity_precollision)))
    print("\tBall after collision: "+str('%.4f'%ball_momentum))
    print("\tBat after collision: "+str('%.4f'%(bat.momentum(bat_velocity_precollision)-ball_momentum)))

    #calculate percent of momentum conserved
    transferred_momentum=ball_momentum/bat.momentum(bat_velocity_precollision)
    print("Momentum transfer efficiency from bat to ball: "+ "{:.4%}".format(transferred_momentum))

    #calculate all of the kinetic energies.  ke=0.5*mass*velocity
    ball_energy=0.5*DATA['ball_mass']*ball_velocity**2

    print("Energies (in J): ")
    print("\tBat before collision: "+str('%.4f'%bat.kinetic(bat_velocity_precollision)))
    print("\tBall after collision: "+str('%.4f'%ball_energy))
    print("\tBat after collision: "+str('%.4f'%(bat.kinetic(bat_velocity_precollision)-ball_momentum)))

    #calculate percent of energy conserved
    transferred_energy=ball_energy/bat.kinetic(bat_velocity_precollision)
    print("Kinetic Energy transfer efficiency from bat to ball: "+ "{:.4%}".format(transferred_energy))
    '''efficiency_file = open("F:\Pythonprojects\Group 4\efficiency.txt","a")
    efficiency_file.write(bat.name+' '+str(transferred_momentum)+'\n')#only needed to run once'''
    print('-------------------------------------------')
#calculate dist from rest-----------------------------
def calculate_distance(bat=1, ball=.1, material='Aluminum', effic="F:\Pythonprojects\Group 4\efficiency.txt"):
    EFFICIENCY= {'Aluminum':None, 'Wood':None,'Plastic':None}#%of nrg transferred in collision
    with open(effic) as f:
        for line in f:
            mat =line[:line.find(' ')]#the material that is being set
            value=float(line[line.find(' ')+1:-1])#the value to set it to
            EFFICIENCY[mat]=value
    print('-------------------------------------------'+'\n'+material+' bat of mass '+str(bat)+' kg vs. ball of mass '+str(ball)+' kg.')
    #calculate the height change from top to bottom of swing using pythagorean theorem
    DATA['bat_height_change']=DATA['string_length']-math.sqrt(DATA['string_length']**2-DATA['bat_xpos_0']**2)
    print("Height change is: " +str('%.4f'%DATA['bat_height_change'])+" m.")

    #calculate the velocity of the bat just before it hits the ball using mgh=.5mv**2 -> v=sqrt(2gh)
    bat_velocity = math.sqrt(19.6*DATA['bat_height_change'])
    print("Bat velocity just before hitting the ball is: " +str('%.4f'%bat_velocity)+" m/s.")

    #calculate energy of the bat just before collision
    bat_energy=0.5*bat*bat_velocity**2
    print("The bat has " + str('%.4f'%bat_energy)+ " J before hitting the ball.")

    #calculate the amount of energy given to the ball
    ball_energy = bat_energy*EFFICIENCY[material]
    print(material+" bats transfer "+"{:.4%}".format(EFFICIENCY[material])+" of their energy.")
    print("The ball will have "+str('%.4f'%ball_energy)+" J after collision.")

    #calculate the time it takes the ball to hit the ground y=4.9*t**2 -> t=sqrt(y/4.9)
    time= math.sqrt(DATA['tee_height']/4.9)
    #calculate ball velocity v=sqrt(2*K/m)
    ball_velocity = math.sqrt(2*ball_energy/ball)
    print('The ball takes '+str('%.4f'%time)+' s to hit the ground, and travels horizontally at '+str('%.4f'%ball_velocity)+' m/s.')
    #calculate distance traveled
    ball_dist = ball_velocity*time
    print('the ball will travel '+ str('%.4f'%ball_dist)+' m.')
    print('-------------------------------------------')
#main-----------------------------------------
#moved to menu program



