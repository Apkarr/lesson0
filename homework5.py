
immutable_var = 3, 'gud', [2, 7, 5], True
print(immutable_var, type(immutable_var))
print(immutable_var[1])
#immutable_var[1] = 'ok'  # если это строку кода раскомментировать будет выдаваться ошибка, описанная ниже;
print(immutable_var[1])  # объект "кортеж" не поддерживает назначение элементов,
                        # относится к неизменяемому типу данных

mutable_list = [1, 2, 3, 5, 8, 's']
print(mutable_list[3])
mutable_list[2] = 24, 'k', 4
print(mutable_list)
mutable_list[0:3] = 24, 'k', 4
print(mutable_list)