import easygui

while True:
    school_name = easygui.enterbox(f"Enter the name of the school",
                                   title="School name")
    maximum_number = easygui.integerbox(f"What is the maximum number of "
                                        f"students allowed per class:\nMust be"
                                        f" a number between 10 and 30",
                                        title="Maximum Class Size",
                                        upperbound=30, lowerbound=10)
    total_students = easygui.integerbox(f"What is the total number of students"
                                        f" at {school_name}:\nMust be a number "
                                        f"between 10 and 1400",
                                        title="Total Roll of School",
                                        upperbound=1400, lowerbound=10)

    teachers_needed = 0
    number_classes_needed = total_students // maximum_number
    print(number_classes_needed)
    extra_students = total_students % maximum_number
    print(extra_students)
    if extra_students != 0:
        teachers_needed = number_classes_needed + 1
        print(teachers_needed)
    else:
        teachers_needed = number_classes_needed
        print(teachers_needed)

    number_teachers = easygui.integerbox(f"How many teachers at {school_name}:"
                                         f"\nMust be a number between 1 and"
                                         f"120", title="Actual Number of "
                                                       "Teachers",
                                         upperbound=120, lowerbound=1)

    if teachers_needed == number_teachers:
        easygui.msgbox(f"You have the perfect amount of teachers needed",
                       title="Perfect Amount")
    elif teachers_needed < number_teachers:
        easygui.msgbox(f"You have too many teachers\nYou could do without "
                       f"{number_teachers - teachers_needed} current teacher/s"
                       , title="Over-staffed")
    else:
        easygui.msgbox(f"You have a shortage of teachers\n You need to hire "
                       f"{teachers_needed - number_teachers} more teacher/s",
                       title="Staff Shortage")

    calculate_exit = easygui.buttonbox(f"Do you want to perform another "
                                       f"calculation", title="More Ratios?",
                                       choices=["Yes", "No"])

    if calculate_exit == "No":
        break
    else:
        continue

easygui.msgbox(f"Goodbye")
