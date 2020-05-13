class UsefulClass:
    "this class might be usefule to other modules."
    pass


def main():
    "create a useful class and does something with it for our module."
    useful = UsefulClass()
    print(useful)
    print("works!")


if __name__ == "__main__":
    main()


