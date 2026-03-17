import random

#Mental math program

#Play again game loop starts here
while True:    
    #Create a score variable first, outside loop
    score = 0
    
    #For loop to repeat question X5
    #The "(1,6)" asks questions 1 to 5
    for i in range(1, 6):
        
        #Generate two random numbers,  i.e 34, 6
        num1 = random.randint(10, 99)
        num2 = random.randint(1,99)
        
        #Randomise the operator/signs
        operator = random.choice(["+", "-"])
        
        #The following is to swap -ves into correct order, place this conditional b4 asking user input
        #Subtraction will be positive
        if operator == "-":
            if num1 < num2:
                num1,  num2 = num2,  num1
        
        #Prompt the user input
        #The try, except lines are to prevent code from crashing when user doesnt enter a #
        while True:
            
            try:
                answer = int(input(f"Question {i}: What is {num1} {operator} {num2}? "))
                
                break
                
            except ValueError:
                print("Please enter numbers!")
        
        #Alternate between add or subtract
        if operator == "+":
            correct = num1 + num2
    
        else:
            correct = num1 - num2
        
        #Check if conditional is correct and print message
        if answer == correct:
            print("Correct!")
            #The following means add plus 1 to score
            score += 1
        
        #Incorrect message and the correct answer
        else:
            print(f"Incorrect! The correct answer is: {correct}")
                    
    #Percentage of score, needs to be outside for loop to give feedback after the total score
    percentage = score / 5 * 100
              
    #Show score after loop finishes
    print(f"Final score: {score} / 5. That's a percentage of {percentage}%")
    
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