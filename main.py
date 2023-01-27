from typing import Callable

#
# def do_operation(a, b, operation):
#     result = operation(a, b)
#     print(f"{result=}  ")
#
#
# def plus(a, b):
#     return a + b
#
#
# def minus(a, b):
#     return a - b


# def select_operation(chice: int)-> Callable:
#     if chice == 1:
#         return plus
#     elif chice == 2:
#         return minus


# selected_operation = select_operation(1)
# print(selected_operation(10, 20))
# do_operation(92, 67, selected_operation)

# map(функция, список или строка)


# number_str = [str(i) for i in range(1, 14+1)]
# number_str2 = [str(i) + " Hello" for i in range(1, 14+1)]

list_for_say_hello = []

# for item in number_str:
#     list_for_say_hello.append(item + " Hello")


# print(list_for_say_hello)

# def add_hello(item):
#     return item + " Hello"


# a = list(map(str.upper, number_str))
# print(list(map(str.upper, a)))


# result = []
# for i in numbers:
#     if i % 2 == 0:
#         result.append(i ** 3)
#     if i % 2 != 0:
#         result.append(i - i)

# print(result)


# def multi(num):
#     if num % 2 == 0:
#         return num ** 3
#     if num % 2 != 0:
#         return num - num

# print(list(map(multi, numbers)))
# numbers_list = [x for x in range(1, 11)]
# numbers_list_2 = [x for x in range(11, 20)]
#
# def multi2(num1, num2):
#     print(num1, num2)
#     return num1 * num2
#
# print(list(map(multi2, numbers_list, numbers_list_2)))

# filter(функция для проверки, список для проверки)
doston = [i for i in range(1,21)]

def even(num):
    return num % 2 == 0

def not_even(num):
    return num % 2 !=0

# print(list(filter(even, doston)))
# print(list(filter(not_even, doston)))

trash_list = [987, 782,"jfkid", "hf", (), {178: 783}, []]

def clean_list_for_Aziza(element):
    return type(element) is int

# print(list(filter(clean_list_for_Aziza, trash_list)))

list_for_say = [str(i) for i in range(10+1)]


hello_list = list(map(lambda x: x + " Hello", list_for_say))

num_list1 = [i for i in range(22)]


# print(list(filter(lambda x: x % 2 == 0, num_list1)))
# print(list(filter(lambda x: x % 2 != 0, num_list1)))

# print(hello_list)
