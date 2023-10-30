import math
# Constants

CAN_COVERAGE = 5.1  # Square meters

CAN_DIAMETER = 0.15  # Meters

CAN_HEIGHT = 0.3  # Meters

BOX_LENGTH = 0.6  # Meters

BOX_WIDTH = 0.3  # Meters

BOX_HEIGHT = 0.35  # Meters

 

# Calculate the area of a single can

can_radius = CAN_DIAMETER / 2

can_area = math.pi * can_radius**2

 

# Calculate the total area to be painted

hall_length = 40  # Meters

hall_width = 30  # Meters

hall_ceiling_height = 3.4  # Meters

hall_area = 2 * (hall_length * hall_width + hall_length * hall_ceiling_height + hall_width * hall_ceiling_height)

 

# Calculate the minimum number of cans needed

num_cans = math.ceil(hall_area / CAN_COVERAGE)

 

# Calculate the number of full boxes

box_volume = BOX_LENGTH * BOX_WIDTH * BOX_HEIGHT

num_boxes = math.floor(num_cans * can_area / box_volume)

 

# Calculate the number of cans not packed into boxes

cans_not_packed = num_cans - num_boxes * math.floor(box_volume / can_area)

 

# Output the results

print("1. Minimum number of cans needed:", num_cans)

print("2. Number of full boxes:", num_boxes)

print("3. Number of cans not packed into boxes:", cans_not_packed)