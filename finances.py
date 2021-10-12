import datetime

today = datetime.date.today()
print(today)

time_delta = datetime.timedelta(days = 7)

print(today + time_delta)
print(today - time_delta)


# class Finances :
    # def __init__(self, name) :
        # self.name = name
#
    # def receive_payment(self) :
        # pass
    # def make_payment(self) :
        # pass
    # def get_balance(self) :
        # pass
