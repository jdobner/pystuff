#!/usr/bin/env python3

# https://leetcode.com/problems/longest-substring-without-repeating-characters/



def lengthOfLongestSubstring1(self, s: str) -> int:
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

def lengthOfLongestSubstring2(s: str) -> int:
    longest = 0
    left = 0
    positions = [-1] * 256
    for i in range(len(s)):
        c = ord(s[i])
        pos = positions[c]
        positions[c] = i
        if pos < left:
            longest = max(longest, i - left + 1)
            # print(left, i, pos, s[left:i+1], positions)
        else:
            left = pos + 1
            # print('else')
    return longest
    

def lengthOfLongestSubstring3(self, s: str) -> int:
    longest = 0
    left = 0
    positions = [-1] * 256
    for i, c  in enumerate(ord(ch) for ch in s):
        pos = positions[c]
        positions[c] = i
        if pos < left:
            longest = max(longest, i - left + 1)
            # print(left, i, pos, s[left:i+1], positions)
        else:
            left = pos + 1
            # print('else')
    return longest


def lengthOfLongestSubstring(self, s: str) -> int:
    return self.lengthOfLongestSubstring3(s)

if __name__ == "__main__":
    main()
