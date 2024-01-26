import sys

# Function to analyze a log file from a cat shelter
def analyze_shelter_logs(log_file_path):
    try:
        # Open the specified log file in read mode
        with open(log_file_path, 'r') as log_file:
            # Read all lines from the log file
            log_lines = log_file.readlines()

        # Initialize variables 
        our_cat_visits = 0 
        other_cats_visits = 0
        total_time_spent = 0  
        visit_durations = [] 

        #  Iterate each line in the log file
        for log_line in log_lines:
            # Check if the line starts with "OURS" 
            if log_line.startswith("OURS"):
                our_cat_visits += 1
                # Extract entry and exit times, and calculate the visit duration
                entry_time, exit_time = map(int, log_line.split(',')[1:])
                duration = exit_time - entry_time
                # Update total time 
                total_time_spent += duration
                visit_durations.append(duration)
            # Check if the line starts with "THEIRS" 
            elif log_line.startswith("THEIRS"):
                other_cats_visits += 1

        # Check if no cat visits were recorded
        if our_cat_visits == 0:
            print("Our cat visits not recorded in the log file.")
            return

        # Calculate average, longest, and shortest visit durations
        average_duration = sum(visit_durations) / len(visit_durations)
        longest_duration = max(visit_durations)
        shortest_duration = min(visit_durations)

        # Print the  results 
        print("\nLog File Analysis")
        print("==================\n")
        print(f"Cat Visits: {our_cat_visits}")
        print(f"Other Cats: {other_cats_visits}\n")
        print(f"Total Time in house: {total_time_spent // 60} hours, {total_time_spent % 60} minutes\n")
        print(f"Average Visit Length: {int(average_duration)} minutes")
        print(f"Longest Visit:        {longest_duration} minutes")
        print(f"Shortest Visit:       {shortest_duration} minutes\n")

    # Handle the case where the specified log file is not found
    except FileNotFoundError:
        print(f"Can't open'{log_file_path}'!")

def main():
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 2:
        print("Missing command line arguements!")
    else:
        # Extract the log file path from the command line argument and analyze the cat shelter log
        log_file_path = sys.argv[1]
        analyze_shelter_logs(log_file_path)
main()