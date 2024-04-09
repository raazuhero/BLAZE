# Save this code in a file, for example, user_agent_script.py

from fake_useragent import UserAgent

def get_random_user_agent():
    ua = UserAgent()
    return ua.random

if __name__ == "__main__":
    user_agent = get_random_user_agent()
    print("Random User Agent:", user_agent)
