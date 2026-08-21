#5-8. Hello Admin
users = ['admin', 'user1', 'user2', 'user3', 'user4']
for user in users:
    if user == 'admin':
        print("Hello Admin, would you like to see a status report?")

    else:
        print(f"Hello {user}, thank you for logging in again.")

#5-9. No Users
if not users:
    print("We need to find some users!")

#5-10. Checking Usernames
current_users = ['user1', 'user2', 'user3', 'user4', 'admin']
new_users = ['user5', 'user6', 'admin', 'user7', 'user8']

for new_user in new_users:
    if new_user in current_users:
        print(f"Sorry, the username '{new_user}' is already taken. Please choose a different username.")
    else:
        print(f"The username '{new_user}' is available.")

current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please choose a different username.")
    else:
        print(f"The username '{new_user}' is available.")

#5-11. Ordinal Numbers
numbers = list(range(1, 9))
for number in numbers:

    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")