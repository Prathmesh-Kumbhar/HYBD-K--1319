RCB=["Virat Kohli","Phil Salt","Jitesh Sharma","Rajat Patidar","Devdutt Padikkal","Krunal Pandya",
     "Tim David", "Romario Shepherd","Josh Hazlewood","Suyash Sharma","Bhuvneshwar Kumar"]

PBKS=["Shreyas Iyer","Josh Inglis","Prabhsimran Singh","Nehal Wadhera","Shashank Singh","Marcus Stoinis",
      "Glenn Maxwell","Marco Jansen","Priyansh Arya","Arshdeep Singh","Yuzvendra Chahal"]

MI=["Rohit Sharma","Ryan Rickelton","Tilak Varma","Suryakumar Yadav","Hardik Pandya","Naman Dhir",
     "Will Jacks","Mitchell Santner","Trent Boult","Deepak Chahar","Jasprit Bumrah"]

GT=["Shubman Gill","Jos Buttler","Sherfane Rutherford","Washington Sundar","Sai Kishore","Sai Sudharsan",
    "Shahrukh Khan","Kagiso Rabada","Mohammed Siraj","Prasidh Krishna","Rashid Khan"]

DC=["KL Rahul","Abishek Porel","Tristan Stubbs","Jake Fraser-McGurk","Karun Nair","Faf du Plessis"
    "Ashutosh Sharma","Vipraj Nigam","Axar Patel","Mitchell Starc","Kuldeep Yadav"]

LSG=["Rishabh Pant","Nicholas Pooran","David Miller","Aiden Markram","Mitchell Marsh","Abdul Samad",
     "Shahbaz Ahamad","Ayush Badoni","Avesh Khan","Akash Deep","Ravi Bishnoi"]

RR=["Sanju Samson","Dhruv Jurel","Vaibhav Suryavanshi","Shimron Hetmyer","Yashasvi Jaiswal","Riyan Parag",
    "Nitish Rana","Jofra Archer","Maheesh Theekshana","Wanindu Hasaranga","Akash Madhwal"]

SRH=["Pat Cummins","Ishan Kishan","Heinrich Klaasen","Travis Head","Abhinav Manohar","Harshal Patel",
     "Abhishek Sharma","Nitish Kumar Reddy","Mohammad Shami","Rahul Chahar","Eshan Malinga"]

KKR=["Venkatesh Iyer","Quinton de Kock","Rahmanullah Gurbaz","Rinku Singh","Angkrish Raghuvanshi","Ajinkya Rahane",
     "Moeen Ali","Andre Russell","Anrich Nortje","Harshit Rana","Sunil Narine"]

CSK=["Ruturaj Gaikwad","MS Dhoni","Devon Conway","Rahul Tripathi","Rachin Ravindra","Ravichandran Ashwin",
    "Sam Curran","Ravindra Jadeja","Shivam Dube","Noor Ahmad","Khaleel Ahmed"]


# any letter find in the case for capital or small
for i in MI:
    if "R".lower() in i.lower():
        print(i)

# Searching on the first letter in the string 
for i in CSK:
    if i.startswith("R"):
        print(i)

# Search the letters in middle or any position
for i in CSK:
    if "r" in i:
        print(i)
