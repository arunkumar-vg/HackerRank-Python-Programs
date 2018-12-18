n = int(input())
dic = {}
for i in range(0, n):
    inputArray = input().split()
    marks = list(map(float, inputArray[1:]))
    dic[inputArray[0]] = sum(marks)/float(len(marks))
print("%.2f" % dic[input()])

