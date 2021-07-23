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
        return False
    return True


def is_command_valid(command):
    data = command.split()
    if len(data) < 2:
        return False

    if data[0] == 'go' or data[0] == 'get' or data[0] == 'look' or command == 'view inventory':
        return True


# --------------------------------------------------GUI----------------------------------------------------------------
def get_entry(win):
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


def get_pos_coordinates(curr_pos):
    if curr_pos == [0, 1]:
        return 342.0, 154.0
    elif curr_pos == [1, 0]:
        return 258.0, 220.0
    elif curr_pos == [1, 1]:
        return 347.0, 222.0
    elif curr_pos == [1, 2]:
        return 425.0, 223.0
    elif curr_pos == [2, 1]:
        return 345.0, 286.0
    elif curr_pos == [2, 2]:
        return 425.0, 286.0


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


def instructions_page_gui():
    win = GraphWin('Adventure Game', 670, 440)
    win.setBackground('black')

    text = Text(Point(335, 220), 'Instructions:\nClick on the screen to continue')
    text.setTextColor('white')
    text.setSize(20)
    text.draw(win)

    win.getMouse()
    win.close()


def rooms_gui_page(message, curr_pos):
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
    message_text = Text(Point(150, 100), message)

    texts = [text, text1, text2, text3, text4, text5, text7, text8, message_text]

    for t in texts:
        t.setTextColor('dark khaki')
        t.setSize(15)
        t.draw(win)

    x, y = get_pos_coordinates(curr_pos)
    position_dot = Circle(Point(x, y), 10)
    position_dot.setFill('red')
    position_dot.draw(win)

    return get_entry(win)


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
    instructions_page_gui()

    inventory = []
    curr_pos = [1, 1]
    room_objects = []
    possible_directions = ['north', 'south', 'west', 'east']
    message = ''
    action_count = 0
    log_file = open('actions_log.txt', 'w')

    while True:
        command = rooms_gui_page(message, curr_pos)
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
            message = 'Invalid command!'
            continue

        if 'go' == command.split()[0]:
            direction = command.split()[1].lower()

            if not is_direction_possible(direction, possible_directions):
                message = f'It is not possible to go {direction}!\nPossible directions:\n'
                for possible_dir in possible_directions:
                    message += f'>> {possible_dir}\n'
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
            room_objects, possible_directions, room_description = room_pos[(curr_pos[0], curr_pos[1])]()
            message = f'Room description: {room_description}\nObjects: {room_objects}'

        elif 'look' == command.split()[0]:
            try:
                room = command.split()[1]
                message = f'You are looking at {room}\nRoom description: {room_desc[room]}'
            except KeyError:
                message = 'Invalid room!'
                continue

        elif "get" in command:
            item = command.split(' ', 1)[1:][0]
            if item in room_objects:
                inventory.append(item)
                message = f'{item} added successfully to your inventory!'
            else:
                message = f'{item} is not in the room and cannot be added to your inventory!'

        elif command == 'view inventory':
            if not inventory:
                message = 'Your inventory is empty.'
            else:
                message = f'You have {len(inventory)} item(s) in your inventory.\n'
                for i in range(len(inventory)):
                    message += f'{i + 1}. {inventory[i]}\n'

        action_count += 1
        print('Action', action_count, ':', command, file=log_file)

    log_file.close()


main()
