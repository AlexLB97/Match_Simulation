# Match_Simulation
This is a class-based python script to predict the outcomes of elimination matches depending on the qualification score of each archer.


This script runs on the command line currently, although it may be expanded to include a GUI at a later date. The purpose of writing this script was two-fold. 
The initial impetus was the need to practice writing class-based programs, but I was also curious about my ability to effectively model match play in archery.

To accomplish this, I created an archer class that stores the performance information about two archers when provided the archer's qualification score as a calling
argument. Based on the qualification score, an array of 50 3-arrow ends is generated and for each archer and normalized around their average arrow value from 
the qualification round. Since lower scoring archers are less consistent, lower qualification scores yield a wider range of possible end scores, but the average across
all of the ends matches their qualification average.

To simulate a match, ends are picked at random from each archer's array of possible ends and scored based on World Archery match play scoring criteria, which is as follows:
- The higher scoring archer for each three arrow end gets 2 points.
- If the archers have the same end score, each archer gets 1 point.
- The first archer to achieve 6 or seven points wins the match.
- If both archers end up at 5 points, the match goes to a one arrow shoot off.

Given these rules, the script will simulate the number of matches input at the beginning of the script, and provide output in the terminal with the number of matches
simulated, the number of matches each archer won, the number of ties, the win percentage of each archer, and the average end of each archer.

I was pleasantly surprised that the modeling in this script produces results that are similar to my personal experience competing on an international level.
