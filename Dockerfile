# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables for JIRA credentials
ENV JIRA_URL=https://your-jira-instance.com
ENV JIRA_USERNAME=your-username
ENV JIRA_PASSWORD=your-password
ENV JIRA_PROJECT_KEY=YOUR_PROJECT_KEY

# Set the working directory
WORKDIR /app

# Copy the Python script into the container
COPY your_script.py /app/your_script.py

# Install any dependencies your script may have
# For example, if you're using the 'jira' library
RUN pip install jira

# Run the Python script when the container starts
CMD [ "python", "your_script.py" ]
