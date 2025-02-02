import os
import requests
from requests.auth import HTTPBasicAuth

WP_URL = os.getenv("WP_URL", "http://localhost/wp-json/wp/v2")
USERNAME = os.getenv("USERNAME", "wordpress")
PASSWORD = os.getenv("PASSWORD", "wordpress")

def get_post(post_id):
    
    response = requests.get(f"{WP_URL}/posts/{post_id}", auth=HTTPBasicAuth(USERNAME, PASSWORD))
    
    if response.status_code == 200:
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