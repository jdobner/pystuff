package leet.min_win_substring_v2;

class Solution {
    public String minWindow(String s, String t) {
        var arr = new int['z' - 'A' + 1];
        int ayy = 'A';
        for (char c : t.toCharArray()) {
            arr[c - ayy]++;
        }
        var target = t.length();
        var minLen = s.length() + 1;
        var substring = "";

        if (target >= minLen) {
            return "";
        }

        var left = 0;
        for (var right = 0; right < s.length(); right++) {
            int index = s.charAt(right) - ayy;
            if (--arr[index] >= 0) {
                target--;
            }
            if (target == 0) {
                for (; target == 0; left++) {
                    int index2 = s.charAt(left) - ayy;
                    if (++arr[index2] > 0) {
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
        var result = this.minWindow(s, t);
        System.out.println(s + ", " + t + " = " + result);
        assert result.equals(r);
    }

    public static void main(String[] args) {
        var s = new Solution();
        s.test("ADOBECODEBANC", "ABC", "BANC");
        
    }
}