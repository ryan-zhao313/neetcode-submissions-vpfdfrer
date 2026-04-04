class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create an adjacency list
        adjList = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adjList[prereq].append(course)

        # create a list ot keep track of visits
        # not visited = 0, visiting = 1, visited = 2
        visited = [0] * numCourses

        # DFS to find out if there is a cycle in the courses or not
        def hasCycle(course):
            if visited[course] == 1:
                return True
            elif visited[course] == 2:
                return False

            visited[course] = 1

            for prereq in adjList[course]:
                if hasCycle(prereq):
                    return True

            visited[course] = 2
            return False

        
        for course in range(numCourses):
            if hasCycle(course):
                return False

        return True