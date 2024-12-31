from users_classes import Admin, User


def print_delimiter():
    print('=' * 50)


users = []
admin = Admin("Admin", "admin@example.com", "securepassword")
admin.get_info()
print_delimiter()

users.append(admin)

print_delimiter()


users.extend(admin.add_user(
    [
        User("John Doe", "john.doe@example.com", "password123"),
        User("Jane Doe", "jane.doe@example.com", "password123"),
        User("Bob Doe", "bob.doe@example.com", "password123"),
    ]
))
print_delimiter()

for user in users:
    user.get_info()
    print_delimiter()

print_delimiter()
admin.delete_user("John Doe",users)
print_delimiter()

for user in users:
    user.get_info()
    print_delimiter()