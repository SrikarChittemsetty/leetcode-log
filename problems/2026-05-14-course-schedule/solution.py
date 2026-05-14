from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}

        for course, prereq in prerequisites:
            if course not in preMap:
                preMap[course] = []
            preMap[course].append(prereq)

        safe = set()
        path = set()

        def dfs(course):
            if course in path:
                return False

            if course not in preMap or course in safe:
                return True

            path.add(course)

            for prereq in preMap[course]:
                if dfs(prereq) == False:
                    return False

            path.remove(course)
            safe.add(course)

            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    assert s.canFinish(2, [[1, 0]]) is True
    assert s.canFinish(2, [[1, 0], [0, 1]]) is False
    assert s.canFinish(4, [[2, 0], [2, 1], [3, 2]]) is True
