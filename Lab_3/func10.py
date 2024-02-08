def ans(nums):
    glist = []
    for i in nums:
        if nums.count(i) == 1:
            glist.append(i) 
    return glist

x = [1,1,1,2,2,3,4]
res = ans(x)
print(res)
