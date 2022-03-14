region_strings = ["East", "South", "Midwest", "West"]

class Seed:
    def __init__(self, region, seed):
        self.region = region
        self.seed = seed

    def to_string(self):
        return "{} {}".format(self.region, self.seed)


class Region:
    def __init__(self, seeds):
        self.seeds = seeds
        self.winner = None


def run_madness(regions):
    for reg_str in region_strings:
        simulate_bracket(regions[reg_str])


def simulate_bracket(region):
    for seed in region.seeds:
        match(region.seeds[0], seed)


def match(team1, team2):
    print("Match Between {} and {}!".format(team1.to_string(), team2.to_string()))
    winner = team1 if team1.seed < team2.seed else team2  # team return scratch bracket
    print("{} Wins!".format(winner.to_string()))
    return winner


if __name__ == '__main__':
    regions = {}
    for reg_str in region_strings:
        seeds = []
        for i in range(0, 16):
            seeds.append(Seed(reg_str, i+1))
        regions[reg_str] = Region(seeds)

    run_madness(regions)

