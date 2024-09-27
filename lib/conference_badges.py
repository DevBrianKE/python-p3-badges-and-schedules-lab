def badge_maker(name):
    return f"Hello, my name is {name}."


def batch_badge_creator(names):
    list =[]
    for name in names:
        list.append( f"Hello, my name is {name}.")
    return list
     

def assign_rooms(names):
    room_assignments = []  # Initialize an empty list to store room assignments
    for i, name in enumerate(names):  # Loop through the names with their indices
        room_number = (i % 8) + 1  # Calculate the room number (1-8)
        room_assignments.append(f"Hello, {name}! You'll be assigned to room {room_number}!")  # Create and append the assignment message
    return room_assignments  # Return the list of room assignments



def printer(names):
    # First, get the badge messages and print them
    badge_messages = batch_badge_creator(names)
    for message in badge_messages:  # Iterate over the badge messages
        print(message)  # Print each badge message
    
    # Then, get the room assignments and print them
    room_assignments = assign_rooms(names)
    for assignment in room_assignments:  # Iterate over the room assignments
        print(assignment)  # Print each room assignment

