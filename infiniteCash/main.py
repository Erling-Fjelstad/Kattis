salary = int(input(), 2)
paymentDay = int(input(), 2)
savings = int(input(), 2)

days = 0
daysSincePaymentDay = 0
cash = savings

while cash > 0:
    days += 1
    daysSincePaymentDay += 1
    toSpend = (cash + 1) // 2
    cash -= toSpend
    if daysSincePaymentDay == paymentDay:
        cash += salary
        daysSincePaymentDay = 0
        if cash >= savings or days > 1000000:
            print("Infinite money!")
            quit()
            
print(f"{days:b}")
