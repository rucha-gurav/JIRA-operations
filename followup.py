from jira import JIRA
from datetime import datetime

# JIRA server URL and credentials
JIRA_URL = 'https://your-jira-instance.com'
JIRA_USERNAME = 'your-username'
JIRA_PASSWORD = 'your-password'

# Initialize the JIRA client
jira = JIRA(JIRA_URL, basic_auth=(JIRA_USERNAME, JIRA_PASSWORD))

# Get all issues from your JIRA project in "Open" state
issues = jira.search_issues('project=YOUR_PROJECT_KEY AND status=Open', maxResults=None)

for issue in issues:
    # Get the issue creation date
    created_date = jira.issue(issue).fields.created
    # Calculate the number of days since the ticket was created
    days_since_creation = (datetime.now() - created_date).days

    # Compose the comment text
    comment_text = f'No response since last {days_since_creation} days.'

    # Add the comment to the issue
    jira.add_comment(issue, comment_text)
    print(f'Comment added to {issue.key}: {comment_text}')
