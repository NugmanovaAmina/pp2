def has_3(nums : list):
    for i in range(len(nums) - 1):
        if (nums[i] == nums[i + 1] == 3):
            return True
        
    return False