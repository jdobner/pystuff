from typing import List

def paren(left: int, right: int, curr: str, res: List[str]):
    # 'evaluate current string
    # if we are out of brackets to add, we must be at a valid string
    if left == 0 and right == 0:
        res.append(curr)
        return

    # recursive call: add either open or close
    # if adding open bracket is valid
    if left > 0:
        # add open bracket, decr count
        paren(left-1, right, curr + "(", res)

    # if adding close bracket is valid
    if right > left:
        # add close bracket, decr count
        paren(left, right-1, curr + ")", res)

    return res


if __name__ == "__main__":
    n = 2
    res = paren(n, n, '', [])
    print(res)