# Create a IPL Teams and perform a Dictionary Operations using for loop

MI = [
{"Jersey NO":45,"Name":"Rohit Sharma","Runs":7345,"Wickets":75,"Team_name":"Mumbai Indians"},
{"Jersey NO":63,"Name":"Suryakumar Yadav","Runs":3249,"Wickets":0,"Team_name":"Mumbai Indians"},
{"Jersey NO":77,"Name":"Tilak Varma","Runs":1200,"Wickets":0,"Team_name":"Mumbai Indians"},
{"Jersey NO":33,"Name":"Hardik Pandya","Runs":2309,"Wickets":53,"Team_name":"Mumbai Indians"},
{"Jersey NO":99,"Name":"Ishan Kishan","Runs":2644,"Wickets":0,"Team_name":"Mumbai Indians"},
{"Jersey NO":19,"Name":"Jasprit Bumrah","Runs":69,"Wickets":145,"Team_name":"Mumbai Indians"},
{"Jersey NO":24,"Name":"Tim David","Runs":659,"Wickets":0,"Team_name":"Mumbai Indians"},
{"Jersey NO":23,"Name":"Piyush Chawla","Runs":584,"Wickets":179,"Team_name":"Mumbai Indians"},
{"Jersey NO":70,"Name":"Gerald Coetzee","Runs":50,"Wickets":15,"Team_name":"Mumbai Indians"},
{"Jersey NO":18,"Name":"Shreyas Gopal","Runs":180,"Wickets":49,"Team_name":"Mumbai Indians"}
]


CSK = [
{"Jersey NO":7,"Name":"MS Dhoni","Runs":5082,"Wickets":0,"Team_name":"Chennai Super Kings"},
{"Jersey NO":8,"Name":"Ravindra Jadeja","Runs":2692,"Wickets":152,"Team_name":"Chennai Super Kings"},
{"Jersey NO":25,"Name":"Ruturaj Gaikwad","Runs":2380,"Wickets":0,"Team_name":"Chennai Super Kings"},
{"Jersey NO":31,"Name":"Shivam Dube","Runs":1100,"Wickets":4,"Team_name":"Chennai Super Kings"},
{"Jersey NO":90,"Name":"Deepak Chahar","Runs":80,"Wickets":72,"Team_name":"Chennai Super Kings"},
{"Jersey NO":54,"Name":"Devon Conway","Runs":924,"Wickets":0,"Team_name":"Chennai Super Kings"},
{"Jersey NO":88,"Name":"Moeen Ali","Runs":1034,"Wickets":35,"Team_name":"Chennai Super Kings"},
{"Jersey NO":47,"Name":"Matheesha Pathirana","Runs":10,"Wickets":34,"Team_name":"Chennai Super Kings"},
{"Jersey NO":17,"Name":"Ajinkya Rahane","Runs":4642,"Wickets":1,"Team_name":"Chennai Super Kings"},
{"Jersey NO":21,"Name":"Tushar Deshpande","Runs":21,"Wickets":42,"Team_name":"Chennai Super Kings"}
]


RCB = [
{"Jersey NO":18,"Name":"Virat Kohli","Runs":8004,"Wickets":4,"Team_name":"Royal Challengers Bangalore"},
{"Jersey NO":97,"Name":"Faf du Plessis","Runs":4571,"Wickets":0,"Team_name":"Royal Challengers Bangalore"},
{"Jersey NO":32,"Name":"Glenn Maxwell","Runs":2719,"Wickets":35,"Team_name":"Royal Challengers Bangalore"},
{"Jersey NO":21,"Name":"Rajat Patidar","Runs":799,"Wickets":0,"Team_name":"Royal Challengers Bangalore"},
{"Jersey NO":19,"Name":"Mohammed Siraj","Runs":56,"Wickets":78,"Team_name":"Royal Challengers Bangalore"},
{"Jersey NO":7,"Name":"Dinesh Karthik","Runs":4516,"Wickets":0,"Team_name":"Royal Challengers Bangalore"},
{"Jersey NO":9,"Name":"Josh Hazlewood","Runs":30,"Wickets":52,"Team_name":"Royal Challengers Bangalore"},
{"Jersey NO":5,"Name":"Mahipal Lomror","Runs":350,"Wickets":2,"Team_name":"Royal Challengers Bangalore"},
{"Jersey NO":13,"Name":"Will Jacks","Runs":230,"Wickets":5,"Team_name":"Royal Challengers Bangalore"},
{"Jersey NO":24,"Name":"Reece Topley","Runs":15,"Wickets":12,"Team_name":"Royal Challengers Bangalore"}
]


KKR = [
{"Jersey NO":12,"Name":"Shreyas Iyer","Runs":3127,"Wickets":0,"Team_name":"Kolkata Knight Riders"},
{"Jersey NO":74,"Name":"Andre Russell","Runs":2262,"Wickets":96,"Team_name":"Kolkata Knight Riders"},
{"Jersey NO":66,"Name":"Sunil Narine","Runs":1046,"Wickets":163,"Team_name":"Kolkata Knight Riders"},
{"Jersey NO":35,"Name":"Rinku Singh","Runs":893,"Wickets":0,"Team_name":"Kolkata Knight Riders"},
{"Jersey NO":25,"Name":"Nitish Rana","Runs":2636,"Wickets":8,"Team_name":"Kolkata Knight Riders"},
{"Jersey NO":19,"Name":"Varun Chakravarthy","Runs":10,"Wickets":62,"Team_name":"Kolkata Knight Riders"},
{"Jersey NO":17,"Name":"Venkatesh Iyer","Runs":1325,"Wickets":3,"Team_name":"Kolkata Knight Riders"},
{"Jersey NO":11,"Name":"Mitchell Starc","Runs":100,"Wickets":65,"Team_name":"Kolkata Knight Riders"},
{"Jersey NO":3,"Name":"Rahmanullah Gurbaz","Runs":350,"Wickets":0,"Team_name":"Kolkata Knight Riders"},
{"Jersey NO":20,"Name":"Harshit Rana","Runs":5,"Wickets":18,"Team_name":"Kolkata Knight Riders"}
]

