class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        ## Initialization
        output = []
        q = collections.deque()  # Monotonic decreasing queue (stores indices)
        l = r = 0  # Left and right pointers for the sliding window

        ## Sliding window expansion
        while r < len(nums):
            # Maintain monotonic queue by removing smaller values from the back
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # Remove elements that are outside the current window (outdated indices)
            if l > q[0]:
                q.popleft()

            # Start recording results when the window reaches size k for the first time
            if (r + 1) >= k:
                output.append(nums[q[0]])  # Append the max of the current window
                l += 1  # Move left pointer to slide the window forward
            
            # Move right pointer to expand the window
            r += 1

        return output