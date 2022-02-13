def intersection(self, nums1, nums2):
    result: Set = set()
    nums1.sort()
    nums2.sort()
    i = j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]: j += 1
        elif nums1[i] < nums2[j]: i += 1
        else:
            result.add(nums1[i])
            i += 1
            j += 1
    