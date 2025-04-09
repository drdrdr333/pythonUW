'''
1.
'''

user_name = input("What is your name? ")
conference_id = input("What is your conference ID?")
org_represented = input("What organization do you represent?")
email_address = input("What is your email address?")

food_preferences = []
while(True):
    food_pref = input("Please state one food preference if necessary: ")

    food_preferences.append(food_pref)

    choice = input("Do you have more? Type 'y' for yes, 'n' for no.")

    if(choice.lower() == 'y'):
        continue
    else:
        break

'''
2.
'''
sessions = ["Python for beginners", "Database development with Python", "Python for data science", "Advanced Python for application developers"]

for i in sessions:
    answer1 = input(f"Do you wish to attend {i} (Y or N)? ")

    if answer1.lower() == 'y':
        print(f"Ok, I've recorded your interest to attend {i}")
    elif answer1.lower() == 'n':
        print(f"Ok, I've recorded your disinterest to attend {i}")


'''
3. 4. 5.
'''

questions = ["What is your name? ", "What is your conference ID?", "What organization do you represent?", "What is your email address?", "State any food preferences?", "Do you wish to attend "]
answers = {}
sessions = ["Python for beginners?", "Database development with Python?", "Python for data science?", "Advanced Python for application developers?"]

for i in questions:
    if i[0:2] == "Do":
        for ii in sessions:
            answer1 = input(f"{i} {ii} ")
            answers[f"{i}{ii}"] = answer1
    else:
        answer = input(i)
        answers[i] = answer
