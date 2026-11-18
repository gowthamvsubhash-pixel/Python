def score_input():
    y = int(input("Please input the first score: "))
    u = int(input("Please enter the second score: "))
    i = int(input("Please enter the third score: "))
    o = int(input("Please enter the fourth score: "))
    p = int(input("Please enter the fifth score: "))

    return [y, u, i, o, p]


def score_total(score):
    total = sum(score)
    print("Total score achieved:", total)

def score_average(score):
    total = 0

    for i in range(score):
        total = total + i

    average = total / len(score)

    print("Average score:", average)

marks = score_input()

score_total(marks)
score_average(marks)