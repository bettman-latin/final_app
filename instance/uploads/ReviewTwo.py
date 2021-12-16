import datetime

class Ticket(object):
    def __init__(self, n, d):
        self.price =  0
        self.number = n
        self.date = d

class WalkUp(Ticket):
    def __init__(self, n, d):
        super(WalkUp, self).__init__(n, d)

        self.price = 50

    def __str__(self):
        return "Number: " + self.number + ", Price: " + self.price

class Advance(Ticket):
    def __init__(self, n, p, d):
        super(Advance, self).__init__(n, p)
        if difference >= 10:
            self.price = 30
        else:
            self.price = 40


        self.number = n 
        self.price = d


    def __str__(self):
        return "Number: " + self.number + ", Price: " + self.price

class StudentAdvance(Ticket):
    def __init__(self, n, p):
        super(StudentAdvance, self).__init__(n, p)
        if difference >= 10:
            self.price = 10
        else:
            self.price = 15

        self.number = n 
        self.price = p

    def __str__(self):
        return "Number: " + self.number + ", Price: " + self.price


show = datetime.date(2021, 9, 10)
print("The show is on: {0}".format(show))

print("When are you buying these tickets?")
buyDate = datetime.date(year = int(input("Year: ")), month = int(input("Month: ")), day = int(input("Day: ")))

difference = show - buyDate

print("You are buying tickets {0} days from the show.".format(difference))

yesno = input("Are you a student? (yes/no): ")
if yesno == "yes":
    student = True
else:
    student = False

print(student)
def main():
    return 

# datetime.timedelta()

# def AdvancePrice(d):
#     return