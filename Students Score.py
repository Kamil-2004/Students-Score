logo = """

  ____  _____  __ __  ____  ____  __  _  _____  ____  ____  ____ _____  ____ 
 (_ (_`|_   _||  |  || _) \| ===||  \| ||_   _|(_ (_`/ (__`/ () \| () )| ===|
.__)__)  |_|   \___/ |____/|____||_|\__|  |_| .__)__)\____)\____/|_|\_\|____|

"""
print(logo)


# Tell the highest scored student

student_scores = input("Enter your list of scores: \n").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    # replace a str value with an int one

highest_score = student_scores[0]

for score in student_scores:
    # if7
    if score > highest_score:
        highest_score = score
print(f"The highest score is : {highest_score}")

Score = highest_score 


