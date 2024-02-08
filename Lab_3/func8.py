def ans(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 0 and nums [i + 1] == 0 and nums [i + 2] == 7:
            return True 
        
    return False
    
has = [1,2,4,0,0,7,5]
print(ans(has))

hasnt = [1, 3, 1]
print(ans(hasnt))