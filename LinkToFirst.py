"""
This script will prompt you for your JIRA password and the ending ticket number ('x'). It will find all JIRA issues created sequentially from the specified ticket and link them as "Relates" issues in the order they were created.
"""
from jira import JIRA
import getpass

# JIRA server URL and credentials
JIRA_URL = 'https://your-jira-instance.com'
JIRA_USERNAME = 'your-username'
JIRA_PASSWORD = getpass.getpass("Enter your JIRA password: ")

# Prompt the user for the ending ticket number 'x'
x = input("Enter the ending ticket number (e.g., PROJECT-123): ")

# Initialize the JIRA client
jira = JIRA(JIRA_URL, basic_auth=(JIRA_USERNAME, JIRA_PASSWORD))

try:
    # Get the issue object for the specified ticket 'x'
    issue_x = jira.issue(x)

    # Get the project key and issue number of the specified ticket 'x'
    project_key, issue_number_x = issue_x.fields.project.key, int(issue_x.fields.issueKey.split('-')[1])

    # Search for issues created sequentially from 'x'
    query = f'project = {project_key} AND issueKey >= {project_key}-{issue_number_x}'
    issues_to_link = jira.search_issues(query)

    # Link the found issues sequentially
    prev_issue = None
    for issue in issues_to_link:
        if prev_issue:
            jira.create_issue_link('Relates', issue, prev_issue)
            print(f"Linked {issue.key} to {prev_issue.key}")
        prev_issue = issue

    print(f"Linked {len(issues_to_link)} issues sequentially to {x}.")
except Exception as e:
    print(f"An error occurred: {e}")
