import random
import time #Adds timed Q's'

#Mental math program

#Play again game loop starts here
while True:
    
    difficulty = input("Choose difficulty (easy, medium, hard): ").lower()#lower() means Easy -> easy. so no uppercase errors 
    
    #This sets the game rules
    if difficulty == "easy":
        min1, max1 = 1, 20
        min2, max2 = 1, 20
        operators = ["+"]
        time_limit = 20
    
    elif difficulty == "medium":
        min1, max1 = 10, 99
        min2, max2 = 1,99
        operators = ["+", "-"]
        time_limit = 15
    
    elif difficulty == "hard":
        min1, max1 = 10, 200
        min2, max2 = 1, 100
        operators = ["+", "-", "*", "/"]
        time_limit = 10
        
    else:
        print("Invalid input! Defaulting to medium: ")
        min1,max1 = 10, 99
        min2, max2 = 1, 99
        operators = ["+", "-"]
        #Default time limit
        time_limit = 15
        
    #Display difficulty they chose, UX upgrade
    print(f"\nYou selected: {difficulty.capitalize()} mode\n")
    
    #Create a score variable first, outside loop
    score = 0
    
    #For loop to repeat question X5
    #The "(1,6)" asks questions 1 to 10
    for i in range(1, 11):
        
        #Randomise the operator/signs
        operator = random.choice(operators)
        
        #The following includes a division logic to ensure no decimals. 
        #Num 2 = 1 digit, num1 = up to 3 digits
        if operator == "/":
            num2 = random.randint(1, 9)
            correct = random.randint(2, 99)
            num1 = correct * num2
        
        #Add friendlier "×" logic here
        elif operator == "*":
            num1 = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 25, 50, 100])
            num2 = random.randint(2, 20)
            correct = num2 * num1
            
        else:
        #Generate two random numbers,i.e 34&6
        #Implement min, max as values
            num1 = random.randint(min1, max1)
            num2 = random.randint(min2, max2)
            
        #The following is to swap -ves into correct order, place this conditional b4 asking user input
        #Subtraction will be positive
        if operator == "-":
            if num1 < num2:
                num1,  num2 = num2,  num1
                
        #Start timer before input
        start_time = time.time()
        
        #Prompt the user input
        #The try, except lines are to prevent code from crashing when user doesnt enter a #
        while True:
            
            try:
                answer = int(input(f"Question {i}: What is {num1} {operator} {num2}? "))
                
                #End timer after valid input
                end_time = time.time()
                time_taken = end_time - start_time
                break
                
            except ValueError:
                print("Please enter numbers!")
                
        #Alternate between add or subtract
        if operator == "+":
            correct = num1 + num2
    
        elif operator == "*":
            pass #Already calculated
         
        elif operator == "/":
            pass 
            
        else:
            correct = num1 - num2
        
        #Check the time
        if time_taken > time_limit:
            print(f"Too slow! You took {time_taken:.2f} seconds")
            print(f"The correct answer is: {correct}")
        
        #Check if conditional is correct and print message
        elif answer == correct:
            print(f"Correct! ({time_taken:.2f} seconds)") 
            
            #The following means add plus 1 to score
            score += 1
              
        else:
            print(f"Incorrect! ({time_taken:.2f} seconds)")
            
            print(f"The correct answer is: {correct}")
                    
    #Percentage of score, needs to be outside for loop to give feedback after the total score
    percentage = score / 10 * 100
              
    #Show score after loop finishes
    print(f"Final score: {score} / 10. That's a percentage of {percentage}%")
    
    #Feedback on user score
    if percentage == 100:
        print("Your mental math is excellent!")
    
    elif percentage >= 60:
        print("Good mental math from you!")
         
    else:
        print("Oops! Try doing more mental math.")
        
    #Play again question
    while True:
        askToReplay = input("Want to play again. (yes or no)?: ").lower()
        
        if askToReplay == "no":
            print("Thanks for playing!")
            break
            
        elif askToReplay == "yes":
            break
            
        else:
            print("Enter only yes or no!")
                
    if askToReplay == "no":
        break #Exit game loop
        
#Date: 16/03. I will be adding the play again feature
#Date 17/03. Upload version 1.0 to Github
#Date 18/03. Added difficulty levels
#Date 19/03. Added ÷ w\o decimals
#And 10 sec time limit for Q's'
#Date 21/03. Make the code user friendly
