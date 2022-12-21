# see https://leetcode.com/problems/integer-to-english-words/description/

ones = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
tens = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']



map_teens = {'10': 'Ten', '11': 'Eleven', '12': 'Twelve', '13': 'Thirteen', '14': 'Fourteen','15': 'Fifteen', '16': 'Sixteen', '17': 'Seventeen', '18': 'Eighteen', '19': 'Nineteen'}

suffixes = ['', 'Thousand', 'Million', 'Billion']
regex = r"^(\d{1,3})(\d{0,3})(\d{0,3})(\d?)$"

class Solution:
    
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        english_num_list = []
        print(f"num: {num}")
        for i in range(len(suffixes)):
            if num == 0:
                break
            local_list = []
            one = num % 10
            num //= 10
            ten = num % 10
            num //= 10
            hundred = num % 10
            num //= 10            
            
            if ten == 1: 
                local_list.append(teens[one])
            else:
                if one: 
                    local_list.append(ones[one - 1])
                if ten:
                    local_list.append(tens[ten - 1])
                
            if hundred:
                local_list.append('Hundred')
                local_list.append(ones[hundred - 1])
                
            if local_list:
                if suffixes[i]:
                    english_num_list.append(suffixes[i])
                english_num_list.extend(local_list)
        return " ".join(reversed(english_num_list))


def test(n):
    sol = Solution()
    print(n)
    print(sol.numberToWords(n))

if __name__ == "__main__":
    test(2 ** 31 - 1)
    test(12345)
    
    
                
                
                
                
                