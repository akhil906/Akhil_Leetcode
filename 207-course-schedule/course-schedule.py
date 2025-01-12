class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        g = defaultdict(list)

        for a,b in prerequisites:
            g[a].append(b)
        

        unvisited = 0
        visiting = 1
        visited = 2


        states = [0]*numCourses

        def dfs(node):

            if states[node] == 1:
                return False
            elif states[node] == 2:
                return True
            
            states[node] = visiting

            for nei in g[node]:
                if not dfs(nei):
                    return False
 
            

            states[node] = visited
            return True

        
        for i in range(numCourses):
                if not dfs(i):
                    return False
        
        return True
            




        