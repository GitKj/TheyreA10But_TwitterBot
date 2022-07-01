from twitter_client import get_Twitter_Client, get_temp_client
from QuestionGenerator import createFullQuestion
import time

def send_tweet() -> None:
    client = get_temp_client()
    question = createFullQuestion()
    print("Tweeting:  \n")
    print(f"{question}")
    response = client.create_tweet(text=question)
    print(f"https://twitter.com/user/status/{response.data['id']}")


def main():

    
    while True:
    # 4 hours is 7200
        print("Generating tweet...")
        send_tweet()
        time.sleep(7200)


if __name__ == "__main__":
    main()