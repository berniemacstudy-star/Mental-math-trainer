import random
import time #Adds timed Q's'

print("=== MENTAL MATH GAME v1.0 ===\n")

#Play again game loop starts here
while True:
    
    while True:
        base_difficulty = input("Choose difficulty (easy, medium, hard): ").lower()#lower() means Easy -> easy. so no uppercase errors
        
        #Ensures user only enters valid input
        if base_difficulty in ["easy", "medium", "hard"]:
            break
            
        else:
            print("Invalid input! Enter only easy, medium or hard.")
    
    #Track current dfficulty chosen
    current_difficulty = base_difficulty
        
    #Display difficulty they chose, UX upgrade
    print(f"\nYou selected: {base_difficulty.capitalize()} mode\n")
    
    #Create a score variable first, outside loop
    score = 0
    
    #Max possible score per mode chosen
    max_possible_score = 0
    
    #Create a streak/maxstreak variable
    streak = 0
    max_streak = 0
    
    #Initialize difficulty so that code runs smoothly, its a string variable
    previous_difficulty = None
    
    #For loop to repeat question X10
    #The "(1,11)" asks questions 1 to 10
    for i in range(1, 11):
                
        #Adapt difficulty dynamically, based on streak and base difficulty. Decide difficulty

        if base_difficulty == "easy":
            if streak >= 6:
                current_difficulty = "hard"
    
            elif streak >= 3:
                current_difficulty = "medium"
        
            else:
                current_difficulty = "easy"

        elif base_difficulty == "medium":
            if streak >= 6:
                current_difficulty = "hard"
            
            else:
                current_difficulty ="medium"

        elif base_difficulty == "hard":
            current_difficulty = "hard"    
                  
        #Track max possible points for this question
        if current_difficulty == "easy":
            max_possible_score += 2
            
        elif current_difficulty == "medium":
            max_possible_score += 3
            
        elif current_difficulty == "hard":
            max_possible_score += 5
            
        #Time limit based on difficulty
        #This sets the game rules
        if current_difficulty == "easy":
            time_limit = 20
            min1, max1 = 1, 20
            min2, max2 = 1, 20
            operators = ["+", "-"]
    
        elif current_difficulty == "medium":
            time_limit = 15
            min1, max1 = 10, 99
            min2, max2 = 1, 99
            operators = ["+", "-"]
    
        elif current_difficulty == "hard":
            time_limit = 10
            min1, max1 = 10, 200
            min2, max2 = 1, 100
            operators = ["+", "-", "*", "/"]
            
        #Show difficulty only if it changed
        #Give difficulty feedback b4 question
        if current_difficulty != previous_difficulty:
            print(f"[Difficulty: {current_difficulty.upper()}]")
            previous_difficulty = current_difficulty
        
        #Randomise the operator/signs
        #Generate question
        operator = random.choice(operators)
        
        #The following includes a division logic to ensure no decimals. 
        #Num 2 = 1 digit, num1 = up to 2 digits
        if operator == "/":
            num2 = random.randint(1, 9)
            correct = random.randint(2, 99)
            num1 = correct * num2
        
        #Add friendlier "×" logic here
        elif operator == "*":
            num1 = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 25, 50, 100])
            num2 = random.randint(2, 20)
            correct = num1 * num2
            
        else:
        #Generate two random numbers,i.e 34&6
        #Implement min, max as values
            num1 = random.randint(min1, max1)
            num2 = random.randint(min2, max2)
            
            #The following is to swap -ves into correct order, place this conditional b4 asking user input
            #Subtraction will be positive
            if operator == "-" and num1 < num2:
                num1,  num2 = num2,  num1

            if operator == "+":
                correct = num1 + num2
                
            else:
                correct = num1 - num2
                      
        #Ask question with timer
        start_time = time.time()
        
        #Prompt the user input
        #The try, except lines are to prevent code from crashing when user doesnt enter a #
        while True:
            try:
                answer = int(input(f"Question {i}: What is {num1} {operator} {num2}? "))
                break
                
            except ValueError:
                print("Please enter numbers!")
                
        #Time taken formula
        time_taken = time.time() - start_time
        
        #Check the answer
        if time_taken > time_limit:
            
            print(f"Too slow! You took {time_taken:.2f} seconds")
            print(f"The correct answer is: {correct}")
            
            #Reset when user answer is too slow
            streak = 0
            
            print("Streak resets :(")
        
        #Check if conditional is correct and print message
        elif answer == correct:
            print(f"Correct! ({time_taken:.2f} seconds)") 
            
            #Speed based logic. Rewards quicker, correct, answers then more points earned in hard mode 
            if current_difficulty == "easy":
                if time_taken < 5:
                    points = 2
                else:
                    points = 1
            
            elif current_difficulty == "medium":
                if time_taken < 5:
                    points = 3
                else:
                    points = 2
                    
            elif current_difficulty == "hard":
                if time_taken < 5:
                    points = 5
                else:
                    points = 3
                    
            score += points
            print(f"+{points} points!")
            
            streak += 1
            
            #Streak will track correct answers
            
            if streak > max_streak:
                max_streak = streak
            
            #This line prints after every user input
            print(f"Current streak: {streak}")
            
        else:
            print(f"Incorrect! ({time_taken:.2f} seconds)")
            
            print(f"Correct answer: {correct}")
            
            #Reset streak to zero for wrong answer
            streak = 0
            print("Streak resets :(")
            
        #Add spacing between questions
        print("-" * 30)#Means _ repeats 30 times
                    
    #Percentage of score, needs to align with the max possible points
    percentage = (score / max_possible_score) * 100 if max_possible_score > 0 else 0
              
    #Spacing for neatness
    print("\n===== RESULTS =====")
    
    #Show final score after loop finishes
    print(f"Score: {score} points")
    
    #Percentage
    print(f"Percentage: ({percentage:.1f})%")
    
    #Show best streak after final score
    print(f"Best streak: {max_streak}")   
    
    #More spacing
    print("====================")
    #Feedback on user score
    if percentage >= 90:
        print("Your mental math is excellent. Outstanding job!")
    
    elif percentage >= 70:
        print("Great mental math from you!")
         
    elif percentage >= 50:
        print("Good attempt. You're getting there!")
    else:
        print("Keep practicing. You'll improve!")
        
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
#Date 24/03. Add streak for enjoyability
#Date 25/03. Make game respond to user
#Date 26/03. Revamp for loop to fix logic
#Date 27/03 to 29/03. First concluding session
#Date 30/03. Reward speedy results + more points per difficulty
#Date 01/04.Version 1.0 Complete
