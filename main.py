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
        print("\nMINI QUIZ")
    print("What is Machine Learning?")
    answer = input("Your answer: ")

    if answer.strip().lower() == "machine learning":
        print("Excellent! Correct answer!")
    else:
        print("Good try! The answer is Machine Learning.")
    print("\nMINI QUIZ")
    print("Question: What is Machine Learning?")
    answer = input("Your answer: ")

    if answer.strip().lower() == "machine learning":
        print("Excellent! You got it right!")
    else:
        print("Good try! The correct answer is Machine Learning.")

elif topic == "3":
    print("\nMathematics helps us understand numbers,")
    print("patterns and logical relationships.")

else:
    print("\nPlease select a valid topic.")
