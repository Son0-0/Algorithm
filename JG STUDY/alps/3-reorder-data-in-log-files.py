# 49ms 14MB
# https://leetcode.com/problems/reorder-data-in-log-files

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        result = []
        llist, llist_ord = [], []
        dlist, dlist_ord = [], []
        
        for idx, log in enumerate(logs):
            temp = log.split()
            if temp[1].isdigit():
                dlist.append(log)
                dlist_ord.append((idx, temp[1:]))
            else:
                llist.append(log)
                llist_ord.append((idx, temp[0], temp[1:]))

        llist_ord.sort(key = lambda x:(x[2], x[1]))

        for data in llist_ord:
            result.append(logs[data[0]])
        for idx, num in dlist_ord: 
            result.append(logs[idx])
        
        return result