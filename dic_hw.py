# Create dict of 2025 movies
movies_db={}

cast_Chava=["Vicky Kaushal","Rashmika Mandanna","Akshaye Khanna","Vineet Kumar Singh"]
movies_db["Chava"]= cast_Chava

cast_Dhurandhar=["Ranveer Singh","Sanjay Dutt ","Akshaye Khanna","Arjun Rampal "]
movies_db["Dhurandhar"]=cast_Dhurandhar


cast_War2=["Hrithik Roshan","Kiara Advani","Anil Kapoor","Ashutosh Rana"]
movies_db["War 2"]=cast_War2

cast_Kantara_part1=["Rishab Shetty","Gulshan Devaiah","Rukmini Vasanth","Jayaram"]
movies_db["Kantara part1"]=cast_Kantara_part1

# 1. Get() Method

print(movies_db.get("Chava"))
print(movies_db.get("Dhurandhar"))
print(movies_db.get("War 2"))
print(movies_db.get("Kantara part1"))


# 2. Keys() Method

print(movies_db.keys())


# 3. Values() Method

print(movies_db.values())

# 4. Items() Method
# Way 1 => directly in print statment

print(movies_db.items())

# Way 2 => using for loop

for i in movies_db.items():
    print(i)

# If you want only keys using items method

for i,j in movies_db.items():
    print(i)

# If you want only values using items method

for i,j in movies_db.items():
    print(j)

# Count of the Akshya Khanna present in movies

count=0
for i in movies_db.values():
    for j in i:
        if j=="Akshaye Khanna":
            count=count+1    
print(count)       



