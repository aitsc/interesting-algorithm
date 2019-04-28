def lengthOfLIS(nums) -> int:
    if not nums:
        return 0
    seqList = []
    for i, x in enumerate(nums):
        m = 1
        for j in range(i):
            if x > nums[j]:
                m = max(m, seqList[j] + 1)
        seqList.append(m)
    return max(seqList)

print(lengthOfLIS([10,9,2,5,3,7,101,18]))