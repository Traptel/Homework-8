# Завдання 1
print("Завдання 1")
numbers = [2, 3, 7, 7, 3, 9, 1, 1, 7, 6, 6, 2]
set_numbers = set(numbers)
print("Кількість різних чисел в списку: ", len(set_numbers))
print(set_numbers)

# Завдання 2
print("\nЗавдання 2")
list1 = [1, 2, 3, 1, 2, 3]
list2 = [3, 4, 5, 3, 4, 5]
set1 = set(list1)
set2 = set(list2)
common_numbers = set1 | set2
print(common_numbers)

# Завдання 3
print("\nЗавдання 3")
lst = [12, "A", [1, 2], {"name": "Nikita"}, 19, "B", True, {1, 2}]
hashable_set = set()

for i in lst:
    if type(i) not in (list, dict, set):
        hashable_set.add(i)

print(hashable_set)
