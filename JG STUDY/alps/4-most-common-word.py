# 54ms 13.8 MB
# https://leetcode.com/problems/most-common-word

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        blist = list("!?',;.")
        for b in blist:
            paragraph = paragraph.replace(b, ' ')

        max_value = 0
        word_set = {}

        for w in list(word for word in paragraph.lower().split() if word not in banned):
            if w in word_set:
                word_set[w] += 1
            else:
                word_set[w] = 1

            if max_value < word_set[w]:
                max_value = word_set[w]
                result = w

        return result