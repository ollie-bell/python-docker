from dotenv import dotenv_values

secrets = dotenv_values(".env.secret")

def main():
    print(secrets["API_KEY"])
    print(secrets["API_SECRET"])

if __name__ == "__main__":
    main()
