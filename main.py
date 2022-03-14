import random

region_strings = ["East", "South", "Midwest", "West"]

class Seed:
    def __init__(self, region, seed):
        self.region = region
        self.seed = seed
        self.name = "{} {}".format(self.region, self.seed)


class Region:
    def __init__(self, seeds, reg_str):
        self.seeds = seeds
        self.reg_str = reg_str
        self.winner = None


def run_madness(regions):
    for reg_str in region_strings:
        simulate_bracket(regions[reg_str])
        print("{} Wins the {} Region!".format(regions[reg_str].winner.name, reg_str))


def simulate_bracket(region):
    teams = region.seeds
    remove = []
    print("\n--------Start {} Region--------".format(region.reg_str))
    for round in range(0, 4):
        remove.clear()

        i = 0
        while i < len(teams)-1:
            winner, loser = match(region.seeds[i], region.seeds[i+1])
            #teams.remove(loser)
            remove.append(loser)
            i += 2

        for loser in remove:
            teams.remove(loser)

    region.winner = teams[0]  # last remaining team wins region


def match(team1, team2):
    rand = random.randint(0, 1000)
    print("Match Between {} and {}!".format(team1.name, team2.name))

    winner = team1
    loser = team2
    if rand > 499:
        winner = team2
        loser = team1
    #if (team1.seed > team2.seed):
        #winner = team2
        #loser = team1

    print("{} Wins!\n-----".format(winner.name))
    return winner, loser


if __name__ == '__main__':
    regions = {}
    for reg_str in region_strings:
        seeds = []

        # This is the March Madness Order, not sure if there's a good way to automate this:
        for i in [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]:
            seeds.append(Seed(reg_str, i))
        regions[reg_str] = Region(seeds, reg_str)

    run_madness(regions)

