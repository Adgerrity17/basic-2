
# Determining the users fortune based upon their age, favorite number, and favorite color
#Data in: To preform this task, we need to get the users name, age, favorite number, and favorite color
#Output: users fortune
#See separate sheet for algorithm
#Other courses required for code to compile: None
# Credits: based upon the code provided in class and in the textbook
###############################################################################

#Program starts here
print("This program will determine your fortune based upon your age, favorite color, and favorite number")
name = input("What is your name? : ")
age_str = input("How old are you? : ")
age_int = int(age_str)
user_color = input("What is your favorite color? : ")
number_str = input("What is your favorite numer? : ")
number_int = int(number_str)
#The information gathered above is the demographic information required to output the user's forturne

Fortune_1 = "You will see someone you did not expect to see today"
Fortune_2 = "Your lucky numbers for today are 18, 47, 28, and 94"
Fortune_3 = "Today is a good day to wear blue"
Fortune_4 = "Avoid taking unnecessary gambles"
Fortune_5 = "Time heals all wounds, keep your head up"
Fortune_6 = "Do or do not... there is no try"
Fortune_7 = "You will find a bushel of money"
Fortune_8 = "Watch out for cloaked strangers laughing menacingly"
Fortune_9 = "The rap game got it all wrong, you should save your money"
#These are the 9 possible fortune outputs
if (age_int < 18):
    if user_color == 'green':
        print(name, "the fortune teller predicts", Fortune_1)
    if user_color == 'blue':
        print(name, "the fortune teller predicts", Fortune_2)
    elif user_color != 'blue':
        if user_color != 'green':
            if number_int < 50:
                print(name, "the fortune teller predicts", Fortune_3)
            if number_int >= 50:
                print(name, "the fortune teller predicts", Fortune_4)
if (age_int > 18):
    if user_color == 'orange':
        if number_int <= 5:
            print(name, "the fortune teller predicts", Fortune_5)
        if number_int > 5:
            print(name, "the fortune teller predicts", Fortune_6)
    elif user_color != 'organge':
        print(name, "the fortune teller predicts", Fortune_7)
if (age_int == 18):
    if number_int == 3:
        print(name, "the fortune teller predicts", Fortune_9)
    else:
        print(name, "the fortune teller predicts", Fortune_8)
#The fortune will display below using boolian expression

