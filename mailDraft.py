"""

"""
from jira import JIRA
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass

# JIRA server URL and credentials
JIRA_URL = 'https://your-jira-instance.com'
JIRA_USERNAME = 'your-username'
JIRA_PASSWORD = getpass.getpass("Enter your JIRA password: ")

# Ticket key for the JIRA ticket you want to fetch
ticket_key = 'PROJECT-123'

# Initialize the JIRA client
jira = JIRA(JIRA_URL, basic_auth=(JIRA_USERNAME, JIRA_PASSWORD))

# Get the issue object for the specified ticket
issue = jira.issue(ticket_key)

# Extract the field values
priority = issue.fields.priority
description = issue.fields.description
cause = issue.fields.customfield_10000  # Replace with the actual custom field ID
state = issue.fields.status

# Format the field values into a table
table = f"""
Priority: {priority}
Description: {description}
Cause: {cause}
State: {state}
"""

# Create the email draft
email_subject = f"JIRA Ticket Details: {ticket_key}"
email_body = f"Ticket Key: {ticket_key}\n{table}"

# Set up the email
sender_email = 'your-email@example.com'
receiver_email = 'receiver-email@example.com'

# Create a MIMEText message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = email_subject
message.attach(MIMEText(email_body, 'plain'))

# Connect to the SMTP server
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_username = 'your-smtp-username'
smtp_password = 'your-smtp-password'

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully.")
except Exception as e:
    print(f"An error occurred: {e}")


"""
script will create an email draft and save it to a file named 'email_draft.txt' without sending it. You can review the draft and send it manually or make any modifications you need before sending it.
"""
from jira import JIRA
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
import smtplib

# JIRA server URL and credentials
JIRA_URL = 'https://your-jira-instance.com'
JIRA_USERNAME = 'your-username'
JIRA_PASSWORD = getpass.getpass("Enter your JIRA password: ")

# Ticket key for the JIRA ticket you want to fetch
ticket_key = 'PROJECT-123'

# Initialize the JIRA client
jira = JIRA(JIRA_URL, basic_auth=(JIRA_USERNAME, JIRA_PASSWORD))

# Get the issue object for the specified ticket
issue = jira.issue(ticket_key)

# Extract the field values
priority = issue.fields.priority
description = issue.fields.description
cause = issue.fields.customfield_10000  # Replace with the actual custom field ID
state = issue.fields.status

# Format the field values into a table
table = f"""
Priority: {priority}
Description: {description}
Cause: {cause}
State: {state}
"""

# Create the email draft
email_subject = f"JIRA Ticket Details: {ticket_key}"
email_body = f"Ticket Key: {ticket_key}\n{table}"

# Set up the email
sender_email = 'your-email@example.com'
receiver_email = 'receiver-email@example.com'

# Create a MIMEText message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = email_subject
message.attach(MIMEText(email_body, 'plain'))

# Save the email draft to a file
with open('email_draft.txt', 'w') as email_file:
    email_file.write(message.as_string())

print("Email draft created as 'email_draft.txt'.")
