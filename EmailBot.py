import smtplib
from email.message import EmailMessage
import pandas as pd

# Define file paths for the text file and CSV file, input email details and email subjects
file_path = input("Enter the path of the text file containing the email you want to send: ")
csv_path = input("Enter the path of the CSV file containing the list of companies and emails: ")
email = input("Enter the email address you want to send the emails from: ")
subject = input("Enter the subject of the email: ")
password = input("Enter the password for the email address: ")


print("Sending emails...")

# Read the content of the text file
with open(file_path, encoding='utf-8') as file:
    rawcontent = file.read()

# Load the CSV file into a DataFrame
df = pd.read_csv(csv_path)

# Set up the SMTP server
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()  # Start TLS for security

# Log in to the SMTP server using the provided credentials
s.login(email, password)

# Iterate through each row in the DataFrame
for i in range(0, len(df)-1):
    # Extract company name and email from the current row
    company_name = df.loc[i, 'Company']
    company_email = df.loc[i, 'Email']

    # Replace placeholder in the email content with the actual company name
    content = rawcontent.replace("{company_name}", company_name)

    # Create an email message
    msg = EmailMessage()
    msg.set_content(content, subtype='plain', charset='utf-8')
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = company_email

    # Send the email message
    s.send_message(msg)

    print(f"Email sent to {company_name}  Email: {i+1}/{len(df)}")

# Quit the SMTP server
s.quit()