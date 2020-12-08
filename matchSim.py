from math import *
from random import *

class Archer:
    """Records an archer's minimum, maximum, and average score for each end."""
    def __init__(self, qual_score):
        self.max_end = 30
        self.average_end = round((qual_score / 24),2)
        self.qual_score = qual_score
        self.min_end = self.determineMin()
        self.match_ends = []
        self.end_average = 0
        self.shootoff_wins = 0
        

    def determineMin(self):
        if self.qual_score < 500:
            self.min_end = self.average_end - 12
        elif self.qual_score < 600:
            self.min_end = self.average_end - 8
        elif self.qual_score < 620:
            self.min_end = self.average_end - 6
        elif self.qual_score < 640:
            self.min_end = self.average_end - 5
        elif self.qual_score < 660:
            self.min_end = self.average_end - 4
        elif self.qual_score >= 660:
            self.min_end = self.average_end - 3
        return floor(self.min_end)

class MatchData:
    def __init__(self, num_matches):
        self.num_matches = num_matches
        self.a1_wins = 0
        self.a2_wins = 0
        self.shootoffs = 0
    
    def get_a1_wins(self):
        return self.a1_wins
    def get_a2_wins(self):
        return self.a2_wins
    def get_a1_percent(self):
        return self.a1_win_percentage
    def get_a2_percent(self):
        return self.a2_win_percentage
    def getMatches(self):
        return self.num_matches
    def getShootoffs(self):
        return self.shootoffs

    


def printIntro():
    print('This program will take the qualification score of two archers and simulate')
    print("any number of matches between them. It will then report the statistics")
    print('of the matches.')

def getQuals():
    qual_one = int(input('Enter the qualification score of first archer: '))
    qual_two = int(input('Enter the qualification score of second archer: '))
    return qual_one, qual_two

def getMatches():
    num_matches = int(input('How many matches will be simulated? '))
    return num_matches

def generateData(match, archer1, archer2):
    for i in range(match.getMatches()):
        match, winner, archer1, archer2 = simOneMatch(match,archer1, archer2)
        if winner == 'a1':
            match.a1_wins += 1
        if winner == 'a2':
            match.a2_wins += 1
        archer1.end_average = sum(archer1.match_ends) / len(archer1.match_ends)
        archer2.end_average = sum(archer2.match_ends) / len(archer2.match_ends)
    return match, archer1, archer2

def simOneMatch(match, archer1, archer2):
    a1_end_list = []
    a2_end_list = []
    a1_points = 0
    a2_points = 0
    a1_scores, a2_scores = generateEndScores(archer1, archer2)
    while a1_points < 6 and a2_points < 6:
        if a1_points == 5 and a2_points == 5:
            match.shootoffs += 1
            winner = simOneArrow(archer1, archer2)
            return match, winner, archer1, archer2
        else:
            a1_end = getEnd(a1_scores)
            a2_end = getEnd(a2_scores)
            archer1.match_ends.append(a1_end)
            archer2.match_ends.append(a2_end)
            if a1_end > a2_end:
                a1_points += 2
            elif a2_end > a1_end:
                a2_points += 2
            elif a1_end == a2_end:
                a1_points += 1
                a2_points += 1
    if a1_points >= 6:
        winner = 'a1'
        return match, winner, archer1, archer2
    elif a2_points >= 6:
        winner = 'a2'
        return match, winner, archer1, archer2

def generateEndScores(archer1, archer2):
    a1_scores = generateScores(archer1)
    a2_scores = generateScores(archer2)
    a1_scores_fixed = fixAverage(archer1, a1_scores)
    a2_scores_fixed = fixAverage(archer2, a2_scores)
    return a1_scores_fixed, a2_scores_fixed
    
def generateScores(archer):
    a_scores = []
    for i in range(50):
        a_end = randint(archer.min_end, archer.max_end)
        a_scores.append(a_end)
    return a_scores

def fixAverage(archer, a_scores):
    a_average, list_average, average_gap = averageGap(archer, a_scores)
    while not (a_average - .1) < list_average < (a_average + .1):
        if average_gap > 0:
            list_index = randint(0, (len(a_scores)-1))
            if archer.max_end > a_scores[list_index]:
                a_scores[list_index] = a_scores[list_index] + 1
                a_average, list_average, average_gap = averageGap(archer, a_scores)
            else:
                continue
        elif average_gap < 0:
            list_index = randint(0, len(a_scores)-1)
            if a_scores[list_index] > archer.min_end:
                a_scores[list_index] = a_scores[list_index] - 1
                a_average, list_average,average_gap = averageGap(archer, a_scores)
            else:
                continue
    return a_scores

def getEnd(a_scores):
    rand_index = randint(0, len(a_scores)-1)
    end_score = a_scores[rand_index]
    return end_score

def simOneArrow(archer1, archer2):
    a1_arrow = getArrow(archer1)
    a2_arrow = getArrow(archer2)
    if a1_arrow > a2_arrow:
        archer1.shootoff_wins += 1
        return 'a1'
    elif a2_arrow > a1_arrow:
        archer2.shootoff_wins += 1
        return 'a2'
    elif a1_arrow == a2_arrow:
        return simOneArrow(archer1, archer2)

def getArrow(archer):
    if archer.qual_score < 500:
        arrow = randint(4,10)
    elif 500 <= archer.qual_score < 550:
        arrow = randint(5,10)
    elif 550 <= archer.qual_score < 620:
        arrow = randint(6,10)
    elif 620 <= archer.qual_score < 650:
        arrow = randint(7,10)
    elif 650 <= archer.qual_score < 670:
        arrow = randint(8,10)
    else:
        arrow = randint(9,10)
    return arrow
        

def averageGap(archer, a_scores):
    a_average = archer.average_end
    list_average = sum(a_scores) / len(a_scores)
    average_gap = a_average * len(a_scores) - sum(a_scores)
    return a_average, list_average, average_gap

def displayData(archer1, archer2, match):

    print("\n{0:>15}: {1} \n".format('Number of matches', match.getMatches()))
    print("{0:^40}\n".format('Archer 1'))
    print('Archer 1 qualification score: {0}'.format(archer1.qual_score))
    print('Archer 1 match wins: {0} ({1:0.2f}%)'.format(match.get_a1_wins(), (match.get_a1_wins()/match.getMatches()*100)))
    print('Archer 1 arrow average: {0:0.3f}'.format(archer1.end_average))
    print("Archer 1 shootoff wins: {0}\n".format(archer1.shootoff_wins))
    print("{0:^40}\n".format('Archer 2'))
    print('Archer 2 qualification score: {0}'.format(archer2.qual_score))
    print('Archer 2 match wins: {0} ({1:0.2f}%)'.format(match.get_a2_wins(), (match.get_a2_wins() / match.getMatches()*100)))
    print('Archer 2 arrow average: {0:0.3f}:'.format(archer2.end_average))
    print('Archer 2 shootoff wins: {0}\n'.format(archer2.shootoff_wins))
    
    
    

def main():
    printIntro()
    qual_one, qual_two = getQuals()
    num_matches = getMatches()
    match = MatchData(num_matches)
    archer1 = Archer(qual_one)
    archer2 = Archer(qual_two)
    match, archer1, archer2= generateData(match, archer1, archer2)
    displayData(archer1, archer2, match)
if "__name__" == "__main__":
   main()


#def test(qual_one, qual_two, num_matches):
 #   match = MatchData(num_matches)
  #  archer1 = Archer(qual_one)
   # archer2 = Archer(qual_two)
    #match, archer1, archer2= generateData(match, archer1, archer2)
    #displayData(archer1, archer2, match)
    
