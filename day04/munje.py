minSeatingMen = 2
maxSeatingMen = 10
men = 100
memo = {}

def func(remainingMen, minMen):
    key = str([remainingMen, minMen])
    if key in memo :
        return sum(memo)
    if remainingMen < 0:
        return 0
    if remainingMen == 0:
        return 1
    
    remainingMen // 10
    memo.append(remainingMen)


print(func(men, maxSeatingMen))