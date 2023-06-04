def moveZeroes(nums):
    n = len(nums)
    left = 0  # Pointer to track the current position to place the next non-zero element

    # Iterate through the array
    for i in range(n):
        if nums[i] != 0:
            # If the current element is non-zero, move it to the left pointer position
            nums[left] = nums[i]
            left += 1

    # Fill the remaining positions from the left pointer to the end of the array with zeros
    while left < n:
        nums[left] = 0
        left += 1

# Test case
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)
