#O(1) remove duplicates without creating new structures
#check if value already exists once and removes any other instance

def remove_duplicates(nums):
    for i in range(1, len(nums)):
        if (nums[i] == nums[i - 1]):
            nums.pop()
    pass

