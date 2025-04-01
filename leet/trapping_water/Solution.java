package leet.trapping_water;

import java.util.Arrays;

class Solution {

    public int trap(int[] heights) {
        return trapIt(heights);
    }

    private int trapIt(int[] heights) {
        var water = 0;
        
        int [] maxs = new int[heights.length];
        
        int maxHeight = 0;
        for (int i = maxs.length - 1; i >= 0; i--) {
            maxs[i] = maxHeight;
            maxHeight = Math.max(maxHeight, heights[i]);
        }

        maxHeight = 0;
        for (int i = 0; i < heights.length - 1; i++) {
            int minHeight = Math.min(maxHeight, maxs[i]);
            int add = Math.max(heights[i] - minHeight, 0);
            water += add;
            maxHeight = Math.max(maxHeight, heights[i]);
        }
        return water;
    }


    private int trap1(int[] heights) {
        var water = 0;
        var left = 0;
        
        while(left < heights.length - 1) {
            var rightCandidate = left;
            var right = 0;
            while (++rightCandidate < heights.length) {
                if (heights[rightCandidate] <= heights[left]) {
                    right = rightCandidate;
                    break;
                } else if (right == 0 || heights[rightCandidate] > heights[right]) {
                    right = rightCandidate;
                }
            }
            
            int height = Math.min(heights[left], heights[right]);
            System.out.println("left: " + left + ", right:" + right + ", height: " + height);
            for (int i = left + 1; i < right; i++) {
                var add = Math.max(0, height - heights[i]);
                water += add;
                System.out.printf("add water pos: %d, amount: %d, total: %d\n", i, add, water);
            }
            left = right;
        }
        return water;

    }

    public static void test(int[] heights) {
        var s = new Solution();
        var t = "";
        for (int i = 0; i < heights.length; i++) {
            if(t.length() > 0) t+= ", ";
            t += i + ":" + heights[i];
        }
        System.out.println(t + "\n");

        t = "";
        int max = Arrays.stream(heights).max().orElseThrow();
        for (int i = max; i > 0; i--) {
            for (int h : heights) {
                t += (h >= i ? "X" : " ");
            }
            t += '\n';
        }
        for (int i = 0; i < heights.length; i++) {
            t+= i % 10;
        }
        t += '\n';
        for (int i : heights) {
            t += i;
        }
        System.out.println(t + "\n");

        var rv = s.trap(heights);
        System.out.println(rv);
    }

    public static void main(String[] args) {
        test(new int[] {0,1,0,2,1,0,1,3,2,1,2,1});
    }

}