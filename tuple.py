# a=["Noob",23,"pro"]

# print(a.index(23))

b={'1':"dog",'2':"cat",'3':"cow",'4':"pig"}
c={"dog","rat","dragonfly","butterfly"}

# print(b.get('1'))
# print(b.keys())
# print(b.values())
b.update({'5':'rat'})
b.pop('2')
for key,value in b.items():
    print(key, value)
print (c)
# b.add("chicken")
# c.remove("dragonfly")
# b.update(c)
# d=b.union(c)
# b.clear()
# print(b.difference(c))
# print(b.intersection(c))