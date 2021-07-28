from graphics import *


# -------------------------------------------Rooms Definition----------------------------------------------------------

def enter_room1():
    description = 'You have entered in the cockpit.\n'
    objects = ['pair of glasses', 'bottle of water']
    possible_directions = ['south']
    possible_looks = ['main cabin', 'cockpit']
    return objects, possible_directions, description, possible_looks


def enter_room2():
    description = 'You have entered in the systems room.\n'
    objects = ['maintenance manual', 'wrench']
    possible_directions = ['east']
    possible_looks = ['main cabin', 'systems room']
    return objects, possible_directions, description, possible_looks


def enter_room3():
    description = 'You have entered in the main cabin.\n'
    objects = []
    possible_directions = ['north', 'south', 'west', 'east']
    possible_looks = ['main cabin', 'cockpit', 'systems room', 'pilot room', 'cargo room']
    return objects, possible_directions, description, possible_looks


def enter_room4():
    description = 'You have entered in the pilot''s bedroom.\n'
    objects = ['key', 'tube of sunscreen', 'booking confirmation']
    possible_directions = ['west', 'south']
    possible_looks = ['main cabin', 'pilot room', 'engine room']
    return objects, possible_directions, description, possible_looks


def enter_room5():
    description = 'You have entered in the cargo room.\n'
    objects = ['can of oil']
    possible_directions = ['north', 'east']
    possible_looks = ['main cabin', 'cargo room', 'engine room']
    return objects, possible_directions, description, possible_looks


def enter_room6():
    description = 'You have entered in the engine room\n'
    objects = []
    possible_directions = ['north', 'west']
    possible_looks = ['engine room', 'pilot room', 'cargo room']
    return objects, possible_directions, description, possible_looks


# --------------------------------------------------Validations--------------------------------------------------------

def is_direction_possible(direction, possible_directions):
    if direction not in possible_directions:
        return False
    return True


def is_look_possible(room, possible_looks):
    if room not in possible_looks:
        return False
    return True


def is_command_valid(command):
    data = command.split()
    if len(data) < 2:
        return False

    if data[0] == 'go' or data[0] == 'get' or data[0] == 'look' or command == 'view inventory':
        return True


# --------------------------------------------------Go Function--------------------------------------------------------
def go(curr_pos, direction, allow_room6, tried_room6):
    if direction == 'north':
        curr_pos[0] += dir_changes['north'][0]
        curr_pos[1] += dir_changes['north'][1]
    elif direction == 'south' and curr_pos != [1, 2]:
        curr_pos[0] += dir_changes['south'][0]
        curr_pos[1] += dir_changes['south'][1]
    elif direction == 'west':
        curr_pos[0] += dir_changes['west'][0]
        curr_pos[1] += dir_changes['west'][1]
    elif direction == 'east' and curr_pos != [2, 1]:
        curr_pos[0] += dir_changes['east'][0]
        curr_pos[1] += dir_changes['east'][1]
    elif direction == 'south' and curr_pos == [1, 2] and not allow_room6:
        # if user wants to enter in engine room and cannot
        curr_pos[0] = 1
        curr_pos[1] = 2
        tried_room6 = True
    elif direction == 'east' and curr_pos == [2, 1] and not allow_room6:
        curr_pos[0] = 2
        curr_pos[1] = 1
        tried_room6 = True
    elif direction == 'south' and curr_pos == [1, 2] and allow_room6:
        curr_pos[0] += dir_changes['south'][0]
        curr_pos[1] += dir_changes['south'][1]
        tried_room6 = True
    elif direction == 'east' and curr_pos == [2, 1] and allow_room6:
        curr_pos[0] += dir_changes['east'][0]
        curr_pos[1] += dir_changes['east'][1]
        tried_room6 = True

    return curr_pos, tried_room6


# --------------------------------------------------GUI----------------------------------------------------------------
def get_entry(win):
    entry = Entry(Point(550.0, 90.0), 30)
    entry.setSize(10)
    entry.setFill("white")
    entry.setTextColor('black')
    entry.draw(win)

    while True:
        key = win.getKey()
        if key == 'Return':
            win.close()
            return entry.getText()


def get_pos_coordinates(curr_pos):
    if curr_pos == [0, 1]:
        return 347.0, 154.0
    elif curr_pos == [1, 0]:
        return 265.0, 222.0
    elif curr_pos == [1, 1]:
        return 347.0, 222.0
    elif curr_pos == [1, 2]:
        return 429.0, 222.0
    elif curr_pos == [2, 1]:
        return 347.0, 286.0
    elif curr_pos == [2, 2]:
        return 429.0, 286.0


