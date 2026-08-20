class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        pos:  [1 4, 6]
        speed:[3, 2, 2]
        target = 10
        car1: dist = 9 -> 3h [3]
        car 2 dist = 10 - 4 = 6 -> dist/speed = 6/2 = 3h [3, 3]
        same time -> same fleet
        car 3 dist = 10 - 6, dist/speed = 4/2 = 2h [3, 3, ]
        """
        
        combined = sorted(zip(position, speed), reverse = True, key= lambda x:x[0])
        time = 0
        fleet = []
        for pos, sp in combined:
            time = (target - pos)/sp

            if not fleet or time > fleet[-1]:
                fleet.append(time)

        return len(fleet)
            
            

            