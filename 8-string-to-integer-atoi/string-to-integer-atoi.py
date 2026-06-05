class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n=len(s)
        while i<n and s[i]==" ":
            i+=1
        sign = 1
        if i<n and s[i]=="-":
            sign = -1
            i+=1
        elif i<n and s[i]=="+":
            i+=1
        num = 0
        while i<n and s[i].isdigit():
            num = num*10 + int(s[i])
            i+=1
        num = num*sign
        int_max = 2147483647
        int_min = -2147483648
        if num > int_max:
            return int_max
        if num < int_min:
            return int_min
        return num
        