def welcome_gui_page():
    win = GraphWin('Adventure Game', 670, 440)

    Image(Point(335, 220), 'space.png').draw(win)
    welcome_message1 = Text(Point(335, 80), 'An alien is planning on visiting planet Earth for a couple days.\n '
                                            'After booking his Airbnb, he jumps in his spaceship and leaves his planet.\n '
                                            'After a 3 days journey in space, he suddenly hears a terrible noise!\n '
                                            'His engine just stopped working...\n '
                                            'He needs to repair it to be on time for his rental in Mallorca. HELP HIM!\n\n '
                                            'You are the alien! Look in your spaceship for any items that could help you'
                                            ' continue your journey.\n')

    welcome_message = Text(Point(550, 370), 'Start HERE')
    welcome_message1.setTextColor('white')
    welcome_message.setTextColor('goldenrod')
    welcome_message1.draw(win)
    welcome_message.draw(win)
    welcome_message.setStyle('bold')
    welcome_message.setSize(25)

    while True:
        p = win.getMouse()
        if 550 <= p.getX() <= 670 and 350 <= p.getY() <= 380:
            break

    win.close()


def instructions_page_gui():
    win = GraphWin('Adventure Game', 670, 440)
    win.setBackground('black')

    text1 = Text(Point(335, 30), 'INSTRUCTIONS:')
    text = Text(Point(335, 200), 'Help the alien gather the items needed to repair his engine!\n\n\n\n'
                                 'What you can do:\n\n\n'
                                 '1. "Go <North, South, East or West>" to move between rooms.\n\n'
                                 '2. "Look <Room Name>" to look at the room your are in or a nearby room.\n\n '
                                 '3. "Get <Item>" to pick up an item that is in your room.\n\n'
                                 '4. "View Inventory" to see which items you have in your inventory.\n\n'
                                 'The green dot represents your current position on the spaceship.')

    text2 = Text(Point(335, 400), 'Click on the screen to continue')
    text1.setTextColor('red')
    text.setTextColor('goldenrod')
    text2.setTextColor('white')
    text1.setSize(20)
    text.setSize(13)
    text2.setSize(15)
    text1.draw(win)
    text.draw(win)
    text2.draw(win)

    win.getMouse()
    win.close()


def rooms_gui_page(message, curr_pos):
    win = GraphWin('Adventure Game', 670, 440)
    Image(Point(335, 220), 'rooms_page_background.png').draw(win)

    triangle = Polygon(Point(335.0, 21.0), Point(88.0, 374.0), Point(582.0, 374.0), )
    rectangle1 = Rectangle(Point(293.0, 205.0), Point(376.0, 270.0))
    rectangle2 = Rectangle(Point(293.0, 139.0), Point(376.0, 205.0))
    rectangle3 = Rectangle(Point(293.0, 332.0), Point(376.0, 270.0))
    rectangle4 = Rectangle(Point(293.0, 205.0), Point(214.0, 270.0))
    rectangle5 = Rectangle(Point(375.0, 205.0), Point(455.0, 270.0))
    rectangle6 = Rectangle(Point(375.0, 270.0), Point(455.0, 332.0))

    shapes = [triangle, rectangle1, rectangle2, rectangle3, rectangle4, rectangle5, rectangle6]

    for shape in shapes:
        shape.setFill('SlateGray3')
        triangle.setFill('Slategray')
        shape.setOutline('goldenrod')
        shape.setWidth(1)
        triangle.setWidth(3)
        shape.draw(win)

    text1 = Text(Point(333.0, 152.0), 'Cockpit')
    text2 = Text(Point(333.0, 218.0), 'Main Cabin')
    text3 = Text(Point(253.0, 218.0), 'Systems Room')
    text4 = Text(Point(413.0, 219.0), 'Pilot Room')
    text5 = Text(Point(333.0, 281.0), 'Cargo Room')
    text7 = Text(Point(413.0, 282.0), 'Engine Room')
    text8 = Text(Point(546.0, 46.0), 'What do you want to do next?')
    text9 = Text(Point(485, 66), 'Press ENTER to quit.')
    message_text = Text(Point(146, 76), message)

    texts = [text1, text2, text3, text4, text5, text7, text8, text9, message_text]

    for t in texts:
        t.setTextColor('white')
        t.setSize(8)
        t.draw(win)

    text8.setSize(13)
    text9.setSize(8)
    message_text.setSize(10)
    x, y = get_pos_coordinates(curr_pos)
    position_dot = Circle(Point(x - 15, y + 25), 10)
    position_dot.setFill('forest green')
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

obj_desc = {
    'pair of glasses': 'These could be helpful if you had\n to read a book.',
    'bottle of water': 'Stay hydrated!',
    'maintenance manual': 'This manual could help you do some reparations.\n'
                          'But without glasses, you can''t even read the title.\n',
    'wrench': 'Perfect tool to do any kind of reparation!',
    'key': 'Well, it''s a key. So it probably opens a door...',
    'tube of sunscreen': 'Essential to tan without burning your alien skin!',
    'booking confirmation': 'Make sure not lose it\n or you will have to forget\n your holidays on Earth!',
    'can of oil': 'It''s greasy and it smells bad.\n The kind of stuff you pour in an engine\n but not in your glass. ',
}

