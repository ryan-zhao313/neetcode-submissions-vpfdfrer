class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        start = 0
        diff = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            diff += gas[i] - cost[i]

            if tank < 0:
                tank = 0
                start = i + 1
            
        if diff < 0:
            return -1
        else:
            return start