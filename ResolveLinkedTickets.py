"""
 script will prompt you for your JIRA password, the ticket number to link from ('x'), and the comment ('y'). It will find all linked issues and resolve them with the specified comment.
"""
from jira import JIRA
import getpass

# JIRA server URL and credentials
JIRA_URL = 'https://your-jira-instance.com'
JIRA_USERNAME = 'your-username'
JIRA_PASSWORD = getpass.getpass("Enter your JIRA password: ")

# Prompt the user for the ticket number to link from (x) and the comment (y)
ticket_to_link_from = input("Enter the JIRA ticket number to link from (e.g., PROJECT-123): ")
comment_text = input("Enter the comment to add when resolving linked tickets: ")

# Initialize the JIRA client
jira = JIRA(JIRA_URL, basic_auth=(JIRA_USERNAME, JIRA_PASSWORD))

try:
    # Get the issue object for the specified ticket 'x'
    issue_x = jira.issue(ticket_to_link_from)

    # Search for linked issues
    linked_issues = jira.search_issues(f'linkedIssue = {ticket_to_link_from}')

    # Resolve each linked issue and add the comment
    for issue in linked_issues:
        jira.transition_issue(issue, '5')  # '5' is the transition ID for "Resolved"
        jira.add_comment(issue, comment_text)
        print(f"Resolved {issue.key} and added comment: {comment_text}")

    print(f"Resolved and added comments to {len(linked_issues)} linked issues.")
except Exception as e:
    print(f"An error occurred: {e}")
