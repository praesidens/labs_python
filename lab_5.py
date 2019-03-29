class Person:
    Name = "B"
    LastName = "S"
    Address = "Lmnsv"
    Passport = "rand"
    Age = 21
    Phone = 1233123
    def __init__(self, n, ln, addr, passport, age, phone):
        self.Name = n
        self.LastName = ln
        self.Address = addr
        self.Passport = passport
        self.Age = age
        self.Phone = phone
    def new_person(n, ln):
        with open("list_of_names", "a") as f:
            line = n + ' ' + ln + '\n'
            f.write(line)

    
    def print_info():
        with open("list_of_names", "r") as f:
            print(f.readlines())


a = Person('B', 'S', 'Lmnsv', 'rand', 21, 32131323)
Person.new_person('D', 'Z')
Person.new_person("S", "D")
print(a.Name)
Person.print_info()
