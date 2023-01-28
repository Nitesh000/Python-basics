def power(base, exp):
    assert exp >= 0 and int(exp) == exp, "Please insert integers."
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else: 
        return base * power(base, exp - 1)

print(power(2,4))
print(power(4,4))
print(power(2,-4))
