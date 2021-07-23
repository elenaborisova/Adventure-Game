from graphics import *


# -------------------------------------------Rooms Definition----------------------------------------------------------

def enter_room1():
    description = 'You have entered in the cockpit.\n'
    objects = ['Pair of glasses', 'Bottle of water']
    possible_directions = ['south']
    return objects, possible_directions, description


def enter_room2():
    description = 'You have entered in the systems room.\n'
    objects = ['Maintenance manual', 'Wrench']
    possible_directions = ['east']
    return objects, possible_directions, description


def enter_room3():
    description = 'You have entered in the main cabin.\n'
    objects = []
    possible_directions = ['north', 'south', 'west', 'east']
    return objects, possible_directions, description


def enter_room4():
    description = 'You have entered in the pilot\'s bedroom.\n'
    objects = ['Key', 'Tube of sunscreen', 'Booking confirmation for Mallorca']
    possible_directions = ['west']
    return objects, possible_directions, description


def enter_room5():
    description = 'You have entered in the cargo bay.\n'
    objects = ['Can of oil']
    possible_directions = ['north', 'east']
    return objects, possible_directions, description


def enter_room6():
    description = 'You have entered in the engine room.\n'
    objects = []
    possible_directions = ['north', 'west']  # TODO add this functionality to LOOK
    return objects, possible_directions, description


# --------------------------------------------------Validations--------------------------------------------------------

def is_direction_possible(direction, possible_directions):
    if direction not in possible_directions:
        print('It is not possible to go ' + direction + '!')
        print('Possible directions:')
        for possible_dir in possible_directions:
            print('>>', possible_dir)
        print()
        return False
    return True


def is_command_valid(command):
    data = command.split()
    if len(data) < 2:
        return False

    if data[0] == 'go' or data[0] == 'get' or data[0] == 'look' or command == 'view inventory':
        return True


# --------------------------------------------------Commands-----------------------------------------------------------

def get(item, inventory, objects):
    if item in objects:
        inventory.append(item)
    else:
        print('The item you want to get is not in the room.\n')
    return inventory


def view_inv(inventory):
    if not inventory:
        print('Your inventory is empty.')
        return

    print('You have', len(inventory), 'item(s) in your inventory.')
    for i in range(len(inventory)):
        print(str(i + 1) + '.', inventory[i])
    print()


# TODO possible to look only neighbour rooms
def look(room, room_desc):
    return room_desc[room]


# --------------------------------------------------GUI----------------------------------------------------------------

def welcome_gui_page():
    win = GraphWin('Adventure Game', 670, 440)

    Image(Point(335, 220), 'space.png').draw(win)
    welcome_message = Text(Point(450, 100), 'START GAME HERE')
    welcome_message.setTextColor('white')
    welcome_message.draw(win)
    welcome_message.setSize(25)

    while True:
        p = win.getMouse()
        if 330 <= p.getX() <= 570 and 90 <= p.getY() <= 110:
            break

    win.close()


def rooms_gui_page():
    win = GraphWin('Adventure Game', 670, 440)
    Image(Point(335, 220), 'rooms_page_background.png').draw(win)

    triangle = Polygon(Point(335.0, 21.0), Point(88.0, 374.0), Point(582.0, 374.0),)
    rectangle1 = Rectangle(Point(293.0, 205.0), Point(376.0, 270.0))
    rectangle2 = Rectangle(Point(293.0, 139.0), Point(376.0, 205.0))
    rectangle3 = Rectangle(Point(293.0, 332.0), Point(376.0, 270.0))
    rectangle4 = Rectangle(Point(293.0, 205.0), Point(214.0, 270.0))
    rectangle5 = Rectangle(Point(375.0, 205.0), Point(455.0, 270.0))
    rectangle6 = Rectangle(Point(375.0, 270.0), Point(455.0, 332.0))

    shapes = [triangle, rectangle1, rectangle2, rectangle3, rectangle4, rectangle5, rectangle6]

    for shape in shapes:
        shape.setFill('black')
        shape.setOutline('dark khaki')
        shape.setWidth(4)
        shape.draw(win)

    text1 = Text(Point(332.0, 172.0), 'ROOM 1')
    text2 = Text(Point(333.0, 238.0), 'ROOM 3')
    text3 = Text(Point(250.0, 238.0), 'ROOM 2')
    text4 = Text(Point(411.0, 239.0), 'ROOM 4')
    text5 = Text(Point(331.0, 301.0), 'ROOM 5')
    text7 = Text(Point(412.0, 302.0), 'ROOM 6')
    text8 = Text(Point(546.0, 66.0), 'What do you want to do next?')

    text = Text(Point(335.0, 406.0), 'You are currently in the main cabin of the spaceship.')
    texts = [text, text1, text2, text3, text4, text5, text7, text8]

    for t in texts:
        t.setTextColor('dark khaki')
        t.setSize(15)
        t.draw(win)

    entry = Entry(Point(552.0, 107.0), 20)
    entry.setSize(10)
    entry.setTextColor('dark khaki')
    entry.setStyle('bold')
    entry.draw(win)

    while True:
        key = win.getKey()
        if key == 'Return':
            win.close()
            return entry.getText()


