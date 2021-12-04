'''
Задание 1.
Написать функцию isNumberEven(), 
которая принимает одно число и возвращает True, 
если чисто четное и ложь - если число нечетное.

Можно удалить комментарий внутри функции и пустой оператор pass
Возвращаемое значение логического типа (True/False) передается обратно с помощью
оператора return
'''


def isNumberEven(num):
    # ...
    # return ...
    pass


a = int(input("Enter the number: "))
even = isNumberEven(a)
if even:
    print("Your number is even")
else:
    print("Your number is odd")


'''
Задание 2.
Написать функцию getLongerWord(w1, w2)
которая принимает две строки w1 и w2 и возвращает ту строку, длина которой больше.
В случае, если обе строки имеют одинаковую длину - функция должна возвратить
первую строку.

В данном примере код функции реализован с ошибками, исправить ошибку внутри функции getLongerWord()

'''


def getLongerWord(w1, w2):
    # ...
    # return ...
    return w1


# Testing:
a1 = getLongerWord("apple", "car")
a2 = getLongerWord("ball", "abrakadabra")
a3 = getLongerWord("foo", "bar")

print(a1)
print(a2)
print(a3)

# Expected output:
# apple
# abrakadabra
# foo

'''
Задание 3.
Написать функцию getNextDigit(num)
которая принимает цифру от 0 до 9
и возвращает "следующее число"
0 -> 1
1 -> 2
...
8 -> 9
9 -> 0

'''

# Testing


def getNextDigit(num):
    # TODO: add implementation here!
    pass


numbers = [0, 7, 2, 9]
for n in numbers:
    next = getNextDigit(n)
    print(f"{n} -> {next}")

'''
Задание 4.
Написать функцию printNumbersUntil(num),
которая выводит на экран (print) 
все числа, начиная от 1 заканчивая num (включительно)

'''

# Testing:


def printNumbersUntil(n):
    pass


print("All numbers until 5:")
printNumbersUntil(5)

print("All numbers until 1:")
printNumbersUntil(1)

print("All numbers until 0:")
printNumbersUntil(0)

# Expected output:
# All numbers until 5:
# 1
# 2
# 3
# 4
# 5
# All numbers until 1:
# 1
# All numbers until 0:
# (ничего)

'''
Задание 5.
Написать функцию returnDigits(a),
которая принимает двузначное целое число а
и возвращает первую и вторую цифру этого числа.

Если число однозначное или больше двузначного - вернуть две цифры None (ошибка)
'''

# Testing


def returnDigits(a):
    # TODO: add implementation!
    return None, None


d1, d2 = returnDigits(25)
print(f"{d1} and {d2}")

d3, d4 = returnDigits(10)
print(f"{d3} and {d4}")

d5, d6 = returnDigits(9)
print(f"{d3} and {d4}")

d7, d8 = returnDigits(100)
print(f"{d7} and {d8}")

# Expected output:
# 2 and 5
# 1 and 0
# None and None
# None and None


'''
Задание 6.
Написать функцию rangeList(beg, end)
которая принимает два числа: from, to
и возвращает список, содержащий числа от from до to (исключая to).

Функция должна возвратить пустой список, если from больше или равно to
'''

# Testing


def rangeList(beg, end):
    return []


l1 = rangeList(2, 5)
print(l1)

l2 = rangeList(5, 2)
print(l2)

# Expected output:
# [2, 3, 4]
# []