room_desc = {
    'cockpit': 'This is where you can control your spaceship.\n'
               'There is a "pair of glasses" on the pilot''s seat\n'
               'and a "bottle of water" in the cup holder.',
    'systems room': 'There are screens and wires everywhere. \n'
                    'It\'s a real mess!\nYou however spotted what appears\nto be a "maintenance manual" on a table\n'
                    'and a "wrench" on the floor.',
    'main cabin': 'This is where everyone seats when traveling.',
    'pilot room': 'There is a bed that does not look\n very comfortable on which lies\n a "tube of sunscreen" together '
                  'with\n your "booking confirmation" for mallorca.\n There is also a "key" on the pilot''s desk.',
    'cargo room': 'It''s full of luggage!\nThere is a big "can of oil" in the corner.',
    'engine room': 'Here is where the whole\n engine''s machinery is located!',
}


# -----------------------------------------------------Main------------------------------------------------------------

def main():
    welcome_gui_page()
    instructions_page_gui()

    inventory = []
    curr_pos = [1, 1]
    room_objects = []
    possible_directions = ['north', 'south', 'west', 'east']
    possible_looks = ['main cabin', 'cockpit', 'systems room', 'pilot room', 'cargo room']
    message = ''
    action_count = 0
    allow_room6 = False  # access to room 6 is not allowed
    hint = True  # hint for the book and pair of glasses combination
    log_file = open('actions_log.txt', 'w')

    while True:
        tried_room6 = False
        command = rooms_gui_page(message, curr_pos)
        command = command.lower()

        if not command:
            break

        if not is_command_valid(command):
            message = 'Invalid command!'
            continue

        if 'go' == command.split()[0]:
            direction = command.split()[1]

            if not is_direction_possible(direction, possible_directions):
                message = f'It is not possible to go {direction}!\nPossible directions:\n'
                for possible_dir in possible_directions:
                    message += f'>> {possible_dir}\n'
                continue

            curr_pos, tried_room6 = go(curr_pos, direction, allow_room6, tried_room6)
            # find current room, call its function, and get its objects
            room_objects, possible_directions, curr_room_description, possible_looks = room_pos[
                (curr_pos[0], curr_pos[1])
            ]()
            if not allow_room6 and tried_room6:
                message = f'You cannot enter the door is locked :('
            else:
                message = f'{curr_room_description}\n'

        elif 'look' == command.split()[0]:
            try:
                room = command.split(' ', 1)[1:][0]

                if not is_look_possible(room, possible_looks):
                    message = f'It is not possible to look at {room}!\nPossible rooms to look at:\n'
                    for possible_look in possible_looks:
                        message += f'>> {possible_look}\n'
                    continue
                else:
                    message = f'You are looking at {room}.\n {room_desc[room]}'
            except KeyError:
                message = 'Invalid room name!'
                continue

        elif "get" in command:
            item = command.split(' ', 1)[1:][0]
            if item in room_objects and item not in inventory:
                inventory.append(item)
                if item == 'key':
                    allow_room6 = True
                if 'maintenance manual' in inventory and 'pair of glasses' in inventory and hint:
                    message = f'You just picked the {item}.\n' \
                              f'{obj_desc[item]}Since you have both the manual and the glasses\n' \
                              f'in your inventory, you can now read\n that a wrench' \
                              f'and some oil are needed\n to repair the engine. '
                    hint = False
                else:
                    message = f'You just picked the {item}.\n' \
                              f'This item was added to your inventory!' \
                              f'\n{obj_desc[item]}'
            elif item in room_objects and item in inventory:
                message = f'{item} is already in your inventory!'
            else:
                message = f'{item} is not in the room \nand cannot be added to your inventory!'

        elif command == 'view inventory':
            if not inventory:
                message = 'Your inventory is empty.'
            else:
                message = f'You have {len(inventory)} item(s) in your inventory:\n'
                for i in range(len(inventory)):
                    message += f'{i + 1}. {inventory[i]}\n'

        if curr_pos == [2, 2] and 'can of oil' in inventory and 'wrench' in inventory:
            score = (9 / (action_count + 1)) * 60 + (
                        3 / len(inventory)) * 40  # Min[actions possible, objects] to win = [9,3]
            score = round(float(score), 1)
            message = f'CONGRATULATION! YOU WIN!\nYour score is: {score}%\n\n ' \
                      f'Try improving your score by solving\n the game as fast as possible and\n ' \
                      f'with the least possible items!'
            command = "YOU WIN"

        action_count += 1
        print('Action', action_count, ':', command, file=log_file)

    log_file.close()


main()
