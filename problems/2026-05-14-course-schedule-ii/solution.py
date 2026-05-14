from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []

        preMap = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        safe = set()
        path = set()

        def dfs(course):
            if course in safe:
                return True

            if course in path:
                return False

            path.add(course)

            for prereq in preMap[course]:
                if dfs(prereq) == False:
                    return False

            path.remove(course)
            safe.add(course)
            order.append(course)

            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return []

        return order


def is_valid_order(num_courses, prerequisites, order):
    if len(order) != num_courses:
        return False
    position = {course: index for index, course in enumerate(order)}
    return all(position[prereq] < position[course] for course, prereq in prerequisites)


if __name__ == "__main__":
    s = Solution()

    order = s.findOrder(2, [[1, 0]])
    assert is_valid_order(2, [[1, 0]], order)

    assert s.findOrder(2, [[1, 0], [0, 1]]) == []

    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    order = s.findOrder(4, prerequisites)
    assert is_valid_order(4, prerequisites, order)

    order = s.findOrder(3, [])
    assert sorted(order) == [0, 1, 2]
