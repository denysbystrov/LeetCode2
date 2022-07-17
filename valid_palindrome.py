"""Number 125: Valid Palidrome"""


def is_palidrome(s: str) -> bool:
    left = 0
    right = len(s)-1
    while left < right:
        l_al_num = s[left].isalnum()
        r_al_num = s[right].isalnum()
        if l_al_num and r_al_num:
            if s[left].upper() != s[right].upper():
                return False
            left += 1
            right -= 1
        else:
            if not l_al_num:
                left += 1
            if not r_al_num:
                right -= 1

    return True

