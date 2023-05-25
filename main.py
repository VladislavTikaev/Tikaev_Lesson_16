# Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения, а чётные нацело делит на два.
l = [int(i) for i in input().split()]
def modify_list(l):
    l[:] = [i // 2 for i in l if i % 2 == 0]
print(modify_list(l))
print(l)