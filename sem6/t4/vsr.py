def numb():
    a = input("Введите цифру от 0 до 9, если нужно, то через пробел укажите систему счисления (bin, oct, hex)\n")
    bases = ('bin', 'oct', 'hex')
    if len(a) >= 2:
        osn = a[1:]
        assert osn in bases, 'Системы счисления могут быть толк bin, oct или hex'
        try:
            int_number = int(a[0])
        except:
            raise ValueError('Можно ввводить только числа от 0 до 9')
        if osn == 'bin':
            res = bin(int_number)
        elif osn == 'oct':
            res = oct(int_number)
        elif osn == 'hex':
            res = hex(int_number)
    else:
        names_of_numbers = {
            '0': 'Ноль',
            '1': 'Один',
            '2': 'Два',
            '3': 'Три',
            '4': 'Четыре',
            '5': 'Пять',
            '6': 'Шесть',
            '7': 'Семь',
            '8': 'Восемь',
            '9': 'Девять'
        }
        assert a in names_of_numbers, 'Можно ввводить только числа от 0 до 9'
        res = names_of_numbers[a]
    return res

print(numb())
