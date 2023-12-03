import random

def common_elements(set1, set2):
    # Функция common_elements принимает два множества set1 и set2 и возвращает список чисел, которые входят и в первое, и во второе множество, в порядке возрастания

    # Создаем список для хранения общих элементов
    common = []

    # Проходим по каждому элементу в первом множестве
    for number in set1:
        # Проверяем, содержится ли текущий элемент во втором множестве
        if number in set2:
            # Если элемент есть в обоих множествах, добавляем его в список общих элементов
            common.append(number)

    # Сортируем список общих элементов по возрастанию
    common.sort()

    return common


# Пример использования программы
set1 = set(random.sample(range(1, 10001), 1000))
set2 = set(random.sample(range(1, 10001), 10000))

common_elements_list = common_elements(set1, set2)
print(common_elements_list)