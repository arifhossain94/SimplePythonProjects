# List to store membership id, age, and fee
id_list = []
age_list = []
fee_list = []


# Function will be called every time for user interaction until choice 'Exit' or termination
def show_menu():
    print("CLUB MEMBERSHIP TRACKER\n=====================")
    print("1- Add Member\n2- Report\n0- Exit")

    user_input = -1

    while user_input < 0 or user_input > 2:
        user_input = int(input("Choice: "))

    return user_input


def add_member():
    # add id and age
    while True:
        try:
            id_number = int(input("Enter Member ID: "))

            if 0 < id_number:
                id_list.append(id_number)
                break
        except ValueError:
            print("Please input a whole number!")
            continue

    while True:
        try:
            age = int(input("Enter Age: "))

            if age > 0:
                age_list.append(age)

            if age == min(age_list):
                print("You are the youngest member so far.")
            elif age == max(age_list):
                print("You are the oldest member so far.")
            # Monthly Membership Fee
            if age <= 25:
                fee = 30
            elif age >= 55:
                fee = 15
            else:
                fee = 50
            fee_list.append(fee)
            print("Your monthly fee is $", fee, ".")
            break
        except ValueError:
            print("Please give a proper age number!")
            continue


# Function to print records
def report():
    if len(id_list) == 0:
        print("No Record Found!\n")
    else:
        print("There are ", len(id_list), " members.")
        print("Total fees $", sum(fee_list), " from members.")
        print("Average fee per member is $", sum(fee_list) / len(id_list), ".")
        print("Average member age is ", sum(age_list) / len(age_list))
        print("Youngest member is ", min(age_list), " years old.")
        print("Oldest member is ", max(age_list), " years old.")


def start_application():
    # print out the whole menu
    choice = show_menu()

    if choice == 0:
        # If choice == 0, terminate program
        exit()
    elif choice == 1:
        add_member()
    elif choice == 2:
        report()
    print()
    # Calling the same function until choice == 0 (Function Recursion)
    start_application()


# Starting the Application
start_application()