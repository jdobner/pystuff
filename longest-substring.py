#!/usr/bin/env python3

# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def main():
    print(lengthOfLongestSubstring("abcabcbb"))

    def lengthOfLongestSubstring(s: str) -> int:
        longest = 0
        left = 0
        positions = {}
        for i in range(len(s)):
            c = s[i]
            pos = positions.get(c, -1)
            positions[c] = i
            if pos < left:
                longest = max(longest, i - left + 1)
                # print(left, i, pos, s[left:i+1], positions)
            else:
                left = pos + 1
                # print('else')
        return longest



if __name__ == "__main__":
    main()
