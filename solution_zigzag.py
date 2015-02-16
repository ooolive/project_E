#coding=utf-8

import math

#class Solution:
    #def convert(self, text, nrows):
        #len_src = len(text)
        #len_smallcol, len_largecol = 0, 0
        #num_largecol, num_smallcol = int(math.floor(nrows/2.0)), int(math.ceil(nrows/2.0))
        #len_smallcol = int(math.ceil((len_src + num_largecol) / float(2 * num_largecol + num_smallcol)))
        #len_largecol = 2 * len_smallcol - 1

        #ret = ''
        #cursmall = True
        #for col in xrange(nrows):
            #cursmall = (col % 2 == 0)
            #len_c = len_smallcol if cursmall else len_largecol
            #for ch in xrange(len_c):
                #if cursmall:
                    #idx = col + ch * (nrows+num_largecol)
                #else:
                    #idx = col + ch * (num_largecol+1)
                #if idx < len_src:
                    #ret += text[idx]
        #return ret

# 上面那个 Solution 把 zig-zag 理解错了
# 2333
# 于是借鉴了 discussion 某人的 idea
# 有了下面这个巨慢的 Solution

class Solution_initial:
    def convert(self, text, nrows):
        if nrows == 1:
            return text

        ret = [ '' for i in xrange(nrows) ]
        facr = nrows - 1
        facp = 2 * facr

        for ch, c in enumerate(text):
            n_pass = ch / facp
            cur_pass_mid = n_pass * facp + facr
            cur_col = facr - abs(ch - cur_pass_mid)
            ret[cur_col] += c

        return ''.join(ret)

# second 速度还可以，比上面的快一点
# 但是貌似还是稍微复杂
# 这个在 discussion 里面也找到撞的了

class Solution_second:
    def convert(self, text, nrows):
        ltext = len(text)
        if nrows == 1:
            return text

        ret = ''

        facr = nrows - 1
        facp = 2 * facr
        npass = int(math.ceil(len(text)/float(facp)))

        for p in xrange(npass):
            ret += text[p*facp]

        for row in xrange(1, nrows-1):
            for p in xrange(npass):
                n_se = p * facp + row
                if n_se < ltext:
                    ret += text[n_se]
                n_se = 2*nrows - row - 2 + p*facp
                if n_se < ltext:
                    ret += text[n_se]

        for p in xrange(npass):
            n_se = p * facp + facr
            if n_se < ltext:
                ret += text[n_se]

        return ret

# https://oj.leetcode.com/discuss/14483/share-simple-c-solution
# 类似 initial，利用 step，不知比 initial 高到哪里去
class Solution:
    def convert(self, text, nrows):
        if nrows <= 1:
            return text

        ltext = len(text)
        ret = ['' for i in xrange(nrows)]

        row, step = 0, 1
        for c in text:
            ret[row] += c

            if row == 0:
                step = 1
            elif row == nrows-1:
                step = -1

            row += step

        return ''.join(ret)

# 这道题特么花了我半天...
# 没基础啊...

sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))
print(sol.convert("A", 1))
print(sol.convert("ABC", 2))
