def decToBin(dec):
    assert int(dec) == dec, "The parameters must be an integer only!"
    if dec == 0:
        return 0
    return dec%2 + 10 * decToBin(int(dec/2))

print(decToBin(10))
