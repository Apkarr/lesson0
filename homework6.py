
my_dict = {'Ленин': 1870, 'Сталин': 1878, 'Дзержинский': 1877,
                    'Свердлов': 1885, 'Троцкий': 1879}
print(my_dict)
print(my_dict['Троцкий'])
print(my_dict.get('Орджоникидзе'))
my_dict.update({'Калинин': 1875,
               'Киров': 1886})
my_dict.pop('Ленин')
print(my_dict)


my_set = {1, 2, 2, 4, 6, 6, 6, 'lessons', (4, 55, 666), True}
print(my_set)
my_set.update([76, 81], 'W')
my_set.remove(2)
print(my_set)

 