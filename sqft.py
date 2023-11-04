def cal_total_sqft():
    """
    Calculate the total square footage of a house with multiple rooms.

    This program asks the user for the number of rooms in the house and the dimensions (length and width) of each room.
    It then calculates the total square footage of the entire house.

    Returns:
    float: The total square footage of the entire house.
    """
    num_rooms = int(input("How many rooms are there in the house? "))
    total_square_footage = 0

    for room in range(1, num_rooms + 1):
        length = float(input(f"Enter the length of room in feet {room}: "))
        width = float(input(f"Enter the width of room in feet {room}: "))
        total_square_footage += length * width

    user_message = (f'That was fun')

    print(f"The total square footage of the entire house is {total_square_footage} square feet.")
    return user_message