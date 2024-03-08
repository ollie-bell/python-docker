import os
from dotenv import load_dotenv

load_dotenv(os.getenv("SECRET_ENV_FILE"))

def main():
    print(os.getenv("API_KEY"))
    print(os.getenv("API_SECRET"))

if __name__ == "__main__":
    main()
