def cal_total_cir():
    """
    Calculate the total circumference of multiple circles.

    This function asks the user for the number of circles and the radius of each circle.
    It then calculates the total circumference of all the circles.

    Returns:
    float: The total circumference of all the circles.
    """
    num_circles = int(input("How many circles do you want to calculate the circumference for? "))
    total_circumference = 0

    for circle in range(1, num_circles + 1):
        radius = float(input(f"Enter the radius of circle {circle}: "))
        circumference = 2 * 3.14159 * radius
        total_circumference += circumference

    user_message = (f'That was fun')

    print(f"The total circumference of all the circles is {total_circumference}.")
    return user_message