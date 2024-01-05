# 4. In a long career for Yorkshire, Geoffrey Boycott played 609 matches, batted 1014
# times, was not out 162 times, and scored 48426 runs. Write a program to calculate and display Boycott's batting average.
# Note: A batting average is the number of runs scored divided by the number of
# completed innings (i.e. the total times batted minus the times not out).


# Program to calculate and display Boycott's batting average
total_matches_played = 609
total_times_batted = 1014
times_not_out = 162
total_runs_scored = 48426

# Calculating Boycott's batting average
batting_average = total_runs_scored / (total_times_batted - times_not_out)

# Displaying results
print(f"Geoffrey Boycott's batting average: {batting_average:.2f}")

