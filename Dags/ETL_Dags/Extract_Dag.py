import requests
import json
import requests

url = "https://linkedin-data-api.p.rapidapi.com/get-profile-posts"
querystring = {"username":"adamselipsky"}
headers = {
	"x-rapidapi-key": "2be0e7b638msh3c059ff1fa1b979p13dcc7jsn2725390790b7",
	"x-rapidapi-host": "linkedin-data-api.p.rapidapi.com"
}

# Function to fetch posts for a given user
def get_linkedin_posts(username):
    params = {"username": username}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = []

        # Extract data from the response and append to posts list
        for post in data['data']:
            posts.append({
                'Total Reactions': post.get('totalReactionCount'),
                'Like Count': post.get('likeCount'),
                'Appreciation Count': post.get('appreciationCount'),
                'Comments Count': post.get('commentsCount'),
                'Posted Date': post.get('postedDate'),
                'Author First Name': post.get('author', {}).get('firstName'),
                'Author Last Name': post.get('author', {}).get('lastName'),
                'Author Username': post.get('author', {}).get('username'),
            })
        # print(posts)
        return posts
    else:
        print("Failed to fetch data")
        return []
# get_linkedin_posts("ehtishamhashmi786")