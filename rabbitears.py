import requests
M3U_URL = 'https://iptv-org.github.io/iptv/index.m3u'

def get_m3u(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def main():
    m3u_content = get_m3u(M3U_URL)
    if not m3u_content:
        print("Failed to retrieve M3U content.")
    else:
        print("M3U content retrieved successfully.")

if __name__ == "__main__":
    main()