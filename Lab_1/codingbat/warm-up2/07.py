def array_front9(nums):
    
    lens = len(nums)
    if lens > 4:
        lens = 4   
    for i in range(0, lens):  
        if nums[i] is 9:
            return True
    return False