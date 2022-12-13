import requests

def scrub_followers(username):
  # Use the Instagram API to get a list of the user's followers
  followers = requests.get(f'https://www.instagram.com/{username}/followers/')

  # Use regular expressions to extract the follower usernames from the response
  import re
  follower_usernames = re.findall(r'"username":"([^"]+)"', followers.text)

  # Return the list of follower usernames
  return follower_usernames

# Example usage:
scrubbed_followers = scrub_followers('username')
print(scrubbed_followers)
