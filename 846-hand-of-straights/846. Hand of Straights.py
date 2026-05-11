class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        counts = Counter(hand)
        
        for key in counts:
            while counts[key] != 0:
                for i in range(groupSize):
                    if key+i in counts and counts[key+i] > 0:
                        counts[key+i] -= 1
                    else:
                        return False
        
        return True