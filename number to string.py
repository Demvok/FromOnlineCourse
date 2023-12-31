# объявление функции
def number_to_words(num):
    majors = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    digits = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', '']
    teens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    if 1 <= num <= 9:
        return digits[num-1]
    elif 10 <= num <= 19:
        return teens[num%10]
    else:
        return (str(majors[num//10-2]) + ' ' + str(digits[num%10-1])).strip()
# считываем данные
n = 40

# вызываем функцию
print(number_to_words(n))