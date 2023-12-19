import logging
from bank import BankSystem

logging.basicConfig(
    filename="errors.log", level=logging.ERROR, format="%(levelname)s - %(message)s"
)
logging.info("Logging started")

try:
    b = BankSystem("JuBank")

    while True:
        b.print_commands()
        user_choice = input("> ").lower().strip()

        if (user_choice == "create" or user_choice == "login") and not b.has_access():
            if user_choice == "create":
                b.registration()
            else:
                b.login()
        elif user_choice == "logout" and b.has_access():
            b.logout()
        elif user_choice == "check_deposit" and b.has_access():
            b.check_deposit()
        elif user_choice == "top_up" and b.has_access():
            b.top_up()
        elif user_choice == "transactions" and b.has_access():
            b.show_transactions()
        elif user_choice == "transfer" and b.has_access():
            b.transfer()
        elif user_choice == "exit":
            break
        else:
            print("Invalid command.")
            logging.error("Wrong command!")

except Exception as e:
    print(f"An error occurred: {e}")
    logging.exception(f"An error occurred: {e}")

print("Thank you for using our bank! Have a nice day! :)")