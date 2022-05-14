misc_tuple = ('Job', 38, True, 44,'female')
print(misc_tuple)
print(len(misc_tuple))
print(misc_tuple[3])

y = list(misc_tuple)
y[3] = 'Fourty'
misc_tuple=tuple(y)
print(misc_tuple)

for item in misc_tuple:
    print(item)



