import requests

def get_random_joke():
    api_url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad status codes
        joke = response.json()
        print(f"{joke['setup']} - {joke['punchline']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching joke: {e}")

if __name__ == "__main__":
    print("Here's a random joke for you:")
    get_random_joke()
