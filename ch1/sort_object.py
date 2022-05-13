# Sorting objects Without Native Comparison Support using attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def main():
    from operator import attrgetter

    users = [User(23), User(3), User(5)]
    sorted_users =sorted(users, key=lambda u: u.user_id)

    print(users) # [User(23), User(3), User(5)]
    print(sorted_users) # [User(3), User(5), User(23)]




if __name__ == "__main__":
    main()
