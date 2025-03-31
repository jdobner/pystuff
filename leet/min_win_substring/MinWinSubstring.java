package leet.min_win_substring;

import java.util.HashMap;

class Solution {
    public String minWindow(String s, String t) {
        var map = new HashMap<Character, Integer>(); 
        var target = t.length();
        var minLen = s.length() + 1;
        var substring = "";

        for (char c : t.toCharArray()) {
            var rv = map.putIfAbsent(c, 1);
            if (rv != null) {
                map.put(c, ++rv);
            }
        }

        var left = 0;
        for (var right = 0; right < s.length(); right++) {
            
            var r = map.computeIfPresent(s.charAt(right), (k, v) -> --v);
            if (r == null) {
                continue;
            } else if (r >= 0) {
                target--;
            }
            if (target == 0) {
                for (; target == 0; left++) {
                    r = map.computeIfPresent(s.charAt(left), (k, v) -> ++v);
                    if (r > 0) {
                        target++;
                        var len = right - left + 1;
                        if (len < minLen) {
                            minLen = len;
                            substring = s.substring(left, right + 1);
                        }
                    }
                }
            }
        }
        return substring;
    }
}