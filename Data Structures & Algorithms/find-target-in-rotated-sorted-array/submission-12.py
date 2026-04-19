class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            #mid is in left array
            if nums[l] <= nums[mid]:
                #if target is not in section of left array or is in right array
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    #else target is in left sorted array
                    r = mid - 1
            else: #mid is in r array
                # if target is in left side of r array or target is not in r array
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                # else, target is in r side of mid in r array
                    l = mid + 1
        return -1
            







