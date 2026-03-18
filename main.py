from database import create_table, create_user, get_users


if __name__ == "__main__":
    create_table()


create_user("Igor", "igor@email.com")

users = get_users()
print(users)