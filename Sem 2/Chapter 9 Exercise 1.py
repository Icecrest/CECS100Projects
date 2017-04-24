# Sean Curley
# 015068363
# Project 9
# April 19, 2017

run = True
check = 0

room = {'cs101': '3004',
        'cs102': '4501',
        'cs103': '6755',
        'NT110': '1244',
        'CM241': '1411'}

instructor = {'cs101': 'Haynes',
              'cs102': 'Alvarado',
              'cs103': 'Rich',
              'NT110': 'Burke',
              'CM241': 'Lee'}

time = {'cs101': '8:00 am',
        'cs102': '9:00 am',
        'cs103': '10:00 am',
        'NT110': '11:00 am',
        'CM241': '1:00 pm'}

while run:
    course = input("Enter which class you would like to view:\nCS101\nCS102\nCS103\nNT1102\nCM241\n~~\t")

    print("The class you chose was",course,"\n")
    course = course.lower()
    print("Room:", room.get(course))
    print("Instructor:", instructor.get(course))
    print("Time:", time.get(course))
    if course not in time:
        print("Course does not exist.")
    check = 1
    while check == 1:
        check = input("Enter 1 to continue, 0 to end program.\n")
        try:
            check = int(check)
        except ValueError:
            print("~~ ValueError Raised ~~\nYou entered an invalid number.  Please try again.")

        if check == 0:
            run = False
        check = 0

print("<<== END PROGRAM ==>>")
