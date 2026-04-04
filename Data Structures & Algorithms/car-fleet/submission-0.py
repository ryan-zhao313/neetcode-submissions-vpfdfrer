class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # first zip the position and speed of the cars
        cars = [(p, s) for p, s in zip(position, speed)]
        
        #sort the cars in reverse order
        cars.sort(reverse=True)

        stack = []
        for p, s in cars:
            # calculate the time taken to reach the target
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)