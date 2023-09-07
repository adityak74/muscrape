"""Search Client"""

from loguru import logger
from typing import List, Optional
from pytube import Search
from muscrape.models.youtube_video import YouTubeVideo

class SearchClient:
    """Search client class"""

    def __init__(self):
        pass

    def validate_search_query(self, query: str) -> bool:
        """Validate search query"""
        if not query or len(query) < 3:
            return False
        return True
    
    def build_youtube_video_from_result(self, result) -> YouTubeVideo:
        """Build YouTube video from result"""
        youtube_video = YouTubeVideo(
            date=result.publish_date,
            title=result.title,
            views=result.views,
            duration=result.length,
            author=result.author,
            thumbnail=result.thumbnail_url,
            url=result.watch_url
        )
        return youtube_video
    
    def build_from_results(self, results) -> List[YouTubeVideo]:
        """Build from results"""
        youtube_videos = []
        if results is None:
            return youtube_videos
        for result in results:
            youtube_video = self.build_youtube_video_from_result(result)
            youtube_videos.append(youtube_video)
        return youtube_videos

    def search(self, query: str, depth: int, debug_level: str = "info") -> Optional[List[YouTubeVideo]]:
        """Search method"""
        if not self.validate_search_query(query):
            return None
        search = Search(query)
        results = search.results
        if debug_level == "debug":
            logger.debug("Search depth: " + str(depth))
            logger.debug("Search results: " + str(len(search.results)))
        depth = depth - 1
        youtube_videos = []
        if depth > 0:
            for i in range(0, depth):
                search.get_next_results()
                if debug_level == "debug":
                    logger.debug("Search depth: " + str(depth - i - 1))
                    logger.debug("Search results: " + str(len(search.results)))
        youtube_videos.extend(self.build_from_results(results))
        return youtube_videos
