def func(l):
   x = l.split(' ')
   suma = 0
   print(f'Список із введених чисел: {x}')
   for i in x:
       i = int(i)
       suma += i
   print(f'Сума списку: {suma}')
func(input('Введіть числа через пробіл: '))


def pal(word):
    word = word.lower().split(' ')
    word1 = ''.join(word)
    if word1[::-1] == word1:
        print(True)
    else:
        print(False)
pal(input('Введіть слово для перевірки: '))


def sort(a):
    for i in a:
        a.sort(key=len)
    print(a)
sort(input('Введіть слова через пробіл: ').split(' '))