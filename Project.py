import datetime
import time

# Function to calculate time difference between current time and deadline
def time_until_deadline(deadline):
    current_time = datetime.datetime.now()
    time_difference = deadline - current_time
    return time_difference.total_seconds()

# Function to check if a deadline is approaching
def check_deadline(task):
    deadline = task['deadline']
    time_diff = time_until_deadline(deadline)
    # Check if deadline is within 24 hours
    if 0 < time_diff <= 24*3600:
        print(f"Deadline for task '{task['title']}' is approaching! It's due in {time_diff/3600:.1f} hours.")

# Example task dictionary
task1 = {'title': 'Complete project', 'deadline': datetime.datetime(2024, 4, 10, 12, 0, 0)}
task2 = {'title': 'Submit report', 'deadline': datetime.datetime(2024, 4, 12, 16, 30, 0)}

# Example tasks list
tasks = [task1, task2]

# Check deadlines periodically
while True:
    for task in tasks:
        check_deadline(task)
    # Check every hour
    time.sleep(3600)
