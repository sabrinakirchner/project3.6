hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

hweek = 40
over = 0.5


def computepay(hrs, rate,hweek):

    if hrs >= hweek:
        reg = hrs * rate
        otp = (hrs - hweek) * (rate*over)
        pay = reg + otp
    else:
        pay = hrs * rate
    return pay

func = computepay(hrs,rate,hweek)

print('Pay:', func)


