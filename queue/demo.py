ll = 4 * []
lls = ["hii", "hello", "bye", "goodbye"]
cat = ""
intll = [1,3,4,5]
for i in range(len(lls)):
    cat += " " + lls[i]

cool = " ".join(lls)

print(ll)
print(cool)
intp = " ".join(str(x) for x in intll)
print(type(intp))
intp_rev = intp[::-1]
print(intp_rev)
