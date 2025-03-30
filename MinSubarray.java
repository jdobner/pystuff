class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        var left = 0;
        var len = nums.length;
        var smallest = len + 1;
        var current = 0;

        for (int right = 0; right < len; right++) {
            current += nums[right];
            while(current >= target && left <= right) {
                smallest = Math.min(smallest, right - left + 1);
                if (smallest == 1){
                    return 1;
                }
                current -= nums[left++];
                //left += 1
            }
        }
        return smallest > len ? 0 : smallest;
    }

    public static void main(String[] args) {
        System.out.println(new Solution().minSubArrayLen(7, new int[] {2,3,1,2,4,3}));
    }
}