def findWinningPlayer(self, skills: List[int], k: int) -> int:
        skill_to_idx = {skill : idx for idx, skill in enumerate(skills)}
        wins = {skill : 0 for skill in skills}
        max_skill = max(skills)

        def check_win(skill):
            return wins[skill] == k

        while True:
            s0, s1 = skills[0], skills[1]
            if s0 > s1:
                winner = s0
                wins[s0] += 1
                skills.append(skills.pop(1))
            else: 
                winner = s1
                wins[s1] += 1
                skills.append(skills.pop(0))

            if check_win(winner):
                break
            
            if winner == max_skill:
                break

        return skill_to_idx[winner]