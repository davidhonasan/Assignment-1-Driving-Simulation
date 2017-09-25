# Main Program
def main():
    print("Driving Simulation")
    initial_velocity = 0
    time = int(input("Time spent on the road = "))
    acceleration = int(input("Acceleration = "))
    distance = int(input("Distance = "))
    speed_limit = 60
    calculate(initial_velocity, time, acceleration, distance, speed_limit)


# Calculate
def calculate(initial_velocity, time, acceleration, distance, speed_limit):
    # Calculate distance_travelled
    print("​(The​ ​*​ ​indicates​ ​every​ ​10m)")
    for time in range(time+1):
        distance_travelled = (initial_velocity * time + 0.5 * acceleration * (time ** 2))/10
        print("Duration: " + str(time) + " Distance: " + "*" * int(distance_travelled))
    # Summary
    print("Summary:")
    speed = initial_velocity + acceleration * time
    distance_travelled = (initial_velocity * time + 0.5 * acceleration * (time ** 2))
    # If speed > speed_limit
    if speed > speed_limit:
        print("The person went over the speed limit. (Max speed was " + str(speed) + " m/s)")
    else:
        print("The person did not go over the speed limit. (Max speed was " + str(speed) + " m/s)")
    # If reached destination or not..
    if distance_travelled >= distance:
        print("The person reached the destination. (Reached " + str(distance_travelled) + " m)")
    else:
        print("The person did not reach the destination. (Reached " + str(distance_travelled) + " m)")


main()