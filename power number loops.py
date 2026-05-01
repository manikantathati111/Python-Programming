base=int(input("enter base value:"))
exponent=int(input("enter exponent value:"))
power=1
for i in range(exponent):
    power=power*base
print("power number =",power)