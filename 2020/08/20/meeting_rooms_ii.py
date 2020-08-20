class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        if not meeting_times: return 0

        dynamic_sol = [1] * len(meeting_times)
        meeting_times.sort(key=lambda meets: meets[0])
        print(meeting_times)
        
        def sort_by_start_time(meeting_times):
            sorted(meeting_times, key=lambda meets: meets[0])
            #pass
            
        def cycle(startt, offset, up_to):
            all_prev = [False] * offset
            for i in range(offset, 0, -1): # O(offset)
                print('{}<{}'.format(meeting_times[up_to-offset][1], startt))
                all_prev[offset-i] = startt > meeting_times[up_to-offset][1]
            print(all_prev)
            return any(all_prev)
            
        #sort_by_start_time(meeting_times) # O(nlogn) | n -> len(meeting_times), timsort
        # meeting_times = sort_by_start_time(meeting_times)
        mt_len = len(meeting_times)
        for i in range(1, mt_len): # O(MT) | MT -> len(meeting_times)
            start, end = meeting_times[i]
            prev_start, prev_end = meeting_times[i-1]
            look_back = dynamic_sol[i-1]
            look_back_ongoing = not look_back or cycle(start, look_back, i)
            print(look_back_ongoing,i)
            if look_back_ongoing and prev_start <= start < prev_end:
                dynamic_sol[i] += dynamic_sol[i-1]
            else:
                dynamic_sol[i] = dynamic_sol[i-1]
                
        print(dynamic_sol)
        return dynamic_sol[-1]
        '''
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)

        e = 0
        numRooms = available = 0
        for start in starts:
            while ends[e] <= start:
                available += 1
                e += 1
            if available:
                available -= 1
            else:
                numRooms += 1

        return numRooms