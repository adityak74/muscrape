"""Main File"""

from muscrape.lib.pytube_client import PytubeClient
from muscrape.lib.search_client import SearchClient

def download_main():
    """Main function"""
    pytube_client = PytubeClient()
    url = "https://www.youtube.com/watch?v=rBk5EKHggKo"
    video_info = pytube_client.get_video_info(url)
    print(video_info)

def main():
    """Main function"""
    search_results = SearchClient().search("hindi music")
    print(len(search_results))

if __name__ == "__main__":
    main()
