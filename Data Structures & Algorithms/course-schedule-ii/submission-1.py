class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preMap = {c: [] for c in range(numCourses)}
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited, completed = set(), set()

        output = []

        def dfs(crs):
            if crs in visited:
                return False
            if crs in completed:
                return True
            visited.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
                
            visited.remove(crs)
            completed.add(crs)
            output.append(crs)
            return True
        

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return output

                

        

    