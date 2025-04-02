import java.util.LinkedList;
import java.util.List;
import static java.lang.String.format;

class Solution {


    public List<String> fullJustify(String[] words, int maxWidth) {
        var results = new LinkedList<String>();
        int right = 0;

        while(right < words.length) {
            int left = right;
            var buffer = new StringBuffer(maxWidth);
            int size = 0;
            int gaps = 0;

            while (right < words.length) {
                int space = size == 0 ? 0 : 1;
                int nextWordSize = words[right].length();
                if (size + gaps + space + nextWordSize <= maxWidth) {
                    right++;
                    size += nextWordSize;
                    gaps += space;
                } else {
                    break;
                }
            }
            var leftJustify = (right == words.length|| gaps == 0);
            int extraSpace = maxWidth - size;
            int spacesPerWord = leftJustify ? 1 : extraSpace / gaps;
            int remaining = leftJustify ? 0 : extraSpace % gaps;
            int i = left;
            for (; i < right; i++) {
                if (i > left) {
                    int spaces = spacesPerWord + (remaining-- > 0 ? 1 : 0);
                    buffer.append(" ".repeat(spaces));
                }
                buffer.append(words[i]);
            }
            if (leftJustify) {
                int padding = maxWidth - (size + gaps);
                buffer.append(" ".repeat(padding));
            }
            var line = buffer.toString();
            // assert line.length() == maxWidth : 
            //     format("len: %d, maxWidth: %d line: %s%s", line.length(), maxWidth, line, "|");
            results.add(line);
        }
        //printResults(maxWidth, results);
        return results;
        
    }

    public static List<String> test(String[] words, int maxWidth) {
        var s = new Solution();
        var results = s.fullJustify(words, maxWidth);
        return results;
    }

    private static void printResults(int maxWidth, List<String> results) {
        for (int i = 0; i < maxWidth; i++) {
            System.out.print(i % 10);
        }
        System.out.println();
        for (String string : results) {
            System.out.println(string + "|");
        }
    }

    public static void main(String[] args) {
        test(new String[]{"This", "is", "an", "example", "of", "text", "justification."}, 16);
        test(new String[]{"This", "is", "an", "example", "of", "text", "justi fy."}, 16);
        test(new String[]{"This", "is", "an", "example", "of", "text", "justification,", "aha!"}, 16);
        
    }

}
