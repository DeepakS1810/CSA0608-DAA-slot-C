def unique_elements(nums):
    unique = []

    for num in nums:
        if num not in unique:
            unique.append(num)

    return unique


# Test Case 1
nums = [3, 7, 3, 5, 2, 5, 9, 2]
print("Output:", unique_elements(nums))

# Test Case 2
nums = [-1, 2, -1, 3, 2, -2]
print("Output:", unique_elements(nums))

# Test Case 3
nums = [1000000, 999999, 1000000]
print("Output:", unique_elements(nums))
