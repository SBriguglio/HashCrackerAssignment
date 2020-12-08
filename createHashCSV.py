import csv
import hashlib


def main():
    with open('userhashes512.csv', 'w', newline='') as csvfile:
        fieldnames = ['users', 'hashed_passwords']
        line = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for i in range(20):
            username = input("username: ")
            password = input("password: ")
            hashed = hashlib.sha512(password.encode()).hexdigest()
            line.writerow({'users': username, 'hashed_passwords': hashed})


if __name__ == '__main__':
    main()