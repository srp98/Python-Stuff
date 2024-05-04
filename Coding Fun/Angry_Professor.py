"""
Program to determine to cancel the class or not based on the number of students attending the class within a certain
threshold of arrival time.
"""


def class_cancel(arr, thr):
    return 'YES' if len([i for i in arr < 1]) < thr else 'NO'


if __name__ == '__main__':
    t = int(input('Enter the number of test cases \n:'))
    for _ in range(t):
        n, k = list(map(int, input('Enter the number of students and cancellation threshold\n:').split()))
        a = list(map(int, input('Enter the arrival times of students\n:')))
        print(class_cancel(a, k))
