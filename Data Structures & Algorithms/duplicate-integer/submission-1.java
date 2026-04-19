class Solution {
    public boolean hasDuplicate(int[] nums) {
        for (int i = 0; i < nums.length-1;i++){
            int compare = nums[i];
            for (int j = i+1; j < nums.length; j++){
                if (compare == nums[j])
                return true;
            }
        }
        return false;
    }
}
