# Sean Curley
# 015068363
# Project 9
# April 19, 2017

run = True
check = 0

room = {'cs101': '3004',            # Create Room Dictionary
        'cs102': '4501',
        'cs103': '6755',
        'nt110': '1244',
        'cm241': '1411'}
instructor = {'cs101': 'Haynes',    # Create Instructor Dictionary
              'cs102': 'Alvarado',
              'cs103': 'Rich',
              'nt110': 'Burke',
              'cm241': 'Lee'}
time = {'cs101': '8:00 am',         # Create Time Dictionary
        'cs102': '9:00 am',
        'cs103': '10:00 am',
        'nt110': '11:00 am',
        'cm241': '1:00 pm'}

while run:
    course = input("Enter which class details you would like to view:\nCS101\nCS102\nCS103\nNT110\nCM241\n~~\t")

    course = course.lower()         # Recieve and modify class input
    course_room = room.get(course)
    course_instructor = instructor.get(course)  # Attempt retrieval of information
    course_time = time.get(course)
    print("\nRoom:", course_room, "\nCourse Instructor:", course_instructor, "\nCourse Time:", course_time)
                                    # Display class information
    if course not in room:          # Check if class exists
        print("This class does not exist.\n")
    check = 1

    while check == 1:
        if check == 1:
            check = input("Enter 1 to continue, Enter 0 to exit program.\n~~\t")    # Get user input for continuation
            try:
                check = int(check)
            except ValueError:
                print("~~ ValueError Raised ~~\n\nInvalid option entered.  Please attempt again.")
            else:
                if check == 0:
                    run = False
        check = 0

print("<<== PROGRAM END ==>>")
