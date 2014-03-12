email2pwd
=========

email2pwd is a simple password generator that generates passwords based on email addresses.
Options:

-e email_list (required)
-c common_password_list (optional, adds contents of the list to the list of generated passwords)
-o output_file (optional, if omitted defaults to STDOUT)
-s (optional, 'special' means that we want to create a separate password file for each email address)

Examples:

1. Output to file "output.txt"
./email2pwd.py -e emails.txt -o output.txt

2. Output to separate file for each email address
./email2pwd.py -e emails.txt -s

For example, if emails.txt contains email address like "john.smith@acme.lab", email2pwd will create a file named "john.smith@acme.lab.txt" with the following contents:


ACME
Acme
JOHN
John
John.Smith
John123
John123456
John2013
John2014
JohnSmith
SMITH
Smith
Smith123
Smith123456
Smith2013
Smith2014
acme
acme123
acme123456
acme2013
acme2014
john.smith
john123
john123456
john2014
johnsmith
smith123
smith123456
smith2014

If we add "-c" option, every password file will be appended with specified password list. Hint: Google for TOP 100 common passwords.
