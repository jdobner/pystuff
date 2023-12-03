
def reverseI(num: int) -> int:
    new_num = 0
    sign = 1 if num > 0 else -1
    num = abs(num)
    while num > 0:
        digit = num % 10
        new_num = new_num * 10 + digit
        num = num // 10
    new_num = new_num * sign
    if new_num < -2 ** 31 or new_num >= 2 ** 31:
        new_num = 0
    return new_num 

def reverseS(num: int) -> int:
    str_num = str(num)
    if str_num[0] == '-':
        str_num = str_num[1:] + '-'
    str_num = str_num[::-1]
    num = int(str_num)
    if num < -2 ** 31 or num >= 2 ** 31:
        num = 0
    return num


class Solution:
    def reverse(self, num: int) -> int:
        return reverseS(num)

