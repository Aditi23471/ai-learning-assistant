
print("================================")
print("      AI LEARNING ASSISTANT")
print("================================")

print("Welcome to your learning space!")

print("\nChoose a topic:")
print("1. Python")
print("2. Artificial Intelligence")
print("3. Mathematics")

topic = input("\nEnter your choice (1-3): ")

if topic == "1":
    print("\nPython is a programming language.")
    print("It is used to build websites, apps and software.")

elif topic == "2":
    print("\nArtificial Intelligence allows computers")
    print("to perform tasks that usually require human intelligence.")

    print("\nMINI QUIZ - 5 QUESTIONS")
    score = 0

    answer = input("\n1. What does AI stand for? ")
    if answer.strip().lower() == "artificial intelligence":
        print("Correct!")
        score += 1
    else:
        print("Correct answer: Artificial Intelligence")

    answer = input("\n2. What is a branch of AI that learns from data? ")
    if answer.strip().lower() == "machine learning":
        print("Correct!")
        score += 1
    else:
        print("Correct answer: Machine Learning")

    answer = input("\n3. Which programming language are we using? ")
    if answer.strip().lower() == "python":
        print("Correct!")
        score += 1
    else:
        print("Correct answer: Python")

    answer = input("\n4. Which Python function takes user input? ")
    if answer.strip().lower() == "input":
        print("Correct!")
        score += 1
    else:
        print("Correct answer: input")

    answer = input("\n5. What subject helps us understand numbers and patterns? ")
    if answer.strip().lower() == "mathematics":
        print("Correct!")
        score += 1
    else:
        print("Correct answer: Mathematics")

    print("\nQUIZ COMPLETED!")
    print("Your final score:", score, "/ 5")
    print("Question: What is Machine Learning?")
    answer = input("Your answer: ")

    score = 0
    if answer.strip().lower() == "machine learning":
        print("Excellent! You got it right!")
        score = score + 1
    else:
        print("Good try! The correct answer is Machine Learning.")
        print("\nYOUR FINAL SCORE")
        print("Score:", score, "/ 5")
        percentage = (score / 5) * 100
print("Your percentage:", percentage, "%")
elif topic == "3":
    print("\nMathematics helps us understand numbers,")
    print("patterns and logical relationships.")

else:
    print("\nPlease select a valid topic.")
