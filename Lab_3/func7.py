def ans(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums [i + 1] == 3:
            return True 
        
    return False
    
has33 = [1, 3, 3]
print(ans(has33))

hasnt33 = [1, 3, 1]
print(ans(hasnt33))