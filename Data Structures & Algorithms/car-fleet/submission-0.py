class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)]
        stack = []
        for p, s in sorted(pair)[::-1]: # Reverse sorted order
            #because we wont know whether the car from front order
            # will reach the element in the other place
            # Get the time it reaches the end
            stack.append((target - p) / s)
            #Does it overlap with other element
            #If the top car collides with the seconds car
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)