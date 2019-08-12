# grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
# print("Grades:", grades)
#
#
# def print_grades(grades_input):
#     for i in grades:
#         print(i)
#
#
# print_grades(grades)
#


# grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
#
#
# def grades_sum(scores):
#     total = 0
#     for i in scores:
#         total = total + i
#     return total
#
#
# print(grades_sum(grades))
#
#
# def grades_average(grades_input):
#     grades_sum(grades_input)
#     average = grades_sum(grades_input) / float(len(grades_input))
#     return average
#
#
# print(grades_average(grades))


grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def print_grades(grades_input):
    for grade in grades_input:
        print(grade)


def grades_sum(scores):
    total = 0
    for score in scores:
        total = total + score
    return total


def grades_average(grades_input):
    sum_of_grades = grades_sum(grades_input)
    average = sum_of_grades / float(len(grades_input))
    return average


def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance = variance + (score - average) ** 2
    return variance / len(scores)


print(grades_variance(grades))


def grades_std_deviation(variance):
    return variance ** 0.5


variance = grades_variance(grades)
print(grades_std_deviation(variance))

print(print_grades(grades))
print(grades_sum(grades))
print(grades_average(grades))
print(grades_variance(grades))
print(grades_std_deviation(variance))
