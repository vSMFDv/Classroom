import math
#1
def replace_first_with_zero_if_needed(a, b):
    return (0,b) if a <= b else (a,b)

#2
def square_non_negative(a, b, c):
    return [x**2 if x >= 0 else x for x in [a, b, c]]

#3
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

#4
def select_numbers_in_interval(a, b, c):
    return [x for x in [a, b, c] if 1 < x < 3]

#5
def stop_input_when_smaller():
    prev = int(input("Введите число: "))
    while True:
        curr = int(input("Введите число: "))
        if curr < prev:
            break
        prev = curr

#6
def perform_action_on_x(x):
    print("1 - Возвести в квадрат")
    print("2 - Извлечь корень квадратный")
    print("3 - Вычислить синус")
    print("4 - Косинус")
    action = int(input("Введите номер действия: "))
    if action == 1:
        return x ** 2
    elif action == 2:
        return x ** 0.5
    elif action == 3:
        return math.sin(x)
    elif action == 4:
        return math.cos(x)

#7
def multiplication_table(k):
    for i in range(2, 11):
        print(f"{i} x {k} = {i * k}")

#8
def to_uppercase(letter):
    return letter.upper()

#9
def replace_numbers(a, b, c, d):
    if a <= b <= c <= d:
        max_value = max(a, b, c, d)
        return [max_value] * 4
    elif a > b > c > d:
        return [a, b, c, d]
    else:
        return [x**2 for x in [a, b, c, d]]

#10
def print_rectangle(m, n):
    for _ in range(m):
        print('1' * n)

#11
def transform_number(a, b, z):
    if a % b == 0:
        return z * (a // b)
    else:
        return z / (a % b)

#12
def has_even_local_maximum(sequence):
    for i in range(1, len(sequence) - 1):
        if sequence[i] > sequence[i - 1] and sequence[i] > sequence[i + 1] and sequence[i] % 2 == 0:
            return True
    return False

#13
def count_and_sum_divisible_by_5_not_7(sequence):
    filtered = [x for x in sequence if x % 5 == 0 and x % 7 != 0]
    return len(filtered), sum(filtered)

#14
def double_sum_of_positives(sequence):
    return 2 * sum(x for x in sequence if x > 0)

#15
def product_of_multiples_of_7(sequence):
    result = 1
    for x in sequence:
        if x % 7 == 0:
            result *= x
    return result

#16а
def evaluate_function_a_a(a):
    return a**2 if -2 <= a <= 2 else 4

#16b
def evaluate_function_a_b(a):
    return a**2+4*a+5 if a<=2 else 1/a**2+4*a+5

#17
def compute_expression(a, n):
    return a ** n, math.prod([a + i for i in range(n)]), sum(1 / math.prod([a + i for i in range(j + 1)]) for j in range(n))


#18
def average_excluding_i(sequence, i):
    return sum(sequence[:i] + sequence[i+1:]) / (len(sequence) - 1)

#19
def check_triangle(x, y, z):
    if x + y > z and x + z > y and y + z > x:
        if x**2 + y**2 > z**2 and x**2 + z**2 > y**2 and y**2 + z**2 > x**2:
            return "Остроугольный треугольник"
        return "Треугольник существует"
    return "Треугольник не существует"

#20
def replace_smallest_if_sum_less_than_one(x, y, z):
    if x != y and y != z and x != z and (x + y + z) < 1:
        min_value = min(x, y, z)
        if min_value == x:
            x = (y + z) / 2
        elif min_value == y:
            y = (x + z) / 2
        else:
            z = (x + y) / 2
    else:
        if x < y:
            x = (y + z) / 2
        else:
            y = (x + z) / 2
    return x, y, z

#21
def solve_quadratic(a, b, c):
    if a == 0:
        return "a не должно быть равно нулю"
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return "Действительных корней нет"
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        return root1, root2

#22
def to_binary_representation(n):
    return bin(n)[2:]


#1
print(replace_first_with_zero_if_needed(1, 2))  # (0, 2)
print(replace_first_with_zero_if_needed(3, 2))  # (3, 2)

#2
print(square_non_negative(1, -2, 3))  # [1, -2, 9]

#3
print(sum_of_digits(123))  # 6

#4
print(select_numbers_in_interval(1, 2, 3))  # [2]

#5
#stop_input_when_smaller()

#6
# print(perform_action_on_x(4))

#7
multiplication_table(5)

#8
print(to_uppercase('a'))  # 'A'

#9
print(replace_numbers(1, 2, 3, 4))  # [4, 4, 4, 4]
print(replace_numbers(5, 4, 3, 2))  # [5, 4, 3, 2]
print(replace_numbers(1, 3, 2, 4))  # [1, 9, 4, 16]

#10
print_rectangle(3, 5)  # Прямоугольник 3x5 из 1

#11
print(transform_number(8, 2, 3))  # 12
print(transform_number(7, 3, 2))  # 2.0

#12
print(has_even_local_maximum([1, 4, 2, 6, 3]))  # True
print(has_even_local_maximum([1, 3, 2, 1]))  # False

#13
print(count_and_sum_divisible_by_5_not_7([5, 10, 15, 35, 40]))  # (3, 55)

#14
print(double_sum_of_positives([-1, 2, 3, -4]))  # 10

#15
print(product_of_multiples_of_7([7, 14, 2, 3]))  # 98

#16
print(evaluate_function_a_a(-4))  # 4
print(evaluate_function_a_b(1))  # 10

#17
print(compute_expression(2, 3))  # 8,24,0.708(3)

#18
print(average_excluding_i([1, 2, 3, 4], 2))  # 2.(3)

#19
print(check_triangle(3, 4, 5))  # Треугольник существует
print(check_triangle(1, 2, 3))  # Треугольник не существует

#20
print(replace_smallest_if_sum_less_than_one(0.2, 0.3, 0.4))  # (0.35, 0.3, 0.4)
print(replace_smallest_if_sum_less_than_one(1, 2, 3))  # (1, 2, 3)

#21
print(solve_quadratic(1, -3, 2))  # (2.0, 1.0)
print(solve_quadratic(1, 2, 1))  # -1.0
print(solve_quadratic(1, 1, 1))  # Действительных корней нет

#22
print(to_binary_representation(10))  # '1010'
