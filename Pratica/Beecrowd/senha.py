sh = []
while True:
    se = int(input())
    sh.append(se)
    if se < 1001 or se > 9999:
        sh.remove(se)
        break
for i in sh:
    print(i-1)