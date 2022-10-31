# lamda
# mop filter, reduce
# decorators

# square_number = lambda x: x**2
# print(square_number(3))

# upper_str = lambda str_text: str_text.upper()
# print(upper_str("January"))

#  sum_lists = lambda lists: sum(lists)
#  print(sum_lists([23, 45, 28]))

# sum_num = lambda x, y: x * y
# print(sum_num(3, 8))

kpi = {
    "math": [3, 4, 5, 1],
    "py": [4, 8, 2, 9],
    "java": [3, 2, 5, 3 ]
}
# dict_number = {key: sum(value) for key, value in kpi.items()}
# print(dict_number)

# dict_keys = {key: key for key in kpi}
# print(dict_key)

# dict_number = {key: 45 for key, value in kpi.items() if sum(value) == 23}
# print(dict_number)

# dict_number = {key: sum(value) if sum(value) != 23 else None for key, value in kpi.items() if sum(value) > 10}
# print(dict_number)

# list_num = [2, 4, 6, 8]
# dict_num = dict(enumerate(list_num))
# print(dict_num)

#map

# list_num = [2, 4, 6, 8]
# def get_square_circle(rad):
#      from  math import pi  ####   factorial
#      square = 1
#      for i in range(1, rad+1):
#          square = square * i
#      return round(square, 2)
# # print(get_square_circle(5))
#
# list_square = list(map(get_square_circle, list_num))
# print(list_square)

# def sum_num(a, b, c):
#     return a + b + c
# list_numbers1 = [2, 4, 5, 7]
# list_numbers2 = [4, 9, 5, 7]
# sum_list = list(map(sum_num, list_numbers1, list_numbers2, list_numbers1))
# print(sum_list)

# list_numbers1 = [2, 4, 5, 7]
# def get_division_2(a):
#     if a % 2 == 0:
#         return a
# lists_division = list(filter(get_division_2, list_numbers1))
# print(lists_division)
#
# names = ["Aimardan", "Helpics", "Rome", "Dadyrobins"]
# names1 = ["Aimardan", "Helprrics", "Rome", "Dadyrrobins"]
# def count_names(a, b):
#     if a == b:
#         return a
# lists_division = list(filter(lambda x: x is not None, list(map(count_names, names, names1))))
# print(lists_division)

# from functools import  reduce
#
# list_numbers1 = [2, 4, 5, 7]
# def get_multiple_int(num1, num2):
#     return num1*num2
# multiple_get = reduce(get_multiple_int, list_numbers1, 10)
# print(multiple_get)
#
# multiple_get = reduce(lambda x, y: x - y, list_numbers1, 10)
# print(multiple_get)

##############################
# def timer(func):
#     def wrapper():
#         from datetime import  datetime
#         before = datetime.now()
#         func()
#         after = datetime.now() - before
#         return after
#     return wrapper
# def get_list_with_for_time():
#     from  datetime import datetime
#     lists = []
#     befor = datetime.now()
#     for i in range(1000000):
#         lists.append(i)
#     after = datetime.now() - befor
#     return after
#
# def get_list_with_comprehentions_time():
#     from  datetime import datetime
#     lists = []
#     befor = datetime.now()
#     lists = [ i for i in range(1000000)]
#
#     after = datetime.now() - befor
#     return after
# print(get_list_with_for_time())
# print(get_list_with_comprehentions_time())


def make_hamburger(func):
    def wrapper():
        print("First slice bread")
        print("Mayonez")
        func()
        print("Ketchup")
        print("Second slice bread")
    return wrapper
@make_hamburger
def make_cotlit_beef():
    print("Beef cotlit")
def make_cotlit_chicken():
    print("Chicken cotlit")

make_cotlit_beef()