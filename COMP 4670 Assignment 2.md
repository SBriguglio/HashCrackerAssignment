# COMP 4670: Assignment 2

### Spencer Briguglio

## Question 1: RSA Public/Private Key Generation, Encryption and Decryption

This program, written in Python 3.8, contains 3 methods, RSA_Keygen(), RSA_Encryption(), and RSA_Decryption(), in addition to a main method. The main method generates a list of primes and then asks the user for an input string to encrypt and decrypt. The main method chooses two primes at random and first uses them to create a public and private key. These keys are then used to encrypt and decrypt the input message, respectively.

Below is sample output showing each step.

1. RSA_Keygen


2. RSA_ Encryption


3. RSA_Decryption


4. Summary of results


## Question 2: Hash Cracker

For this section, I began by acquiring a list of the top 10,000 most common passwords from a git repository found here: https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt. I created a small program written in Python to create a dictionary CSV file which had two columns. The first column was each of the 10000 passwords in plaintext and the second column was their SHA-512 hashed value. I also created another small program to produce a CSV with usernames and hashed passwords to stand in for a stolen list from a company database.

After producing a dictionary and stolen user login details, I used my hash cracker program (hashcracker.py) to compare hashed password against the dictionary and print matches along with the plaintext password. For simplicities sake, I name all the hits that I had added to the userdata, some variation of Hit1 or Hit2. 

As hoped, the hash cracker compare the SHA-512 hashed passwords against the dictionary and detected the matched. A screen shot of the output is included below.


For reference, I've included the hashcraker.py code below:

```python
import csv


def main():
    # userhashes512.csv contains the usernames with SHA-512 hashed passwords
    with open('userhashes512.csv', 'r', newline='') as userhash:
        fieldnamesTop10 = ['unhashed_passwords', 'sha512-hashed_passwords']
        fieldnamesUserHash = ['users', 'hashed_passwords']
        ureader = csv.DictReader(userhash, fieldnames=fieldnamesUserHash)
        for urow in ureader:
            # top10k512.csv contains the dictionary of the 10000 most commonly used passwords all hashed via SHA-512
            with open('top10k512.csv', 'r', newline='') as top10k:
                hreader = csv.DictReader(top10k, fieldnames=fieldnamesTop10)
                for hrow in hreader:
                    #if a match is found, prints the username, hash password and plaintext password
                    if urow['hashed_passwords'] == hrow['sha512-hashed_passwords']:
                        print("===[MATCH]===\nUsername: "+urow['users']+"\nPassword(hashed): "+urow['hashed_passwords']
                              +"\nPassword(plaintext): "+hrow["unhashed_passwords"]+"\n\n")
                        break



if __name__ == '__main__':
    main()
```

