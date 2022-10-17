print("Cameron Hackett")
print("cjh200@miami.edu")
print("CSC115-4B")
print("Computer Science")
print("")
# Display my information

invalid = True
while invalid:
    print("Enter a starting number of organisms: ")
    startNumber = float(input())
    print("Enter a daily population increase: ")
    dailyIncrease = float(input())
    print("Enter a time frame: ")
    timeFrame = float(input())
    print("")
    invalid = False
    if startNumber <= 0:
        invalid = True
        print("No negative numbers allowed.")
    if dailyIncrease > 100:
        invalid = True
        print("Please enter a daily increase less than 100.")
    if timeFrame > 30:
        invalid = True
        print("Time frame must be less than 30.")
# while loop checks inputs and re-runs the program if they are not valid

dayNumber = 1
print("Day Approximate               Population")
print(1, ".", "                         ", startNumber)
dailyIncrease /= 100
# setting up formatting for table

while dayNumber < timeFrame:
    dayNumber += 1
    startNumber += (startNumber * dailyIncrease)
    print(dayNumber, ".", "                         ", startNumber)
# loop continues to multiply population until time frame is reached

