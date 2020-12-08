import csv
import hashlib


def main():
    with open('top.txt', 'r', newline='') as top10k, open ('top10k1.csv', 'w', newline='') as csvfile:
        fieldnames = ['unhashed_passwords', 'sha1-hashed_passwords']
        line = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for i in range(10000):
            read = top10k.readline()
            size = len(read)
            read = read[0:size-2]
            hashed = hashlib.sha1(read.encode()).hexdigest()
            line.writerow({'unhashed_passwords': read, 'sha1-hashed_passwords': hashed})


if __name__ == '__main__':
    main()