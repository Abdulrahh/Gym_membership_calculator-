import sys
while True:
    first_name = input("Enter your first name: ").strip().capitalize()
    if first_name == "":
        print("name must not be empty")
        continue 
    elif first_name.isalpha():
        break 
    else:
        print("invalid name")

while True:
    last_name = input("Enter your last name: ").strip().capitalize()
    if last_name == "":
        print("name must not be empty")
        continue 
    elif last_name.isalpha():
        break 
    else:
        print("invalid name")
        
while True:
    membership_ID = input("Enter your Gym membership ID: ").upper()
    if (len(membership_ID) != 6 or membership_ID[4] != "-" or membership_ID[5] != "M" or not membership_ID[:4].isalnum()):
        print("Invalid membership ID")
        continue 
    else:
        print(f"Welcome {first_name} {last_name} ")
        break 


def get_age():
    while True:
        try:
            age = int(input("Enter Your age: "))
            return age 
        except(ValueError):
            print("Invalid input")

age = get_age()
if age < 16 or age > 90:
    print("You are too old or too young to acess the gym membership")
    sys.exit() 
else:
    print("Your age is qualified to acess the gym membership")
    print()


tier = {"Bronze tier": 25,
        "Silver tier": 40,
        "Gold tier": 60}

print("*********Avalable gym subricption plan*************")
for x, y  in tier.items():
    print(f"{x}, £{y} per month")


while True: 
    selection = input("Enter gym subcription plan from the available choices: ").capitalize()
    if selection in tier:
        subtotal = tier[selection]
        break
    else:
        print("Invalid Subcription")

while True:
    student_discount = input("Are you a student (Y or N): ").capitalize()
    if student_discount == "Y":
        discount = 0.2 * subtotal
        total = subtotal - discount 
        break
    elif student_discount == "N":
        discount = 0
        total = subtotal - discount
        break 
    else:
        print("invalid input")
        


print("******Outpput Summary*********")
print(F"Name: {first_name} {last_name}")
print(f"ID: {membership_ID}")
print(f"Your selected membership is {selection} ")

print(F"Student discount: {discount}, total montly cost {total}")




