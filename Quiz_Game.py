print("Welcome to Funny Quiz Game 😂")
score = 0

# Question 1
print("\n1. What has teeth but cannot bite?")
print("a) Dog")
print("b) Comb")
print("c) Human")
ans1 = input("Enter your answer (a/b/c): ")

if ans1 == "b":
    print("Correct 😂")
    score += 1
else:
    print("Wrong ❌  Correct answer is Comb")

# Question 2
print("\n2. What runs but never walks?")
print("a) River")
print("b) Man")
print("c) Dog")
ans2 = input("Enter your answer (a/b/c): ")

if ans2 == "a":
    print("Correct 😄")
    score += 1
else:
    print("Wrong ❌  Correct answer is River")

# Question 3
print("\n3. Which room has no doors or windows?")
print("a) Bedroom")
print("b) Bathroom")
print("c) Mushroom")
ans3 = input("Enter your answer (a/b/c): ")

if ans3 == "c":
    print("Correct 🤣")
    score += 1
else:
    print("Wrong ❌  Correct answer is Mushroom")

# Question 4
print("\n4. What has hands but cannot clap?")
print("a) Human")
print("b) Clock")
print("c) Monkey")
ans4 = input("Enter your answer (a/b/c): ")

if ans4 == "b":
    print("Correct 😆")
    score += 1
else:
    print("Wrong ❌  Correct answer is Clock")

# Question 5
print("\n5. If you drop a yellow hat in the Red Sea, what does it become?")
print("a) Red")
print("b) Blue")
print("c) Wet")
ans5 = input("Enter your answer (a/b/c): ")

if ans5 == "c":
    print("Correct 🤪")
    score += 1
else:
    print("Wrong ❌  Correct answer is Wet")

print("\n🎉 Quiz Finished!")
print("Your Score:", score, "/ 5")