def room_gui(room_objects, room_description):
    win = GraphWin('Adventure Game', 670, 440)
    win.setBackground('black')

    text = Text(Point(335, 220), f'Room description: {room_description}\n'
                                 f'Objects: {room_objects}')
    text.setTextColor('dark khaki')
    text.setSize(20)
    text.draw(win)

    win.getMouse()
    win.close()


def look_room_gui(room, room_description):
    win = GraphWin('Adventure Game', 670, 440)
    win.setBackground('black')

    text = Text(Point(335, 220), f'You are looking at {room}\n'
                                 f'Room description: {room_description}\n')
    text.setTextColor('dark khaki')
    text.setSize(20)
    text.draw(win)

    win.getMouse()
    win.close()


# --------------------------------------------------Dictionaries-------------------------------------------------------

# Room Positions --> Room Number : [Matrix Row, Matrix Column]
room_pos = {
    (0, 1): enter_room1,  # key = location: value = function to room
    (1, 0): enter_room2,
    (1, 1): enter_room3,
    (1, 2): enter_room4,
    (2, 1): enter_room5,
    (2, 2): enter_room6,
}

# Change in index depending on direction
dir_changes = {
    'north': (-1, 0),
    'south': (1, 0),
    'west': (0, -1),
    'east': (0, 1),
}

# TODO Objects Descriptions
obj_desc = {
    'Pair of glasses': 'OD1',
    'Bottle of water': 'OD2',
    'Maintenance manual': 'OD3',
    'Wrench': 'OD4',
    'Key': 'OD5',
    'Tube of sunscreen': 'OD6',
    'Booking confirmation for Mallorca': 'OD7',
    'Can of oil': 'OD8',
}

# TODO Room Description + objects
room_desc = {
    'room1': 'RD1',
    'room2': 'RD2',
    'room3': 'RD3',
    'room4': 'RD4',
    'room5': 'RD5',
    'room6': 'RD6',
}


# -----------------------------------------------------Main------------------------------------------------------------

def main():
    welcome_gui_page()

    inventory = []
    curr_pos = [1, 1]
    curr_room_objects = []
    curr_room_description = ''
    possible_directions = ['north', 'south', 'west', 'east']
    action_count = 0
    log_file = open('actions_log.txt', 'w')
    game_over = False

    while True:
        command = rooms_gui_page()
        # command = input('What do you want to do now?\n'
        #                 'You can choose from:\n'
        #                 '>>> go [possible direction]\n'
        #                 '>>> look [nearby room]\n'
        #                 '>>> get [item]\n'
        #                 '>>> view inventory\n'
        #                 '[Press <ENTER> to quit]\n')

        if not command:
            break

        if not is_command_valid(command):
            print('Invalid command!\n')
            continue

        if 'go' == command.split()[0]:
            direction = command.split()[1].lower()

            if not is_direction_possible(direction, possible_directions):
                continue

            if direction == 'north':
                curr_pos[0] += dir_changes['north'][0]
                curr_pos[1] += dir_changes['north'][1]
            elif direction == 'south':
                curr_pos[0] += dir_changes['south'][0]
                curr_pos[1] += dir_changes['south'][1]
            elif direction == 'west':
                curr_pos[0] += dir_changes['west'][0]
                curr_pos[1] += dir_changes['west'][1]
            elif direction == 'east':
                curr_pos[0] += dir_changes['east'][0]
                curr_pos[1] += dir_changes['east'][1]

            # find current room, call its function, and get its objects
            curr_room_objects, possible_directions, curr_room_description = room_pos[(curr_pos[0], curr_pos[1])]()
            room_gui(curr_room_objects, curr_room_description)

        elif 'look' == command.split()[0]:
            try:
                room = command.split()[1]
                look_room_gui(room, curr_room_description)
                # print(look(room, curr_room_description))
                # print()
            except KeyError:
                print('Invalid room!\n')
                continue

        elif "get" in command:
            item = command.split(' ', 1)[1:][0]
            inventory = get(item, inventory, curr_room_objects)

        elif command == 'view inventory':
            view_inv(inventory)

        action_count += 1
        print('Action', action_count, ':', command, file=log_file)

        if game_over:
            break

    log_file.close()


main()
