class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Each task takes 1 unit of time
        # There must be at least 'n' units of time between two same tasks
        # Goal: Minimize total time (including idle time)

        # Count the frequency of each task
        count = Counter(tasks)

        # Use a max heap (invert count to negative for Python's min-heap)
        # Tasks with the highest frequency are scheduled first
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0  # Current time unit
        q = deque()  # Queue to hold tasks that are in cooldown
        # Each element in q is a pair: [remaining_count, ready_time]

        while maxHeap or q:
            time += 1  # Increment time by 1 unit

            if maxHeap:
                # Pop the task with highest remaining count
                cnt = 1 + heapq.heappop(maxHeap)  # Add 1 since counts are negative
                # If there are more of this task left
                if cnt:
                    # Add it to cooldown queue with the time when it can be re-added to heap
                    q.append([cnt, time + n])

            # If the task at the front of cooldown queue is ready to be scheduled again
            if q and q[0][1] == time:
                # Re-insert it into the heap for future scheduling
                heapq.heappush(maxHeap, q.popleft()[0])

        return time  # Total time taken to complete all tasks
