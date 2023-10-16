"""
 script will prompt you to enter the number of days ("x") and then resolve all JIRA issues in the "Open" state that were created within the last "x" days.
"""


from jira import JIRA
from datetime import datetime, timedelta

# JIRA server URL and credentials
JIRA_URL = 'https://your-jira-instance.com'
JIRA_USERNAME = 'your-username'
JIRA_PASSWORD = 'your-password'

# Prompt the user for the number of days ("x")
x = int(input("Enter the number of days (x): "))

# Initialize the JIRA client
jira = JIRA(JIRA_URL, basic_auth=(JIRA_USERNAME, JIRA_PASSWORD))

# Calculate the date "x" days ago
x_days_ago = datetime.now() - timedelta(days=x)

# Search for JIRA issues created in the last "x" days that are in the "Open" state
query = f'created >= "{x_days_ago.strftime("%Y-%m-%d")}" AND status = "Open"'
issues = jira.search_issues(query)

# Resolve each issue
for issue in issues:
    jira.transition_issue(issue, '5')  # '5' is the transition ID for "Resolved"
    print(f"Resolved issue {issue.key}")

print(f"Resolved {len(issues)} issues in the 'Open' state created in the last {x} days.")
