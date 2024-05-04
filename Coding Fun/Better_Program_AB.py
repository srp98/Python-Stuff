import random

# User Input Section
# print("Input the 3 scores of a ranging between 1 and 100: ")
# a = list(map(int, input().rstrip().rsplit()))
# print("Input the 3 scores of b, ranging between 1 and 100: ")
# b = list(map(int, input().rstrip().rsplit()))

# Random Section
a = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]
b = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]


# Triplet Function
def triplet(x, y):
    """
    Functions checks each member of x and y and compares them, the greater one gets score added to respective score
    functions
    :param x: Array of 3 values ranging between 1-100
    :param y: Array of 3 values ranging between 1-100
    :return: Score of x and score of y
    """
    score_x, score_y = 0, 0
    for i in range(len(x)):
        if x[i] > y[i]:
            score_x += 1

        if x[i] == y[i]:
            score_x += 1
            score_y += 1

        else:
            score_y += 1

    return [score_x, score_y]


result = triplet(a, b)
print(result)
print(' '.join(map(str, result)))
print(f"The Scores of a: {a} and Scores of b: {b} then the,\n "
      f"Triplet Function between a, b gives: {triplet(a, b)}")
