package leet.simplifypath;


class Solution {
    public String simplifyPath(String path) {
        var paths = path.split("/");
        var paths2 = new String[paths.length];
        var i = 0;
        for (String thePath : paths) {
            if(thePath.equals("..")) {
                i = Math.max(0, i - 1);
            } else if (thePath.length() > 0 && !thePath.equals(".")) {
                paths2[i++] = thePath;
            }
        }
        var newPath = new StringBuilder();
        for (int n = 0; n < i; n++) {
            newPath.append('/');
            newPath.append(paths2[n]);
        }
        return newPath.length() > 0 ? newPath.toString() : "/";
    }

    public static void main(String[] args) {
        System.out.println(new Solution().simplifyPath("/home/"));
    }

}