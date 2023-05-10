def div3(num):
    print(num % 3 == 0)

def div100(num):
    if type(num) is str:
        raise TypeError
    elif num == 0:
        raise ZeroDivisionError 
    else:
        print(num / 100)

def magicDate(Date):
    Date = Date.split('.')
    Magic = int(Date[0]) * int(Date[1]) == int(Date[2][2:4])
    print(Magic)

def luckyTiket(Tiket):
    lucky = sum([eval(i) for i in Tiket][:3]) ==  sum([eval(i) for i in Tiket][3:6])
    print(lucky)

