class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic, t_dic = {}, {}
        
        for i in s:
            s_dic[i] = (s_dic[i] + 1 if i in s_dic else 1)

        for i in t:
            t_dic[i] = (t_dic[i] + 1 if i in t_dic else 1)

        # for n in s:
        #     if n in s_dic:
        #         s_dic[n] += 1
        #     else:
        #         s_dic[n] = 1

        # for n in t:
        #     if n in t_dic:
        #         t_dic[n] += 1
        #     else:
        #         t_dic[n] = 1

        return s_dic == t_dic