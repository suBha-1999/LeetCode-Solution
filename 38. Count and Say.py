class Solution:
    def countAndSay(self, n: int) -> str:
        if(n==1):
            return '1'
        def RLE(s):
            nn=len(s)
            res=''
            cur_char=s[0]
            cur_char_freq=1
            for i in s[1:]:
                if(i==cur_char):
                    cur_char_freq+=1
                else:
                    res+=f"{cur_char_freq}{cur_char}"
                    cur_char=i
                    cur_char_freq=1
            res+=f"{cur_char_freq}{cur_char}"
            return res
        s='1'
        for i in range(n-1):
            s=RLE(s)
        return s

sol = Solution()
n = 4
res = sol.countAndSay(n)
print(res)