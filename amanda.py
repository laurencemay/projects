import time
import random

num = random.randint(0, 12)
times = 0
score = 0
keep_going = True

while keep_going:
    int_answer = -1
    while int_answer < 0:
        str_answer = input(str(num) + " x 9 ")
        try:
            int_answer = int(str_answer)
        except:
            print("please type a number")

    if int_answer == num * 9:
        print("correct")
        time.sleep(1)
        num = random.randint(0, 12)
        times += 1
        score += 1
    else:
        print("incorrect")
        time.sleep(1)
        num = random.randint(0, 12)
        times += 1
    if times == 10:
        print("The End")
        time.sleep(0.5)
        print("your score was " + str(score))
        keep_going = False

