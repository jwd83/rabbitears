import urllib.request


M3U_URL = 'https://iptv-org.github.io/iptv/index.m3u'
LOCAL_FILE = 'index.m3u'

def update_local_file():
    urllib.request.urlretrieve(M3U_URL, LOCAL_FILE)

def search_local_file():
    print("Enter your search term:")
    search_term = input().strip()
    with open(LOCAL_FILE, "r") as f:
        content = f.readlines()
        for line in content:
            if search_term in line:
                print("Found:", line.strip())

def main():
    while True:
        print("Main Menu\n---------------\n1. Update Local M3U File\n2. Search Local M3U File\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            update_local_file()
        elif choice == "2":
            search_local_file()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
