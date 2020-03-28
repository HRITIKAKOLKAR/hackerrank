"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
"""
import string
def swap_case(s):
    #for i in range(0,len(s)):
    #    w[i]=s[i].swapcase()
    #return str([lambda s[i]:s[i].swapcase() for i in range(0,len(s))])
    return ''.join([i.swapcase() for i in s])
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
