# 책 참고: 91 ms 17.2 MB
# 그냥 풀었을 때: 1073 ms 17.1 MB
# 라이브러리를 사용하자 : (
# https://leetcode.com/problems/group-anagrams

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for str in strs:
            result[''.join(sorted(str))].append(str)

        return list(result.values())

#         rlist, result = [], []
#         for str in strs:
#             target = ''.join(sorted(str))
#             if not target in rlist:
#                 rlist.append(target)
#                 result.append([str])
#             else:
#                 result[rlist.index(target)].append(str)

#         return result

# groupAnagrams()
