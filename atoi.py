
def myAtoi(s: str) -> int:
    s = s.lstrip(' ')
    postive = True
    if s.startswith('+'):
        s = s[1:]
    elif s.startswith('-'):
        postive = False
        # s = s[1:]
    if len(s) > 10:
        

    

