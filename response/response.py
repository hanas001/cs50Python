import re
import validators

def main():
    email = input("What's your email address? ")
    # validate_email(email)
    if validators.email(email):
        print('Valid')
    else:
        print('Invalid')
def validate_email(email):
    pattern = r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
    if re.match(pattern, email):
        print('Valid')
    else:
        print('Invalid')


if __name__ == "__main__":
    main()