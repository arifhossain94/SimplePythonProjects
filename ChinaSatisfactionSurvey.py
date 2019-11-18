import sys

rating_records = []


def start_message():
    print("Welcome to China Border Protection\n===== Satisfaction Survey ========")
    print("1- Submit Rating\n2- View Rating\n3- Reset Rating\n0- Exit ")

    user_input = -1

    while user_input < 0 or user_input > 3:
        user_input = int(input("Your Choice? "))

    return user_input


def submit_rating():
    global rating

    while True:
        try:
            rating = int(input("Your rating (1-4)? "))

            if 1 <= rating <= 4:
                rating_records.append(rating)
                break
            else:
                print("Printing our of bound...Please choose again!")
            continue
        except ValueError:
            print("Please Choose a Whole Number")
            continue

    return rating


def view_ratings():
    if len(rating_records) == 0:
        print("There are no rating for this officer yet.")
    else:
        print("Highest Rating: ", max(rating_records))
        print("Lowest Rating: ", min(rating_records))
        print("Average Rating: ", round(sum(rating_records) / len(rating_records)))


def reset_rating():
    rating_records.clear()
    print("The ratings for this officer is reset.")


def start_survey():
    choice = start_message()

    if choice == 0:
        sys.exit()
    elif choice == 1:
        submit_rating()
    elif choice == 2:
        view_ratings()
    else:
        reset_rating()

    print()
    # Calling the same method until choice == 0
    start_survey()


start_survey()