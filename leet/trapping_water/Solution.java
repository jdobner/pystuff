package leet.trapping_water;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Stack;

class Solution {

    public int trap(int[] heights) {
        return trap2(heights);
    }

    private int trapIt(int[] heights) {
        var water = 0;
        
        int [] maxs = new int[heights.length];
        
        int maxHeight = 0;
        for (int i = maxs.length - 1; i >= 0; i--) {
            maxs[i] = maxHeight;
            maxHeight = Math.max(maxHeight, heights[i]);
        }
        //printArray(maxs);

        maxHeight = 0;
        for (int i = 0; i < heights.length - 1; i++) {
            int minHeight = Math.min(maxHeight, maxs[i]);
            int add = Math.max(minHeight - heights[i], 0);
            water += add;
            maxHeight = Math.max(maxHeight, heights[i]);
        }
        return water;
    }


    private int trap2(int[] heights) {
        var water = 0;
        var maxs = new ArrayDeque<Integer>();        
        int maxHeight = -1;
        for (int i = heights.length - 1; i >= 0; i--) {
            if (heights[i] > maxHeight) {
              maxs.offer(i);
              maxHeight = heights[i];
            }          
        }
        //printArray(maxs);

        maxHeight = 0;
        int nextMaxHPos = 0;
        int nextMaxHeight = 0;
        for (int i = 0; i < heights.length - 1; i++) {
            if (nextMaxHPos == i) {
                nextMaxHPos = maxs.poll();
                nextMaxHeight = heights[nextMaxHPos];
            }
            int minHeight = Math.min(maxHeight, nextMaxHeight);
            int add = Math.max(minHeight - heights[i], 0);
            water += add;
            maxHeight = Math.max(maxHeight, heights[i]);
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
        System.out.println(t);
        printArray(heights);

        // t += '\n';
        // for (int i : heights) {
        //     t += i;
        // }
        // System.out.println(t + "\n");

        var rv = s.trap(heights);
        System.out.println(rv);
    }

    private static void printArray(int[] a) {
        for (int i : a) {
            System.out.print(i);
        }
        System.out.println();
    }

    public static void main(String[] args) {
        test(new int[] {0,1,0,2,1,0,1,3,2,1,2,1});
        //test(new int[] {4,2,3});
    }

}