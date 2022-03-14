import random

region_strings = ["East", "South", "Midwest", "West"]

# Historical odds for each Seed against each other seed as percent (through 2021)
# data from: http://mcubed.net/ncaab/seeds.shtml
# Note: If the seeds have never played each other, the high seed always wins (marked 100% win)
odds = [50.0, 53.9, 63.4, 71.1, 83.9, 70.6, 85.7, 79.8, 90.1, 85.7, 55.6, 100, 100, 100, 100, 99.3],\
    [46.1, 50.0, 60.3, 44.4, 16.7, 72.2, 69.4, 44.4, 50.0, 64.5, 83.3, 100, 100, 100, 93.8, 100],\
    [36.6, 39.7, 50.0, 62.5, 50.0, 57.6, 61.1, 100, 100, 69.2, 67.9, 100, 100, 84.7, 100, 100],\
    [28.9, 55.6, 37.5, 50.0, 56.3, 33.3, 33.3, 36.4, 50.0, 100, 100, 69.0, 79.0, 100, 100, 100],\
    [16.1, 83.3, 50.0, 43.8, 50.0, 100, 100, 25.0, 25.0, 100, 100, 67.1, 84.2, 100, 100, 100],\
    [29.4, 27.8, 42.4, 66.7, 0, 50.0, 66.7, 25.0, 100, 60.0, 63.4, 100, 100, 87.5, 100, 100],\
    [14.3, 30.6, 38.9, 66.7, 0, 33.3, 50.0, 50.0, 100, 60.1, 100, 100, 100, 100, 50.0, 100],\
    [20.2, 55.6, 0.0, 63.6, 75.0, 75.0, 50.0, 50.0, 51.8, 100, 100, 0.0, 100, 100, 100, 100],\
    [9.9, 50.0, 0.0, 50.0, 75.0, 0.0, 0.0, 48.2, 50.0, 100, 0.0, 100, 100, 100, 100, 100],\
    [14.3, 35.5, 30.8, 0.0, 0.0, 40.0, 39.9, 0.0, 0.0, 50.0, 33.3, 100, 100, 100, 100, 100],\
    [44.4, 16.7, 32.1, 0.0, 0.0, 36.6, 0.0, 0.0, 100, 66.7, 50.0, 100, 100, 100, 100, 100],\
    [0.0, 0.0, 0.0, 31.0, 32.9, 0.0, 0.0, 100, 0.0, 0.0, 0.0, 50.0, 75.0, 100, 100, 100],\
    [0.0, 0.0, 0.0, 21.0, 15.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 25.0, 50.0, 100, 100, 100],\
    [0.0, 0.0, 15.3, 0.0, 0.0, 12.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 50.0, 100, 100],\
    [0.0, 6.3, 0.0, 0.0, 0.0, 0.0, 50.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 50.0, 100],\
    [0.7, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 50.0]



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


def final_four(finalists):
    print(finalists)
    finalist1, loser = match(finalists[0], finalists[3])  # East vs West
    finalist2, loser = match(finalists[1], finalists[2])  # South vs Midwest
    winner, loser = match(finalist1, finalist2)
    return winner


def run_madness(regions):
    final_four = []
    for reg_str in region_strings:
        simulate_bracket(regions[reg_str])
        print("{} Wins the {} Region!".format(regions[reg_str].winner.name, reg_str))
        final_four.append(regions[reg_str].winner)
    return final_four


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
        print("")

    region.winner = teams[0]  # last remaining team wins region


def match(team1, team2):
    rand = random.randint(0, 1000)
    print("Match Between {} and {}!".format(team1.name, team2.name))
    #print("Team 1 odds: {} - Rand: {}".format(int(odds[team1.seed - 1][team2.seed - 1])*10, rand))

    winner = team1
    loser = team2
    if rand > int(odds[team1.seed - 1][team2.seed - 1]) * 10:
        winner = team2
        loser = team1

    print("{} Wins!\n".format(winner.name))
    return winner, loser


# This is how region/seed relate to team name as of 2022 Bracket
def label_2022_teams(regions):
    east = ["Baylor", "Kentucky", "Purdue", "UCLA", "Saint Mary's", "Texas", "Murray State", "N. Carolina", "Marquette", "San Fran.", "Va. Tech", "Wyoming/Indiana", "Akron", "Yale", "St. Peters", "Norfolk St."]
    south = ["Arizona", "Villanova", "Tennessee", "Illinois", "Houston", "Colorado St.", "Ohio State", "Seton Hall", "TCU", "Loyola Chicago", "Michigan", "UAB", "Chattanooga", "Longwood", "Delaware", "Wright State/Bryant"]
    midwest = ["Kansas", "Auburn", "Wisconsin", "Providence", "Iowa", "LSU", "USC", "San Diego St.", "Creighton", "Miami (Fla.)", "Iowa State", "Richmond", "South Dakota St.", "Colgate", "Jax. State", "Texas So./Texas A&M-CC"]
    west = ["Gonzaga", "Duke", "Texas Tech", "Arkansas", "Connecticut", "Alabama", "Michigan St.", "Boise State", "Memphis", "Davidson", "Rutgers/Notre Dame", "New Mexico St.", "Vermont", "Montana St.", "CS Fullerton", "Georgia St."]

    for reg_str in region_strings:
        for seed in regions[reg_str].seeds:
            # Why is there no switch/case in Python??
            if seed.region == "East":
                seed.name = "#{} {}".format(seed.seed, east[seed.seed - 1])
            elif seed.region == "South":
                seed.name = "#{} {}".format(seed.seed, south[seed.seed - 1])
            elif seed.region == "Midwest":
                seed.name = "#{} {}".format(seed.seed, midwest[seed.seed - 1])
            elif seed.region == "West":
                seed.name = "#{} {}".format(seed.seed, west[seed.seed - 1])
            else:
                print("Something went wrong with team labelling")
                exit(0)


if __name__ == '__main__':
    regions = {}
    for reg_str in region_strings:
        seeds = []

        # This is the March Madness match order, not sure if there's a good way to automate this:
        for i in [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]:
            seeds.append(Seed(reg_str, i))
        regions[reg_str] = Region(seeds, reg_str)

    label_2022_teams(regions)
    finalists = run_madness(regions)
    print("\nThe final Four are {}, {}, {}, and {}!".format(finalists[0].name, finalists[1].name, finalists[2].name, finalists[3].name))
    winner = final_four(finalists)
    print("******* {} Win March Madness *******".format(winner.name))


