#Ame Shajd
#1/26/24
#You will make an autograded quiz. The quiz will ask 5 questions to the user and provide a total score at the end.


#multiplechoice function that basically adds a point to your score if its right
def multipleChoice(input, correct_answer):
    score = 0
    if input == correct_answer:
        score += 1
    return score
#trueFalse function that basically adds a point to your score if its right
def trueFalse(input, correct_answer):
    score = 0
    if input == correct_answer:
        score += 1
    return score
#numericalEntry function that basically adds a point to your score if its right
def numericalEntry(input, correct_answer):
    score = 0
    if input == correct_answer:
        score += 1
    return score
#fillIN function that basically adds a point to your score if its right
def fillIn(input, correct_answer):
    score = 0
    if input == correct_answer:
        score += 1
    return score
#freeWill function that basically adds a point to your score if its right
def freeWill(input,input1, correct_answer, correct_answer1):
    score = 0
    if input == correct_answer and input1 == correct_answer1:
        score += 1

    return score

#over here it uses this as the first and main funciton, everything inside will be executed first
if __name__ == "__main__": 
    
    questions = 5
    score = 0
    
    #introduction
    print("Welcome to Quiz Grader\n")
    #this is my question 1 and towards the end they have user input with the correct answer and then it adds a score plus 1
    print("Question 1")
    print("How many terms does drexel have?")
    print("a. 1")
    print("b. 2")
    print("c. 3")
    print("d. 4") 
    user_answer = input("Enter your answer: ") 
    correct_answer = "c"
    score += multipleChoice(user_answer, correct_answer)
    print()
    
       #this is my question 2 and towards the end they have user input with the correct answer and then it adds a score plus 1
 
    print("Question 2")
    print("Is the following statement true or false?")
    print("Is 5 > 8")
    user_answer = input("Is this true or false: ")
    correct_answer = "false"
    score += trueFalse(user_answer, correct_answer)
    print()
    #this is my question 3 and towards the end they have user input with the correct answer and then it adds a score plus 1

    print("Question 3")
    print("How many days are in a week?")
    user_answer = int(input("Enter a number as the answer: "))
    correct_answer = 7
    score += numericalEntry(user_answer, correct_answer)
    print()
    #this is my question 4 and towards the end they have user input with the correct answer and then it adds a score plus 1

    print("Question 4")
    print("Roses are red, _______ are blue")
    user_answer = input("Enter an answer to fill in the blank: ")
    correct_answer = "violets"
    score += fillIn(user_answer, correct_answer)
    print()
    #this is my question 5 and towards the end they have user input with the correct answer and then it adds a score plus 1

    print("Question 5")
    print("What are the two solutions to (Sqrt16)")
    user_answer = int(input("Enter first root: "))
    user_answer1 = int(input("Enter second root: ")) 
    correct_answer = 4
    correct_answer1 = -4
    score += freeWill(user_answer, user_answer1, correct_answer, correct_answer1)
    print()
    print(f'You got a {score} out of 5 correct')
    print(f'You score is {(score/questions)* 100:.2f}%')



    



    

















