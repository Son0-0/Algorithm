# https://leetcode.com/problems/minimum-height-trees
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        graph = [[] for _ in range(n)]
        
        # graph 만들기
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        # 하나만 연결된 노드 stack에 append
        stack = []
        for idx in range(n):
            if len(graph[idx]) == 1:
                stack.append(idx)

        while 2 < n:
            temp_list = []            
            for node in stack:
                n -= 1
                temp = graph[node].pop()
                graph[temp].remove(node)
                
                if len(graph[temp]) == 1:
                    temp_list.append(temp)
                    
            stack = temp_list
            
        return stack
