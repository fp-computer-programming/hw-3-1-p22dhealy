# author: DMH 9/28/21

team1_wins = input("How many wins does the first team have?")

team1_ties = input("How many ties does the first team have?")

team1_points = (int(team1_wins) * 3) + int(team1_ties)

team2_wins = input("How many wins does the second team have?")

team2_ties = input("How many ties does the second team have?")

team2_points = (int(team2_wins) * 3) + int(team2_ties)

if team1_points > team2_points:
    print("Team 1 finished with more points!")
else:
    print("Team 2 finished with more points!")
