# 2. Напишите функцию, которая проверяет: является ли слово палиндромом

def palindrome(a):
    return a[::-1] == a

while True:
    a = input('Введите слово: ')
    print(f'{a} Это полиндром' if palindrome(a) else f'{a} Это не полиндром')
























