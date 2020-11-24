"""
Реализовать работу с двумя списками: сравнение, сложение, поэлементное сложение,
нахождение и подсчёт одинаковых элементов.
"""

def sovpad(list1, list2):
    sovpad = list(set(list1) & set(list2))
    num_sovpad = len(sovpad)
    return print(f"Повторяющиеся Элементы:{sovpad}, в количестве {num_sovpad}")

def add(list1, list2):
    add_result = list1.copy()
    add_result.extend(list2)
    return print(f"Объединения списка {list1} и списка {list2}: {add_result}")

def add_elements(list1, list2):
    if len(list1) <= len(list2):
        list2_copy = list2.copy()
        for i in range(len(list1)):
            list2_copy[i]+=list1[i]
        return print(f"Результат поэлементного сложения списков {list1} и {list2}: {list2_copy}")
    else:
        list1_copy = list1.copy()
        for i in range(len(list2)):
            list1_copy[i]+=list2[i]
        return print(f"Результат поэлементного сложения списков {list1} и {list2}: {list1_copy}")


list1 = ["ангары", "диашиз", "лентяй", "окуляр", "памела", "портер", "ужение", "хионея", "швабка", "шпанка", "диашиз"]
list2 = ["ангары", "диашиз", "диашиз", "детище", "памела", "окуляр", "угроза", "окуляр", "швабка", "диашиз"]
list3 = [1, 2, 3, 4, 5]
list4 = [25 ,-6, 6, 6, 0, 11, 20, 1]

sovpad(list1, list2)
add(list1, list2)
add_elements(list3, list4)
