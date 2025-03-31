package leet.min_win_substring_v2;

class Solution {
    public String minWindow(String s, String t) {
        var arr = new int['z' + 1];
        //int ayy = 'A';
        for (char c : t.toCharArray()) {
            arr[c]++;
        }
        var target = t.length();
        var minLen = s.length() + 1;
        var substring = "";

        if (target >= minLen) {
            return "";
        }

        var left = 0;
        for (var right = 0; right < s.length(); right++) {
            //int index = s.charAt(right) - ayy;
            if (--arr[s.charAt(right)] >= 0) {
                target--;
            }
            if (target == 0) {
                for (; target == 0; left++) {
                    //int index2 = s.charAt(left) - ayy;
                    if (++arr[s.charAt(left)] > 0) {
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

    void test(String s, String t, String r) {
        assert this.minWindow(s, t) == r;
        System.out.println(s + ", " + t + " = " + r);
    }

    public static void main(String[] args) {
        var s = new Solution();
        s.test("ADOBECODEBANC", "ABC", "BANC");
        
    }
}