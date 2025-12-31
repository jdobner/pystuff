#!/usr/bin/env python3

## zig zag conversion of a string
## https://leetcode.com/problems/zigzag-conversion/

import io


def _convert(s: str, numRows: int) -> str:
   p2p = numRows * 2 - min(numRows, 2)
   result = io.StringIO()
   for cr in range(numRows):
      cursor = cr
      while cursor < len(s):
         result.write(s[cursor])
         print(result.getvalue())
         if (cursor - cr) % p2p == 0:
            # =IF(E9 < Height - 1, (Height -E9  - 1) * 2, P2P) 
            if cr < numRows - 1:
               cursor += (numRows - cr - 1) * 2  
            else: 
               cursor += p2p
         else:
            cursor += p2p - ((numRows - cr - 1) * 2 )
         # print(f"{cursor=}")
   return result.getvalue()

def _convertList(s : list, numRows: int) -> str:
   p2p = numRows * 2 - min(numRows, 2)
   result = [] 

   for cr in range(numRows):
      cursor = cr
      while cursor < len(s):
         result.append(cursor)
         print(result)
         if (cursor - cr) % p2p == 0:
            # =IF(E9 < Height - 1, (Height -E9  - 1) * 2, P2P) 
            if cr < numRows - 1:
               cursor += (numRows - cr - 1) * 2  
            else: 
               cursor += p2p
         else:
            cursor += p2p - ((numRows - cr - 1) * 2 )
         print(f"{cursor=}")

   
def main():
    print(_convert('PAYPALISHIRING', 3))
    #print(_convertList([i for i in range(21)], 5))


if __name__ == "__main__":
    main()