IPL_T20_DB={"MI":MI,"CSK":CSK,"RCB":RCB,"KKR":KKR}

# Find the Player Name Which Score 5000+ runs

for team in IPL_T20_DB:
    players=IPL_T20_DB[team]
    
    for player in players:
        if player["Runs"]>=5000:
            print(player["Name"],"-",player["Runs"])

''' 
Output:

Rohit Sharma - 7345
MS Dhoni - 5082
Virat Kohli - 8004

'''

# Find the player name which have a 25+ Wickets

for team in IPL_T20_DB:
    players=IPL_T20_DB[team]
    
    for player in players:
        if player["Wickets"]>=25:
            print(player["Name"],"-",player["Wickets"])

'''
Output :

Rohit Sharma - 75
Hardik Pandya - 53
Jasprit Bumrah - 145
Piyush Chawla - 179
Shreyas Gopal - 49
Ravindra Jadeja - 152
Deepak Chahar - 72
Moeen Ali - 35
Matheesha Pathirana - 34
Tushar Deshpande - 42
Glenn Maxwell - 35
Mohammed Siraj - 78
Josh Hazlewood - 52
Andre Russell - 96
Sunil Narine - 163
Varun Chakravarthy - 62
Mitchell Starc - 65
'''

# Find those players which have a 2000+ runs And also 20+ wickets

for team in IPL_T20_DB:
    players=IPL_T20_DB[team]
    
    for player in players:
        if player["Runs"]>=2000 and player["Wickets"]>=20:
            print(player["Name"],"-",player["Runs"],"---","Wickets: ",player["Wickets"])

'''
Output :

Rohit Sharma - 7345 --- Wickets:  75
Hardik Pandya - 2309 --- Wickets:  53
Ravindra Jadeja - 2692 --- Wickets:  152
Glenn Maxwell - 2719 --- Wickets:  35
Andre Russell - 2262 --- Wickets:  96
'''

# Find the player name which have less than 1000 runs and less than 20 wickets

for team in IPL_T20_DB:
    players=IPL_T20_DB[team]
    
    for player in players:
        if player["Runs"]<=1000 and player["Wickets"]<=20:
            print(player["Name"],"-",player["Runs"],"---","Wickets: ",player["Wickets"])

'''
Output :

Tim David - 659 --- Wickets:  0
Gerald Coetzee - 50 --- Wickets:  15
Devon Conway - 924 --- Wickets:  0
Rajat Patidar - 799 --- Wickets:  0
Mahipal Lomror - 350 --- Wickets:  2
Will Jacks - 230 --- Wickets:  5
Reece Topley - 15 --- Wickets:  12
Rinku Singh - 893 --- Wickets:  0
Rahmanullah Gurbaz - 350 --- Wickets:  0
Harshit Rana - 5 --- Wickets:  18

'''
# Find those player which have 0 wickets but it can score 1000+ scores with his team name 


for team in IPL_T20_DB:
    players=IPL_T20_DB[team]
    
    for player in players:
        if player["Runs"]>=1000 and player["Wickets"]==0:
            print(player["Name"],"-",player["Runs"],"---","Wickets: ",player["Wickets"],"\t\t",player["Team_name"])


'''
Output :

Suryakumar Yadav - 3249 --- Wickets:  0          Mumbai Indians
Tilak Varma - 1200 --- Wickets:  0               Mumbai Indians
Ishan Kishan - 2644 --- Wickets:  0              Mumbai Indians
MS Dhoni - 5082 --- Wickets:  0                  Chennai Super Kings
Ruturaj Gaikwad - 2380 --- Wickets:  0           Chennai Super Kings
Faf du Plessis - 4571 --- Wickets:  0            Royal Challengers Bangalore
Dinesh Karthik - 4516 --- Wickets:  0            Royal Challengers Bangalore
Shreyas Iyer - 3127 --- Wickets:  0              Kolkata Knight Riders

'''

# Find High Wicket Taker and his wickets

max_wicket=0
Player="" 

for team,players in IPL_T20_DB.items():
    for player in players:
        if player["Wickets"]> max_wicket:
            max_wicket=player["Wickets"]
            Player=player["Name"]

print("Highest Wickets : ",max_wicket)
print("Highest Wicket Taker is : ",Player)

'''
Output :

Highest Wickets :  179
Highest Wicket Taker is :  Piyush Chawla

'''


# Find the Highest Runs and the player Name

max_Runs=0
Player="" 

for team,players in IPL_T20_DB.items():
    for player in players:
        if player["Runs"]> max_Runs:
            max_Runs=player["Runs"]
            Player=player["Name"]

print("Highest Runs are : ",max_Runs)
print("Highest Runs made by : ",Player)

'''
Highest Runs are :  8004
Highest Runs made by :  Virat Kohli
'''


