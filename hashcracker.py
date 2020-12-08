import csv


def main():
    with open('userhashes512.csv', 'r', newline='') as userhash:
        fieldnamesTop10 = ['unhashed_passwords', 'sha512-hashed_passwords']
        fieldnamesUserHash = ['users', 'hashed_passwords']
        ureader = csv.DictReader(userhash, fieldnames=fieldnamesUserHash)
        for urow in ureader:
            with open('top10k512.csv', 'r', newline='') as top10k:
                hreader = csv.DictReader(top10k, fieldnames=fieldnamesTop10)
                for hrow in hreader:
                    if urow['hashed_passwords'] == hrow['sha512-hashed_passwords']:
                        print("===[MATCH]===\nUsername: "+urow['users']+"\nPassword(hashed): "+urow['hashed_passwords']
                              +"\nPassword(plaintext): "+hrow["unhashed_passwords"]+"\n\n")
                        break




if __name__ == '__main__':
    main()
