import requests

def top_ten(subreddit):
        """Print the titles of the first 10 hot posts in the given subreddit."""
            url = f"https://www.reddit.com/r/{subreddit}/hot.json"
                headers = {
                                "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
                                    }
                    
                    response = requests.get(url, headers=headers, allow_redirects=False)
                        
                            if response.status_code == 404:
                                        print("None")
                                                return
                                                
                                                try:
                                                            data = response.json().get("data")
                                                                    if "children" in data:
                                                                                    for post in data["children"][:10]:
                                                                                                        print(post["data"]["title"])
                                                                                                            except Exception as e:
                                                                                                                        print("An error occurred:", e)

                                                                                                                        if __name__ == "__main__":
                                                                                                                                import sys
                                                                                                                                    
                                                                                                                                        if len(sys.argv) < 2:
                                                                                                                                                    print("Please pass an argument for the subreddit to search.")
                                                                                                                                                        else:
                                                                                                                                                                    top_ten(sys.argv[1])

