# Emails-Extractor
Scrape emails from an existing gmail address on the basis of their subject containing keywords.

# Objective

Scrape emails from an existing gmail address on the basis of their subject containing keywords for example here I am taking keyword as "Thank you for applying" and categories them into a "job" category using Python.

# Example 
1. User applies for a job and receives a confirmation email. 
2. The subject of the email contains the keywords "Thank you for applying".
3. User applies for n number of jobs and receives n number of emails, subject containing the keywords "Thank you for applying".
4. Filter out all the emails received after applying for a job.

# Requirements before executing the code :
Navigate to see all setting from your gmail page and follow steps listed below:
1. Turn off the 2-step verification for your Gmail.
2. Enable IMAP access from setting in via Gmail.
3. Turn on access to less secure apps.


# Things to note:
1. When running the code for first time a google security check web page might open, click on check activity and again click and accept yes it was me. When running code for first time google might give you multiple security alert.
2. If you run this code on python IDLE password entered might me echoed, so better use the command prompt to run the code.

# Python libraries required :
```python 

import imaplib, email
from email.header import decode_header
import re
```

# Executing the code :
As you run the code :
1. Enter your gmail id. 
2. Enter your password.
3. Enter the number of email you want to search (from latest to n), this will search for n number of emails from the latest to the n.
4. After entering all the required data the code will print all the mails where the subject has keyword "Thank you for applying". The senders id, subject and the body of the mail will be printed.
