# see https://leetcode.com/problems/integer-to-english-words/description/

map_ones = {'': '', '0': '', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four','5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}

map_tens = {'': '', '0': '', '2': 'Twenty', '3': 'Thirty', '4': 'Forty','5': 'Fifty', '6': 'Sixty', '7': 'Seventy', '8': 'Eighty', '9': 'Ninety'}
map_teens = {'10': 'Ten', '11': 'Eleven', '12': 'Twelve', '13': 'Thirteen', '14': 'Fourteen','15': 'Fifteen', '16': 'Sixteen', '17': 'Seventeen', '18': 'Eighteen', '19': 'Nineteen'}

suffixes = ['', 'Thousand', 'Million', 'Billion']
regex = r"^(\d{1,3})(\d{0,3})(\d{0,3})(\d?)$"

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        english_num_list = []
        print(f"num: {num}")
        num_str = str(num)[::-1]
        for i in range(len(suffixes)):
            local_list = []
            append_if_not_empty = lambda x: local_list.append(x) if len(x) > 0 else None
            next_three = num_str[i*3:(i+1)*3] 
            print(f"next_three: {next_three}")
            if len(next_three) == 0:
                break
            # print(next_three)
            
            if next_three[1:2] == '1': #teen
                local_list.append(map_teens[next_three[1::-1]])
            else:
                append_if_not_empty(map_ones[next_three[0:1]])
                append_if_not_empty(map_tens[next_three[1:2]])
                
            hundreds = map_ones[next_three[2:3]]
            if hundreds:
                local_list.append('Hundred')
                local_list.append(hundreds)
                
            if local_list:
                if suffixes[i]:
                    english_num_list.append(suffixes[i])
                english_num_list.extend(local_list)
        return " ".join(reversed(english_num_list))


def test(n):
    num_as_str = str(n)
    sol = Solution()
    print(num_as_str)
    print(sol.numberToWords(num_as_str))

if __name__ == "__main__":
    test(2 ** 31 - 1)
    test(12345)
    
    
                
                
                
                
                