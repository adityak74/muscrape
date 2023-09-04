"""Pytube client"""
from pytube import YouTube
from muscrape.models.youtube_video import YouTubeVideo

class PytubeClient:
    """Pytube client"""
    def __init__(self):
        pass

    def get_video_info(self, url) -> YouTubeVideo:
        """Get video info from url"""
        youtube = YouTube(url)
        return YouTubeVideo(
            date=youtube.publish_date,
            title=youtube.title,
            views=youtube.views,
            duration=youtube.length,
            author=youtube.author,
            thumbnail=youtube.thumbnail_url
        )
