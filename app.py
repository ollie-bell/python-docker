import os
from dotenv import dotenv_values

secrets = dotenv_values(os.getenv("SECRET_ENV_FILE"))

def main():
    print(secrets["API_KEY"])
    print(secrets["API_SECRET"])

if __name__ == "__main__":
    main()
