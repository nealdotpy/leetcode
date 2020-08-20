class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # will sort in ascending order by first element
        points.sort(key=lambda point: point[0]) # timsort -> O(PL log PL), merge+quick

        def merge_intervals(points):
            pts_len = len(points) # PL
            i = 1
            while i < pts_len: # O(PL)
                start, end = points[i]
                prev_start, prev_end = points[i-1]
                contained_in_prev_interval = prev_start <= start <= prev_end
                if contained_in_prev_interval:
                    # how do we merge, now that we know we need to merge?
                    # take max(starts), min(ends)
                    max_of_starts = max(prev_start, start)
                    min_of_ends = min(prev_end, end)
                    points[i] = [max_of_starts, min_of_ends]
                    del points[i-1]
                    pts_len -= 1
                else:
                    i += 1

        merge_intervals(points) # O(PL)
        return len(points)