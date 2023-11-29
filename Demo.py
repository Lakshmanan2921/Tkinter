def create_usernames(num_usernames):
    usernames = []
    for i in range(1, num_usernames + 1):
        usernames.append(f"user{i}")
    return usernames


def prompt_user_to_choose(usernames):
    print("Choose a username:")
    for i, username in enumerate(usernames, start=1):
        print(f"{i}. {username}")

    choice = input("Enter the number:")
    choice_index = int(choice) - 1

    if choice_index > 0 and choice_index <= len(usernames):
        chosen_username = usernames[choice_index]
        print(f"You have chosen the username: {chosen_username}")
    else:
        print("Invalid choice. Please enter a valid number.")


num_usernames = 5  # Change this to the desired number of usernames
usernames = create_usernames(num_usernames)
prompt_user_to_choose(usernames)
