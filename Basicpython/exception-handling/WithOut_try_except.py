print("Before")
a = 10
b = 0

try:
    c = a / b
    print("division ", c)
except Exception as e:
    print("Error: ", e)
else:
    print("Division is successful")
finally:
    print("Finally block is executed")

print("After")
