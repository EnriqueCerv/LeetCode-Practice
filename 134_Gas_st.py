# %% 134 Gas station

def canCompleteCircuit(gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        gas = np.array(gas)
        cost = np.array(cost)
        next_station = gas - cost
        n = len(next_station)

        if (next_station >= 0).sum() == 0:
            return -1

        start_index = np.where(next_station == next_station.max())[0][0]
        
        delta = 0
        for i in range(n):
            index = (i+start_index)%n
            delta += next_station[index]
            if delta < 0:
                return -1
        return start_index
        
gas = [5,8,2,8] 
cost = [6,5,6,6]

# gas = [2,3,4]
# cost = [3,4,3]

canCompleteCircuit(gas, cost)

def canCompleteCircuit(gas, cost):
        ans = 0
        net = 0
        summ = 0

        # Try to start from each index.
        for i in range(len(gas)):
            net += gas[i] - cost[i]
            summ += gas[i] - cost[i]
            if summ < 0:
                summ = 0
                ans = i + 1  # Start from the next index.

        return -1 if net < 0 else ans