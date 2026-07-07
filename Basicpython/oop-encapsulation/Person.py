class Person:
    AVG_AGE = 18  # static constant

    def __init__(self):
        print(" Cons is calliing  ther person class")
        self.__name = None
        self.__dob = None
        self.__address = None


    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def set_dob(self, dob):
        self.__dob = dob  # dob should be datetime object

        # Getter and Setter for address

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address



p = Person()
p.set_name("Ram")
p.set_dob("2000-01-01")
p.set_address("Indore")
print("Name:",p.get_name())
print("DOB:",p.get_dob())
print("Address:",p.get_address())
print(Person.AVG_AGE)