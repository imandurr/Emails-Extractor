

print('\n  Please read the README file carefully to successfully execute the code \n')

print('\n\t\t Gmail Extractor \n')

# Importing libraries
import imaplib, email
from email.header import decode_header
import re, getpass

username = str(input('Enter your gmail id :'))
password = getpass.getpass(prompt = 'Enter your password :',stream = None)
imap_url = 'imap.gmail.com'

# create an IMAP4 class with SSL
imap = imaplib.IMAP4_SSL("imap.gmail.com")
# authenticate
imap.login(username, password)
print('Login Successful')
status, messages = imap.select("INBOX")
# number of top emails to fetch
N = int(input('Enter the number of email you want to search (from latest to n) : '))
# total number of emails
messages = int(messages[0])

for i in range(messages, messages-N, -1):
    res, msg = imap.fetch(str(i), "(RFC822)")
    for response in msg:

        if isinstance(response, tuple):
            # parse a bytes email into a message object
            msg = email.message_from_bytes(response[1])
            # decode the email subject
            subject = decode_header(msg["Subject"])[0][0]

            if isinstance(subject, bytes):
                subject = subject.decode()
                
            pattern = 'Thank you for applying'
            if re.search(pattern,subject):
                print('\n\n\n----------------------------------\n')
                from_ = msg.get("From")
                print("\n FROM = {} \n subject = {}".format(from_, subject))
                body = ""
                b = msg
                if msg.is_multipart():
                    for part in msg.walk():
                        ctype = part.get_content_type()
                        cdispo = str(part.get('Content-Disposition'))

                        # skip any text/plain (txt) attachments
                        if ctype == 'text/plain' and 'attachment' not in cdispo:
                            body = part.get_payload(decode=True)  # decode
                            break
                # not multipart - i.e. plain text, no attachments
                else:
                    body = msg.get_payload(decode=True)
                print('\n message =', body.decode())
