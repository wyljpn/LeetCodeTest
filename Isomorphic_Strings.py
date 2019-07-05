class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 把每个字符的值当成dict的key,val是其下标的集合
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            # dict.get(key, default=None)
            # 如果dict中有存在key,则返回指定key的值；否则返回[]
            d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        # 需要使用sorted来重新产生一个List进行比较。
        # 如果直接比较dict.values()（返回Object），即使print出来的值看上去相等，返回值却是False。
        return sorted(d1.values()) == sorted(d2.values())

    # 建立s到t的双向映射。如果d1中v对应的值与w不同，则说明构造不相同；d2同理。
    def isIsomorphic_2(self, s, t):
        d1, d2 = {}, {}
        for v, w in zip(s, t):
            if (v in d1 and d1[v] != w) or (w in d2 and d2[w] != v):
                return False
            d1[v], d2[w] = w, v
        return True


s = "avab"
t = "cvcc"
so = Solution()
res = so.isIsomorphic(s, t)
print(res)
