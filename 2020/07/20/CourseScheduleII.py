'''
210. Course Schedule II - Medium
https://leetcode.com/problems/course-schedule-ii/

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have
to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return
the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them.
If it is impossible to finish all courses, return an empty array.
'''
def find_order(num_courses, prerequisites):
    '''
    visited = [False] * num_courses
    taken = visited
    prereq_hash_table = {}
    class_order = []

    for edge in prerequisites:
        if edge[0] in prereq_hash_table:
            prereq_hash_table[edge[0]] += [edge[1]]
        else:
            prereq_hash_table[edge[0]] = [edge[1]]

    print(prereq_hash_table)

    def top_sort(node, visited, stack):
        visited[node] = True
        print('looking at node={}; visited:{}'.format(node,visited))
        if node in prereq_hash_table:
            for prereq in prereq_hash_table[node]:
                if not visited[prereq]:
                    top_sort(prereq, visited, stack)

        stack.append(node)
        print('c_o: {}'.format(class_order))
        print('stack: {}'.format(stack))

    for course in range(num_courses):
        if not visited[course]:
            top_sort(course, visited, class_order)

    #print(class_order)
    return class_order
    '''
    from collections import defaultdict
    prereq_count_by_course, successor_courses_by_course = defaultdict(int), defaultdict(list)
    for course, requires in prerequisites:
        prereq_count_by_course[course] += 1
        successor_courses_by_course[requires].append(course)
    print(set(range(num_courses)))
    print('pre->{}'.format(prereq_count_by_course))
    print('suc->{}'.format(successor_courses_by_course))
    print(set(prereq_count_by_course))
    free = set(range(num_courses)) - set(prereq_count_by_course)
    print('free->{}'.format(free))
    class_order = []
    while free:
        free_course = free.pop()
        class_order.append(free_course)
        for successor_course in successor_courses_by_course[free_course]:
            prereq_count_by_course[successor_course] -= 1
            prereq_count_by_course[successor_course] or free.add(successor_course) # pylint: disable=redefined-builtin
    return class_order * (len(class_order) == num_courses)

print('ANS->{}'.format(find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]])))
print('ANS->{}'.format(find_order(2, [[0, 1]])))
print('ANS->{}'.format(find_order(2, [[0, 1], [1, 0]])))
print('ANS->{}'.format(find_order(7, [[2, 1], [6, 5], [6, 3], [5, 1], [5, 0], [4, 5]])))
