print("Welcome to computer Quiz ! ")

playing = input("Do You Wanna Play ? ").lower().strip()
score=0

if playing !="yes":
    quit()


print("okay ! Lets Play ")

answer1 = input("What does CPU Stands For = ").lower().strip()
if answer1 == 'central processing unit':
    score+=1
    print(" Correct ")
else:
    print(" Incorrect ")


answer2 = input("What does RAM Stands For = ").lower().strip()
if answer2 == "random access memory":
    print(" Correct ")
    score+=1
else:
    print(" Incorrect ")

answer3 = input("What does WWW Stands For = ").lower().strip()
if answer3 == "world wide web":
    print(" Correct ")
    score+=1
else:
    print(" Incorrect ")


answer4 = input("What does HTML Stands For = ").lower().strip()
if answer4 == "hyper text markup language":
    print(" Correct ")
    score+=1
else:
    print(" Incorrect ")

print("You got ",score," Question correct ! ")
# print("You got "+str(score)+" Question correct ! ")

print("You got ",(score/4)*100,"  % ")
