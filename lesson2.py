# legb scope

#local -l
#encloses -e
#global -g
#built-in -b

# a = "global var"

# def get_sum():
#     a = 4
#     b = 5
#     return a + b
# print(get_sum())
# print(a)

# def hello():
#     word = "Hello word!!!"
#     def by():
#         nonlocal word
#         word = "byu byu"
#         print(word)
#     return by()
#
# hello()

# pi = 3.15
# def get_pi():
#     global pi   # Warning !!!
#     pi = 3.11
#     print(pi)
# get_pi()
# print(pi)

# def get_pi():
#     pi = 3.11
#     print(pi)
# func = get_pi
# func()

# def obertka(func):
#     def _wrapper():
#         print("function start")
#         func()
#         print("function end")
#     return _wrapper
# @obertka
# def get_pi():
#     pi = 3.11
#     print(pi)
#
# get_pi()

