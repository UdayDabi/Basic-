from reportlab.platypus.para import test_program

test_dict={'name':"John", 'age':30, 'city':"New York"}
print(test_dict)
print(test_dict.get('age'))
print(test_dict.keys())
print(test_dict.values())
print(test_dict.items())
# test_dict.clear()
# print(test_dict)
# test_dict.pop('age')
print(test_dict)
# test_dict.popitem()
print(test_dict)
print(len(test_dict))
test_dict.update({'LastName':"Dabi"})
print(test_dict)
