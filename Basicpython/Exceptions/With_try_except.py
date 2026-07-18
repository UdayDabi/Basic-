print("Before")
a = 10
b = 0
print("Mid")
try:
    c = a / b
    print(c)
except Exception as e:
    print("Exception:", e)
else:
    print("In else block")
finally:
    print("In finally block")
print("After")
