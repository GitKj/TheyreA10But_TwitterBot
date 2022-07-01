from twitter_client import get_Twitter_Client
from QuestionGenerator import createFullQuestion
import time

def send_tweet() -> None:
    client = get_Twitter_Client()
    question = createFullQuestion()
    print("Tweeting:  \n")
    print(f"{question}")
    response = client.create_tweet(text=question)
    print(f"https://twitter.com/user/status/{response.data['id']}")


def main():

    # 2 hours is 7200    
    while True:
        print("Generating tweet...")
        send_tweet()
        time.sleep(7200)


if __name__ == "__main__":
    main()