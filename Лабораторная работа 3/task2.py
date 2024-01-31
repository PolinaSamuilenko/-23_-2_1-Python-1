# TODO Напишите функцию find_common_participants
def find_common_participants(string_1, string_2, separate = ","):
    set_1 = set(string_1.split(separate))
    set_2 = set(string_2.split(separate))
    list_part = list(set_1.intersection(set_2))
    list_part.sort()
    return list_part

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group))
# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, separate= "|"))