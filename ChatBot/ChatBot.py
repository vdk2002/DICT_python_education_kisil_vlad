bot_name = "Stepashka"
Birth_year = "2021"
print("Hello! My name is" + " " + bot_name)
print("I was created in" + " "+Birth_year)

print("Please,remind me your name.")
your_name = str(input())
print("What a great name you have," + your_name+"!")

print("Let me guess your age.")
print("Enter revainders of dividing your age dy 3, 5 and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is" + str(age)+"; that's a good time to start programming!")

print("Now I will prove to you that I can count to any number you want.")
your_num = int(input())
for i in range(your_num):
    print(i, end="!\n")
print("Completed, have a nice day!")

print("Let's test your programming knowledge.")
print("""
How many bytes ate there in a kilobyte?
1. 256
2.1024
3.128
4.825
""")


def answers(new_answer):
     answer = int(input())
     if answer == 2:
        print("Congratulations, have a nice day!")
     else:
        print("Please, try again.")
        answers("1")
answers("2")