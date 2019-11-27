# Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range, print an error.
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

score = input("Enter Score: ")
fscore = float(score)
if fscore < 0.0 or fscore > 1.0:
    print("Error, score should be between 0.0 and 1.0")
    quit()
if fscore < 0.6:
    print("F")
elif fscore >= 0.6 and fscore < 0.7:
    print("D")
elif fscore >= 0.7 and fscore < 0.8:
    print("C")
elif fscore >= 0.8 and fscore < 0.9:
    print("B")
else:
    print("A")
