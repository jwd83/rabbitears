import urllib.request


M3U_URL = 'https://iptv-org.github.io/iptv/index.m3u'
LOCAL_FILE = 'index.m3u'

def main():

    urllib.request.urlretrieve(M3U_URL, LOCAL_FILE)

if __name__ == "__main__":
    main()
