'''
Task 1 : create 5 classes of your choice and write minimum 2 attributes and 1 method in each class
            1. fruits 2. car 3. bike 4. laptop 5.Table

'''
# 1.  For Fruit Class

class fruit:
    def __init__(self,name,color):
        self.name=name
        self.color=color
        

    def display(self):
        print(f"Fruit name is  {self.name} its color is {self.color}.")
    

f1=fruit("Mango","Yellow")
f2=fruit("Apple","Red")
f1.display()
f2.display()

'''
Output :

Fruit name is  Mango ,its color is Yellow .
Fruit name is  Apple ,its color is Red .
'''

# 2. For class Car

class car:
    def __init__(self,Brand,mileage):
        self.Brand=Brand
        self.mileage=mileage

    def car_info(self):
        print(f"The car brand is {self.Brand} and it gives mileage of {self.mileage} km/l")

c1=car("BMW",60)
c2=car("Maruti Suzuki Swift",24)

c1.car_info()
c2.car_info()
         

'''
Output :

The car brand is BMW and it gives mileage of 60 km/l
The car brand is Maruti Suzuki Swift and it gives mileage of 24 km/l
'''

# 3. For class Bike

class bike:
    def __init__(self,name,speed):
        self.name=name
        self.speed=speed

    def bike_info(self):
        print(f"The name of the Bike is {self.name} and its high speed is {self.speed} km/h")

b1=bike("Kawasaki Ninja H2R",400)
b2=bike("Royal Enfield Continental GT 650",170)

b1.bike_info()
b2.bike_info()

'''
Output :

The name of the Bike is Kawasaki Ninja H2R and its high speed is 400 km/h
The name of the Bike is Royal Enfield Continental GT 650 and its high speed is 170 km/h

'''

# 4. For class Laptop

class laptop:
    def __init__(self,brand,ram):
        self.brand=brand
        self.ram=ram

    def laptop_info(self):
        print(f"The brand of the laptop is {self.brand} and its Ram is {self.ram} GB")
         
l1=laptop("Lenovo",8)
l2=laptop("HP",16)

l1.laptop_info()
l2.laptop_info()

'''
Output :

The brand of the laptop is Lenovo and its Ram is 8 GB
The brand of the laptop is HP and its Ram is 16 GB

'''


# 5. For class Table

class Table:
    def __init__(self,material,shape):
        self.material=material
        self.shape=shape

    def table_info(self):
        print(f"The material of table is {self.material} and its shape is {self.shape}.")

t1=Table("Glass","Round")
t2=Table("Wood","Rectangle")

t1.table_info()
t2.table_info()
         
'''
Output :

The material of table is Glass and its shape is Round.
The material of table is Wood and its shape is Rectangle.

'''
# Create a 2026 IPL players list of 5 Teams

class Player:
    def __init__(self,jersey_number, player_name,runs,team_name,wickets):

        self.jersey_number=jersey_number
        self.player_name=player_name
        self.runs=runs
        self.team_name=team_name
        self.wickets=wickets

    def display(self):
        print("Player Name : ",self.player_name)
        print("Team Name : ",self.team_name)

p1=Player(45, "Rohit Sharma", 7878, "MI", 23)
p2=Player(63, "Ryan Rickelton", 2500, "MI", 0)
p3=Player(77, "Suryakumar Yadav", 3200, "MI", 0)
p4=Player(33, "Hardik Pandya", 4500, "MI", 100)
p5=Player(9, "Tilak Varma", 1200, "MI", 0)
p6=Player(99, "Sherfane Rutherford", 1500, "MI", 0)
p7=Player(93, "Jasprit Bumrah", 2321, "MI", 150)
p8=Player(11, "Mitchell Santner", 500, "MI", 180)
p9=Player(25, "Shardul Thakur", 200, "MI", 50)
p10=Player(55, "Trent Boult", 300, "MI", 40)
p11=Player(70, "AM Ghazanfar", 100, "MI", 30)

Mumbai_Indians=[]

Mumbai_Indians.append(p1)
Mumbai_Indians.append(p2)
Mumbai_Indians.append(p3)
Mumbai_Indians.append(p4)
Mumbai_Indians.append(p5)
Mumbai_Indians.append(p6)
Mumbai_Indians.append(p7)
Mumbai_Indians.append(p8)
Mumbai_Indians.append(p9)
Mumbai_Indians.append(p10)
Mumbai_Indians.append(p11)

for player in Mumbai_Indians:
    player.display()


'''
Output :

Player Name :  Rohit Sharma
Team Name :  MI
Player Name :  Ryan Rickelton
Team Name :  MI
Player Name :  Suryakumar Yadav
Team Name :  MI
Player Name :  Hardik Pandya
Team Name :  MI
Player Name :  Tilak Varma
Team Name :  MI
Player Name :  Sherfane Rutherford
Team Name :  MI
Player Name :  Jasprit Bumrah
Team Name :  MI
Player Name :  Mitchell Santner
Team Name :  MI
Player Name :  Shardul Thakur
Team Name :  MI
Player Name :  Trent Boult
Team Name :  MI
Player Name :  AM Ghazanfar
Team Name :  MI
'''



