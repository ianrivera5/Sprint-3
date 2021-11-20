# Question 1
# sum_1 = 0
# for numbers in range(1, 1000):
#     if numbers % 3 == 0 or numbers % 5 == 0:
#         sum_1 = sum_1 + numbers
# print(sum_1)

# Question 2
# num_1, num_2 = 0, 1
# total = 0
# while True:
#     num_1, num_2 = num_2, num_1 + num_2
#     if num_2 >= 4000000:
#         break
#     if num_2 % 2 == 0:
#         total += num_2
# print(total)

# Question 6
# def difference(num):
#     return (((num ** 2) * (num + 1) ** 2) / 4) - (num * (num + 1) * (2 * num + 1) / 6)
#
#
# print(difference(100))

# Question 5
# numbers = 2 * 2 * 2 * 2 * 3 * 3 * 5 * 7 * 11 * 13 * 17 * 19
# print(numbers)

# Question 4
# num_max = 0
# for dig in range(100, 999):
#     for dig_1 in range(100, 999):
#         multiply = dig * dig_1
#         if str(multiply) == str(multiply)[::-1]:
#             if multiply > num_max:
#                 num_max = multiply
# print(num_max)
