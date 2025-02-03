import os
import requests
from requests.auth import HTTPBasicAuth

"""
For the script, WordPress must be ran locally. While the GET request works, the POST request does not work
because of the error code 401, which implies that the user is not authenticated. I have checked the username
and password, and observed that they were in the container's database. I have also tried to change the password
inside the database through the terminal, but the error is still existent.

The only possible explanation comes from the fact that while the user is an author, the user does not have the
permission to update the post. Unfortunately, I do not know how to change the user's permission. 

Meanwhile, I feel that the user itself should change their own post so the problem might lie somewhere else.
"""


"""
#Normally, this part would be used to get the environment variables from the Dockerfile.

WP_URL = os.getenv("WP_URL", "http://localhost/wp-json/wp/v2")
USERNAME = os.getenv("USERNAME", "wordpress")
PASSWORD = os.getenv("PASSWORD", "wordpress")
"""

WP_URL = "http://localhost/wp-json/wp/v2"
USERNAME = "PrMine54"
PASSWORD = "wordpress"

def get_post(post_id):
    
    response = requests.get(f"{WP_URL}/posts/{post_id}", auth=HTTPBasicAuth(USERNAME, PASSWORD))
    
    if response.status_code == 200:
        print("Post found succesfully!")
        return response.json()
    
    else:
        print("Error: ", response.status_code)
        return None
    
def update_post(post_id, new_content):
    
    data = {
        "content": new_content
    }
    
    response = requests.post(f"{WP_URL}/posts/{post_id}", auth=HTTPBasicAuth(USERNAME, PASSWORD), json=data)
    
    if response.status_code == 200:
        print("Post updated successfully")
        
    else:
        print("Error: ", response.status_code)
        
#Example

post_id = 1
post = get_post(post_id)

if post:
    
    print("Old Content:", post["content"]["rendered"])
    new_content = "<p>Updated blog post content...</p>"
    update_post(post_id, new_content)