def tribonacci( n: int) -> int:
        n0, n1, n2 = 0,1,1
        res = 0
        for i in range (3,n+1):
            res = n0 + n1 + n2
            n0 = n1
            n1 = n2
            n2 = res
            print(f"now res {res}")
        return res

print(tribonacci(9)) 
