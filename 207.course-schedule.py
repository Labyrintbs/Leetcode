#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        indeg = [0 for _ in range(numCourses)]

        for cours in prerequisites:
            edges[cours[1]].append(cours[0])
            indeg[cours[0]] += 1  
        
        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])
        visited = 0
        while q:
            u = q.popleft()
            visited += 1
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        
        return visited == numCourses
        
# @lc code=end

