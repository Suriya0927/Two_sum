def twoSum(num, target):
    for i in range(0,len(num)):
        for j in range(i+1, len(num)):
            if (target-num[i]) == num[j]:
                print(i,j)


num = [2,7,11,5]
target = 9
twoSum(num,target)

