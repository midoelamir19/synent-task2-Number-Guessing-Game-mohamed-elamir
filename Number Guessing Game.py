import random


def Number_Guessing_Game ():
    random_num=random.randint(1, 100)
    count=0
    while True :
        num=float(input("Enter your Guess : "))
        if abs(random_num-num)<=5 :
            print("Difference too low")
        else:
            print("Difference too high")
        count+=1
        if random_num==num:
            break

    print("Congratulations!you reach right number after ",count," attempts")

Number_Guessing_Game()