class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dire = deque()
        radiant = deque()
        for i in range(len(senate)):
            if senate[i] =='R':
                radiant.append(i)
            else:
                dire.append(i)
        rounds = len(senate) - 1
        while dire and radiant:
            rounds += 1
            if dire[0] < radiant[0]:
                dire.append(rounds)
            else:
                radiant.append(rounds)
            dire.popleft()
            radiant.popleft()
        if len(radiant) > len(dire):
            return 'Radiant'
        else:
            return 'Dire'