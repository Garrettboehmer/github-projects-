#Garrett Boehmner
#Course information
#This program hopes to take an input for a course number from a user and spit out the room number, instructor, meeting time.

def main():
    #dictionary for rooms as values
    rooms = {}
    #dictionary as the instructors as values
    instructors = {}
    #dictionary with meeting times for the class as the values
    meeting_times = {}
    #used to store user input for the Course Number
    course = ' '
    #used to store the value pulled from dictionary rooms
    room = ''
    #used to store the value pulled from dictionary meeting_times
    meet = ''
    #used to store the value pulled from dictionary instuctors
    intru = ''

    rooms = {'CS101': 3004, 'CS102': 4501, 'CS103': 6755, 'NT110': 1244, 'CM241': 1411}
    instructors = {'CS101': 'Haynes', 'CS102': 'Alvarado',  'CS103': 'Rich', 'NT110': 'Burke', 'CM241': 'Lee' }
    meeting_times = {'CS101': '8:00 a.m.', 'CS102': '9:00 a.m.', 'CS103': '10:00 a.m.', 'NT110': '11:00 a.m.', 'CM241': '1:00 p.m.'}

    while course not in rooms:
        course = input('Please enter a course number: ')
        room = rooms.get(course, 'Not found')
        intru = instructors.get(course, 'Not found')
        meet = meeting_times.get(course, 'Not found')
        if course in rooms:
            print(f'You have requested information about course {course}: ')
            print(f'Room:\t\t {room}')
            print(f'Instructor:\t {intru}')
            print(f'Time:\t\t {meet}')
        elif course not in rooms:
            print('We can not find that paticular course number please try again.')

main()