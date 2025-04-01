package leet.trapping_water;

import java.util.Arrays;

class Solution {

    public int trap(int[] heights) {
        return trap2(heights);
    }

    private int trap2(int[] heights) {
        var water = 0;
        var sorted = new int[heights.length][];
        
        for (int i = 0; i < heights.length; i++) {
            sorted[i] = new int[]{heights[i], i};
        }

        Arrays.sort(sorted, (v1, v2)->{
            var diff = v1[0] - v2[0];
            return diff != 0 ? diff : v1[1] - v2[1]; 
        });

        int c = 0;
        var left = sorted
        while (c > sorted.length - 1) {
            var left = sorted[c];
            var right = sorted[++c];
            if (left[1] > right[1]) {
                var tmp = left;
                left = right;
                right = tmp;
            }
            int height = Math.min(left[0], right[0]);
            for(int i = left[1] + 1; i < right[1]; i++ ) {
                int amount = height - heights[i];
                water += amount;
                System.out.printf("left: %d, i: %d,  ");
                sorted[i] = null;
            }
        }

        return water;

    }

    private int trap1(int[] heights) {
        var water = 0;
        var left = 0;
        var maxHeight = 0;
        
        while(left < heights.length - 1) {
            var right = left + 1;
            for (var i = right; i < heights.length - 1 && heights[i] < heights[left]; i++) {
                
            }
            int height = Math.min(heights[left], heights[right]);
            System.out.println("left: " + left + ", right:" + right + ", height: " + height);
            for (int i = left + 1; i < right; i++) {
                var add = Math.max(0, height - heights[i]);
                water += add;
                System.out.println("add water pos: " + i + ", amount: " + add + ", total: " + water);
            }
            left = right;
        }
        return water;

    }

    public static void main(String[] args) {
        var s = new Solution();
        var rv = s.trap(new int[] {0,1,0,2,1,0,1,3,2,1,2,1});
        System.out.println(rv);
    }

}