def validInputCon(numbers):
    # check inc
    seqCount = 0
    for i in range(1, len(numbers)):
        if int(numbers[i-1]) == (int(numbers[i])+1)%10:
            seqCount+=1
            print("- %d, %d, %d" % (int(numbers[i-1]), int(numbers[i]), seqCount))
        else:
            seqCount=0
            
        if seqCount >=2:
            return False
        
    # check dec
    seqCount = 0
    for i in range(1, len(numbers)):
        if int(numbers[i-1]) == (int(numbers[i])-1)%10:
            seqCount+=1
            print("+ %d, %d, %d" % (int(numbers[i-1]), int(numbers[i]), seqCount))
        else:
            seqCount=0
            
        if seqCount >=2:
            return False
    return True

def validInputDup(numbers):
    seqCount = 0
    for i in range(1, len(numbers)):
        if int(numbers[i-1]) == int(numbers[i]):
            seqCount+=1
            print("= %d, %d, %d" % (int(numbers[i-1]), int(numbers[i]), seqCount))
        else:
            seqCount=0
            
        if seqCount >=2:
            return False
    return True

def validInputPattern(numbers):
    print(numbers)
    return True

while True:
    inputstr = input("input:")
    numbers = inputstr.split(',')
    isOk = validInputDup(numbers)
    if isOk:
        isOk = validInputCon(numbers)
    if isOk:
        isOk = validInputPattern(numbers)

    if isOk:
        print ("검증 완료")
        break
    else:
        print("규칙에 안맞아")
