import datetime

# Get the current system time
current_time = datetime.datetime.now().time()

# Extract the hour from the current time
hour = current_time.hour

# Define greetings based on the time of day
if 5 <= hour < 12:
    greeting = "Good morning!"
elif 12 <= hour < 17:
    greeting = "Good afternoon!"
else:
    greeting = "Good evening!"

# Accept a sentence from the user
sentence = input("Enter your username: ")

# Display the greetings message along with the user's sentence
print(f"{greeting} {sentence}")
