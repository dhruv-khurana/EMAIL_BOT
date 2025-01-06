# EmailBot
This Python script automates the process of sending personalized emails to a list of companies. It reads the email content from a text file and the list of companies and their email addresses from a CSV file. The script then sends the emails using the provided email account.

## How It Works
Input File Paths and Email Details:

The script prompts the user to input the path to the text file containing the email content.
The user is also prompted to input the path to the CSV file containing the list of companies and their email addresses.
The user provides the email address from which the emails will be sent, the subject of the email, and the password for the email account.

### Read Email Content:

The script reads the content of the specified text file.
### Load Company Data:

The script loads the CSV file into a pandas DataFrame to access the company names and email addresses.
### Set Up SMTP Server:

The script sets up an SMTP server connection to Gmail's SMTP server and starts TLS for security.
It logs in to the SMTP server using the provided email address and password.
### Send Emails:

The script iterates through each row in the DataFrame.
For each company, it extracts the company name and email address.
It replaces a placeholder in the email content with the actual company name.
It creates an email message with the personalized content, subject, sender, and recipient.
It sends the email message.

## Example
When prompted, enter the following details:

* Path to the text file containing the email content. (use txtfile.txt as an example)
* Path to the CSV file containing the list of companies and emails. (use mycsv.csv as an example)
* Email address to send the emails from.
* Subject of the email.
* [Password](https://stackoverflow.com/questions/72480454/sending-email-with-python-google-disables-less-secure-apps)
## Requirements
* Python 3.x  
* pandas  
* smtplib  
* email.message

## Note
* Ensure that "Less secure app access" is enabled in your Gmail account settings, or use an app-specific password if you have 2-Step Verification enabled.
Handle your credentials securely and avoid hardcoding them in your scripts.          
* Consider using environment variables or a configuration file to store sensitive information.
* [Visit this link](https://stackoverflow.com/questions/72480454/sending-email-with-python-google-disables-less-secure-apps) to learn more
