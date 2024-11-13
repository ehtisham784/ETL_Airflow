import pandas as pd
from Extract_Dag import get_linkedin_posts

def transform_function():
    # Define the usernames to fetch posts for
    usernames = ["ehtishamhashmi786", "alisaqlain818", "zaid-farooq-1b129a9b"]

    all_posts = []

    # Loop over the usernames and fetch their posts
    for username in usernames:
        posts = get_linkedin_posts(username)
        all_posts.extend(posts)

    # Create a pandas DataFrame from the extracted data
    linkedin_post_tbl = pd.DataFrame(all_posts)

    # Add a Post_ID column
    linkedin_post_tbl['Post_ID'] = linkedin_post_tbl.index + 1

    # Fill missing values with 0
    linkedin_post_tbl.fillna(0, inplace=True)

    return linkedin_post_tbl
