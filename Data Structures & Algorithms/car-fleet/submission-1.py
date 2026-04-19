class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [] # [position, speed]
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        cars.sort()
        currTime = 0 #arrival time of current fleet
        fleetNum = 0
        print(cars)
        for car in reversed(cars):
            time=(target-car[0])/car[1] #time of arrival = target - pos // speed
            if time > currTime: # if next car slower, never catches up, creates new fleet
                fleetNum += 1
                currTime = time
            #else, car catches up or arrives at same time and joins current fleet
        return fleetNum
                