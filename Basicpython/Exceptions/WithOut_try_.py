print("before exception")
a = 10
b = 0
print("mide exception")

try:
    c = a / b
    print(c)
except Exception as e:
    print("Error:", e)
else:
    print("in else No exception occurred")
finally:
    print("finally block executed")
print("after exception")
