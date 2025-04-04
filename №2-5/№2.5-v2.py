num = list(range(1,21))

fnum = list(filter(lambda x: (x%2 == 0), num))
upnum = list(map(lambda x: (x+10), fnum))
sortnum = sorted(upnum, reverse = True)

print(fnum)
print(upnum)
print(sortnum)