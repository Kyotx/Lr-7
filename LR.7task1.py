def characteristic(s):
    # Функция characteristic принимает список s и возвращает сумму положительных четных элементов строки

    sum_even = 0
    for num in s:
        if num > 0 and num % 2 == 0:
            sum_even += num #sum_even = sum_even + num
    return sum_even

def sort_strings_by_characteristic(strings):
    # Функция sort_strings_by_characteristic принимает список строк strings и сортирует их в порядке возрастания характеристик

    # Создаем словарь, где ключами будут строки из списка, а значениями - их характеристики
    chars = {}
    for s in strings:
        chars[s] = characteristic(list(map(int, s.split())))

    # Сортируем словарь по значениям (характеристикам) в порядке возрастания
    sorted_chars = sorted(chars.items(), key=lambda x: x[1])

    # Создаем новый список, в котором строки будут расположены в порядке возрастания характеристик
    sorted_strings = [item[0] for item in sorted_chars]

    return sorted_strings

# Пример использования программы
list_of_strings = ['1 2 3 4', '5 6 7 8', '-1 -2 -3 -4']
sorted_strings = sort_strings_by_characteristic(list_of_strings)
print(sorted_strings)