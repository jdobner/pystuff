package leet.simplifypath;


class Solution {
    public String simplifyPath(String path) {
        var paths = path.split("/");

        for (var i = 0; i < paths.length; i++) {
            var thePath = paths[i];
            if(thePath.equals("..")) {
                paths[i] = "";
                for (var n = i - 1; n >= 0; n--) {
                    if (paths[n].length() > 0) {
                        paths[n] = "";
                        break;
                    }
                }
            } else if (thePath.equals(".")) {
                paths[i] = "";
            } 
        }
        var newPath = new StringBuilder();
        for (String thePath : paths) {
            if (thePath.length() > 0) {
                newPath.append('/');
                newPath.append(thePath);
            }        
        }
        return newPath.length() > 0 ? newPath.toString() : "/";
    }

    void test(String path) {
        var result = simplifyPath(path);
        System.out.println(path + ": " + result);
    }
    public static void main(String[] args) {
        var s = new Solution();
        s.test("/home/");
        s.test("/.../a/../b/c/../d/./");
        s.test("/a/./b/../../c/");
    }

}