import requests
import re

# Function to get comments from the API
def get_comments(base_url, subfeddit_id, total_comments, limit):
    comments = []  # List to store all comments
    skip = 0  # Variable to handle pagination

    # Loop until we get the desired number of comments
    while skip < total_comments:
        # Build the API request URL with pagination parameters
        url = f"{base_url}/api/v1/comments/?subfeddit_id={subfeddit_id}&skip={skip}&limit={limit}"
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code != 200:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)  # Print the error message from the API
            break

        data = response.json()  # Parse the response to JSON
        
        # Add only the comments part of the response to the list
        comments.extend(data["comments"])
        
        # Increase skip value to get the next batch of comments
        skip += limit

    # Return only the requested number of comments
    return comments[:total_comments]


# Function to clean the text of each comment
def clean_text(text):
    text = text.lower()  # Convert text to lowercase
    text = re.sub(r'http\S+', '', text)  # Remove links
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove special characters and numbers
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    return text
