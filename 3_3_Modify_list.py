# Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения, а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка

def modify_list1(l):
    shift = 0
    for i in range(0, len(l)):
        i = i - shift
        if l[i] % 2 == 0:
            l[i] = l[i] // 2
        else:
            l.pop(i)
            shift += 1


def modify_list2(l):
    l[:] = [i // 2 for i in l if i % 2 == 0]


l = [1, 2, 3, 4, 5]
modify_list1(l)
print(l)

l = [1, 2, 3, 4, 5]
modify_list2(l)
print(l)
