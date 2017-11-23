import math
can_coverage = 5.1*(100**2)
can_diameter = 15
can_height = 30
box_length = 60
box_width = 30
box_height = 35
cans_for_box_length = math.floor(box_length/can_diameter)
cans_for_box_width = math.floor(box_width/can_diameter)
cans_for_box_height = math.floor(box_height/can_height)
cans_in_box = cans_for_box_height * cans_for_box_length * cans_for_box_width
room_length = 4000
room_width = 3000
room_height = 340
longwall_room_area = room_length * room_height
shortwall_room_area = room_width * room_height
total_room_area = longwall_room_area * 2 + shortwall_room_area * 2
cans_for_room = math.ceil(total_room_area/can_coverage)
full_boxes = math.floor(cans_for_room/cans_in_box)
cans_not_in_box = cans_for_room % cans_in_box
print ("Number of cans required: " + str(cans_for_room))
print(str(cans_in_box))
print(str(full_boxes))
print(str(cans_not_in_box))
