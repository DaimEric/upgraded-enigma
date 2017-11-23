class Person:
    def __init__(self):
        self.__first_name = str()
        self.__last_name = str()
        self.__day = int()
        self.__month = int()
        self.__year = int()

    def set_name(self, forename, surname):
        self.__first_name = forename
        self.__last_name = surname

    def get_name(self):
        return self.__first_name + " " + self.__last_name

    def set_dob(self, d, m, y):
        if self.__is_valid_date(d, m):
            self.__day = int(d)
            self.__month = int(m)
            self.__year = int(y)
        else:
            return "Invalid date entered."

    def get_dob(self):
        return "{0}-{1}-{2}".format(self.__day, self.__month, self.__year)

    def get_age_at(self, d, m, y):
        age = -1
        if self.__is_valid_date(d, m) and self.__is_after_dob(d, m, y):
            age = y - self.__year
            if (m < self.__month) or (m == self.__month and d < self.__day):
                age -= 1
        return age

    def get_details(self):
        return "{0}, {1}".format(self.get_name(), self.get_dob())

    def __is_valid_date(self, d, m):
        return 0 < d <= 31 and 0 < m <= 12

    def __is_after_dob(self, d, m, y):
        return (y > self.__year) or\
               (y == self.__year and m > self.__month) or\
               (y == self.__year and m == self.__month and d > self.__day)


john = Person()

john.set_name("John", "Lennon")
john.set_dob(8, 10, 1940)

print(john.get_details())

daim = Person()

daim.set_name("Daim", "Eric")
daim.set_dob(20, 10, 1945)

print(daim.get_details())
