def create_user_accounts():
    """Creates user accounts with specified names and access levels."""

    users = []
    add_more = True

    while add_more:
        try:
            num_users = int(input("How many users would you like to add? "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        for _ in range(num_users):
            name = input("Enter the user's name: ")
            while True:
                access_level = input("Enter the user's access level (admin/standard): ").lower()
                if access_level in ("admin", "standard"):
                    break
                else:
                    print("Invalid access level. Please enter 'admin' or 'standard'.")
            users.append({"name": name, "access_level": access_level})

        while True:
            another = input("Add more users? (yes/no): ").lower()
            if another == "yes":
                break
            elif another == "no":
                add_more = False
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    print("\nUser Accounts:")
    for user in users:
        print(f"Name: {user['name']}, Access Level: {user['access_level']}")

if __name__ == "__main__":
    create_user_accounts()