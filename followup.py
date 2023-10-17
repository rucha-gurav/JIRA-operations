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

"""
new
"""
import requests
from datetime import datetime
import pytz

# Jira API endpoint and your credentials
jira_url = 'https://your-jira-instance.atlassian.net'
jira_username = 'your-username'
jira_password = 'your-api-token'  # Generate an API token in your Jira account

# Jira issue status and transition ID for "For Review"
status_name = 'For Review'
transition_id = 21  # Replace with the correct transition ID

# Define the Jira REST API URL for searching issues
search_url = f"{jira_url}/rest/api/3/search"

# Create a session to maintain authentication
session = requests.Session()
session.auth = (jira_username, jira_password)

# Define JQL query to find issues in "For Review" status
jql_query = f'project = "Your Project" AND status = "{status_name}"'

# Send a Jira API request to get issues in "For Review" status
response = session.get(search_url, params={'jql': jql_query})
if response.status_code != 200:
    print(f"Failed to retrieve issues: {response.status_code} - {response.text}")
    exit()

data = response.json()

# Function to convert JST time to a datetime object
def convert_to_datetime(jst_time_str):
    jst = pytz.timezone('Asia/Tokyo')
    dt = datetime.fromisoformat(jst_time_str.replace('Z', '+00:00'))
    return jst.localize(dt)

# Loop through the issues and calculate the time in "For Review" status
for issue in data['issues']:
    issue_key = issue['key']
    created_date_str = issue['fields']['created']
    created_date = convert_to_datetime(created_date_str)
    current_date = datetime.now(pytz.utc)
    days_in_status = (current_date - created_date).days

    # Comment on the issue with the number of days in "For Review" status
    comment_url = f"{jira_url}/rest/api/3/issue/{issue_key}/comment"
    comment_body = {
        "body": f"This issue has been in '{status_name}' status for {days_in_status} days."
    }
    comment_response = session.post(comment_url, json=comment_body)
    if comment_response.status_code != 201:
        print(f"Failed to comment on issue {issue_key}: {comment_response.status_code} - {comment_response.text}")
    else:
        print(f"Comment added to issue {issue_key}: {days_in_status} days in '{status_name}' status.")
