class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Make an array of cars
        cars = [{"pos": pos, "sp": sp} for pos, sp in zip(position, speed)]
        # Sort descending by position
        cars = sorted(cars, key=lambda x: x["pos"], reverse=True)
        eta_stack: list[float] = []

        for car in cars:
            eta = (target - car["pos"]) / car["sp"]
            # If car's ETA is larger than previous fleet's ETA, forms new fleet
            if len(eta_stack) == 0 or eta > eta_stack[-1]:
                eta_stack.append(eta)
            # Else it will join the previous fleet
        
        return len(eta_stack)
