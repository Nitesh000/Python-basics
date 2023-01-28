def sum_of_digits(num):
    assert num>=0 and int(num) == num, "the number has to be a positive integer only!"
    if num == 0:
        return 0
    else:
        return int(num%10) + sum_of_digits(int(num/10))

print(sum_of_digits(4))
print(sum_of_digits(332))
print(sum_of_digits(-4))
