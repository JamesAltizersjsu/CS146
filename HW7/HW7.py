import heapq

def minMeetingRooms(intervals):
    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    
    # Initialize a min heap to track end times
    end_times = []
    
    for interval in intervals:
        if not end_times or end_times[0] <= interval[0]:
            # Assign a new server
            heapq.heappush(end_times, interval[1])
        else:
            # Reassign an existing server
            heapq.heappop(end_times)
            heapq.heappush(end_times, interval[1])
    
    return len(end_times)

# Example usage
intervals = [[1, 5], [2, 6], [3, 7], [4, 8]]
result = minMeetingRooms(intervals)
print(f"Minimum number of servers needed: {result}")
