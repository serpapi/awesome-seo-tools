import urllib.request
import re

def get_keywords(topic):
    try:
        # Encode the user's input for the URL
        encoded_topic = urllib.parse.quote(topic)
        url = f"https://www.google.com/complete/search?q={encoded_topic}&cp=1&client=psy-ab"

        # Send an HTTP GET request and read the response
        with urllib.request.urlopen(url) as response:
            html_content = response.read().decode("utf-8")

        # Use regular expressions to extract keyword suggestions
        suggestions = re.findall(r'"(.*?)"', html_content)

        # Filter out empty and non-alphabetical suggestions
        filtered_suggestions = [s for s in suggestions if s.isalpha()]

        if filtered_suggestions:
            print("Keyword Suggestions:")
            for suggestion in filtered_suggestions:
                print(suggestion)
        else:
            print("No keyword suggestions found for the given topic.")

    except urllib.error.HTTPError as e:
        print(f"HTTP error: {e}")
    except urllib.error.URLError as e:
        print(f"URL error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    topic = input("Enter a topic or industry: ").strip()
    if topic:
        get_keywords(topic)
    else:
        print("Please enter a valid topic.")
