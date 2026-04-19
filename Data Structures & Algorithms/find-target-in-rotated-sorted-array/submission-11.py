class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        lowestVal = nums[0]
        pivotIndex = 0
        while l <= r:
            if nums[l] <= nums[r]:
                if nums[l] <= lowestVal:
                    lowestVal = nums[l]
                    pivotIndex = l
                break
            mid = (l + r) // 2
            if nums[mid] < lowestVal:
                lowestVal = nums[mid]
                pivotIndex = mid

            if nums[l] <= nums[mid]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid - 1
        offset = 0
        if target >= nums[0] and pivotIndex != 0:
            arr = nums[0:pivotIndex]
        else:
            arr = nums[pivotIndex:]
            offset = pivotIndex
        print(pivotIndex)
        print(arr)
        l, r = 0, len(arr)-1
        while l <= r:
            mid = (l + r) // 2
            if target == arr[mid]:
                return mid + offset
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1









