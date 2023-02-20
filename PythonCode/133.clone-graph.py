#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        dic = {}
        def dfs(node):
            if not node: return
            elif node in dic: return dic[node]
            clone = Node(node.val)
            dic[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            return clone

        def bfs(node):
            '''
            if not node:return
            queue = []
            clone = Node(node.val)
            dic[node] = clone
            queue.append(node)
            while queue:
                temp = queue.pop(0)
                for n in temp.neighbors:
                    if not n in dic:
                        dic[n] = Node(n.val)
                        queue.append(n)
                    dic[temp].neighbors.append(dic[n])
            return clone
            '''
            if not node:return node
            queue, clones = [node], {node.val : Node(node.val)}
            while queue:
                cur = queue.pop(0)
                cur_clone = clones[cur.val]
                for n in cur.neighbors:
                    if not n.val in clones:
                        clones[n.val] = Node(n.val)
                        queue.append(n)
                    cur_clone.neighbors.append(clones[n.val])
            return clones[node.val]
            '''
            if not node: return node
        
            q, clones = deque([node]), {node.val: Node(node.val, [])}
            while q:
                cur = q.popleft() 
                cur_clone = clones[cur.val]            

                for ngbr in cur.neighbors:
                    if ngbr.val not in clones:
                        clones[ngbr.val] = Node(ngbr.val, [])
                        q.append(ngbr)
                        
                    cur_clone.neighbors.append(clones[ngbr.val])
                    
            return clones[node.val]
            '''

        
        return bfs(node)

        
# @lc code=end

