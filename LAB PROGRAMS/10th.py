def sort_array(nums):
    if len(nums) < 2:
        return nums

    def merge_sort(arr, temp, start, end):
        if end - start <= 1:
            return

        mid = (start + end) // 2
        merge_sort(arr, temp, start, mid)
        merge_sort(arr, temp, mid, end)

        left, right, index = start, mid, start

        while left < mid and right < end:
            if arr[left] <= arr[right]:
                temp[index] = arr[left]
                left += 1
            else:
                temp[index] = arr[right]
                right += 1
            index += 1

        while left < mid:
            temp[index] = arr[left]
            left += 1
            index += 1

        while right < end:
            temp[index] = arr[right]
            right += 1
            index += 1

        for index in range(start, end):
            arr[index] = temp[index]

    temp = [0] * len(nums)
    merge_sort(nums, temp, 0, len(nums))
    return nums


nums = [5, 2, 3, 1]
print(sort_array(nums))
