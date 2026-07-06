from itertools import permutations

list = [10,20,30,40,50]
list1=[60,70,80,90,100]
new_list = list+list1
print(new_list)
# print(new_list[2:8])
new_list.append(101)
print(new_list)
print(new_list.count(10))
print(new_list.index(30))
new_list.insert(10,110)
print(new_list)
new_list.remove(110)
print(new_list)
new_list.reverse()
print(new_list)
new_list.sort()
print(new_list)
print(min(new_list))