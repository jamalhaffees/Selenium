car={
    "brand": "Toyota",
    "model": "Rav4",
    "color":"Blue",
    "year": 2021,
}
a = car.keys()
print(a)

b = car.values()
print(b)

car["value"]= "$40k"
print(car)

car.update({"type": "SUV"})
print(car)

del car["value"]
print(car)

for y in car.values():
    print(y)

for c, d in car.items():
    print(c,d)

