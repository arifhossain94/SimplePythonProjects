# Simple Restaurant Reservation System with reporting
class RestaurantReservationSystem:
    # initialize table of size 20 -- default value 'AVAILABLE'
    table = ["AVAILABLE"] * 20

    # get table number from input
    @staticmethod
    def __get_table_number():
        while True:
            try:
                table_number = int(input("Choose a Table Number: "))
                if (0 <= table_number <= 19) and type(table_number) is int:
                    return table_number
                else:
                    print("Please Provide a Proper Table Number! (0-19)\n")
                    continue
            except ValueError:
                print("Please Provide Whole Number Within Range!\n")
                continue

    # if reservation is not available go back to main menu
    def __reserve_a_table(self):
        table_number = self.__get_table_number()

        if self.table[table_number] == "AVAILABLE":
            reservation_input = input("Please insert Reservation Name: ")
            self.table[table_number] = reservation_input
            print("Reservation Successful Under", reservation_input, "!\n")
        else:
            print("Sorry, Table is Not Available!\n")

    # take an int input to check if the table number is 'RESERVED' or not
    def __clear_reservation(self):
        while True:
            table_number = self.__get_table_number()

            if self.table[table_number] != "AVAILABLE":
                self.table[table_number] = "AVAILABLE"
                print("Cleared Reservation for Table ", table_number, "!\n", sep="")
                break
            else:
                print("Selected Table Already Available!\n")
                break

    # display table and its availability
    def __report(self):
        for x in range(1, len(self.table)+1):
            print("Table: ", x, "-", self.table[x-1])

        print()

    def start_menu(self):
        welcome_message = "WELCOME TO RESTAURANT RESERVATION SYSTEM!"
        print(welcome_message, "=" * len(welcome_message), sep="\n")
        self.__choice_menu()

    def __choice_menu(self):
        print("Please Choose an Option: ")
        print("1- Reserve a Table\n2- Clear Reservation\n3- Report\n0- Exit ")

        user_input = -1
        while user_input < 0 or user_input > 3:
            user_input = int(input("Please choose "))

        if user_input == 1:
            self.__reserve_a_table()
        elif user_input == 2:
            self.__clear_reservation()
        elif user_input == 3:
            self.__report()
        elif user_input == 0:
            exit()

        self.__choice_menu()


# used to initialize RestaurantReservationSystem object
rrs = RestaurantReservationSystem()
rrs.start_menu()
