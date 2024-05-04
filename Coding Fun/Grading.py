"""
Given a grading function which rounds the score to next multiple:
- Difference between the grade and next multiple of 5 is less than 3, round grade upto to next multiple of 5
- If value of score is less than 38, no rounding occurs

Eg: Score = 84, will be rounded to 85 but score 29 will not be rounded
"""


def grade(arr):
    """
    Grading functions which rounds the score to next multiplier if:
    - Difference between the grade and next multiple of 5 is less than 3, round grade upto to next multiple of 5
    - If value of score is less than 38, no rounding occurs
    :param arr: An Array of scores
    :return: Rounded scores
    """
    return [print((arr[j] + (5-(arr[j] % 5))))
            if ((arr[j] % 5) > 2) and (arr[j] >= 38)
            else print(arr[j])
            for j in range(len(arr))]


if __name__ == '__main__':
    n = int(input('Enter the number of students in range [1, 60]:'))
    score = [int(input()) for _ in range(n)]
    grade(score)
