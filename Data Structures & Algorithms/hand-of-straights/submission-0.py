class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        
        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]

            #can we create a group starting first ele of size groupSize
            for i in range(first, first + groupSize):
                #False 1
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    #False 2
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        #True 1
        return True
        # O(n*logn)

