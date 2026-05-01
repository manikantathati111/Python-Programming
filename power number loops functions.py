def my_function(base,exponent,power):
    for i in range(exponent):
        power=power*base
    return power
base=int(input("enter base value:"))
exponent=int(input("enter exponent value:"))
power=1
print("power number =",my_function(base,exponent,power))