

d ={'name':"John", 'age':30, 'city':"New York"}
print(d)
print(d.get('name'))
print(d.keys())
print(d.values())
print(d.items())
# d.clear()
print(d)
d_copy = d.copy()
print(d_copy)
d.update({'DOB':"01-01-1990"})
print(d)
d.setdefault('gender', 'male')
print(d)
d.setdefault('age', 25)  # This will not change the age since it already exists
print(d)
print(len(d))
d.pop('DOB')
print(d)
d.popitem()
print(d)