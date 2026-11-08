nums = [1, 2, 1]

total = 0

for i in range(len(nums)):
    distinct = set()

    for j in range(i, len(nums)):
        distinct.add(nums[j])
        count = len(distinct)

        total = total + (count * count)

print("Output:", total)
