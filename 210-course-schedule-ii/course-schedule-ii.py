class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        g = defaultdict(list)
        order = []

        for a,b in prerequisites:
            g[a].append(b)

        
        unvisited = 0
        visiting = 1
        visited = 2

        states = [unvisited] * numCourses

        def dfs(i): #return True - if no cycle, False - if Cycle
            if states[i] == visiting:
                return False
            elif states[i] == visited:
                return True
            
            states[i] = visiting

            for neighbours in g[i]: #checking prereq of this courses
                if not dfs(neighbours):
                    return False
            
            states[i] = visited
            order.append(i)
            return True
        

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order
    