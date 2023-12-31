"""Muscrape is a Python package for scraping music data from the web."""
# Path: muscrape/muscrape_init.py

import random
from loguru import logger
from dotenv import load_dotenv
from muscrape.lib.yaml_client import YAMLClient
from muscrape.lib.json_client import JSONClient
from muscrape.lib.search_client import SearchClient

load_dotenv()

def start():
    """Main function"""
    logger.info("Starting Muscrape")
    config = YAMLClient().load("muscrape/config.yaml")
    if config.get("seed_search_queries") is None:
        logger.error("No seed search queries found in config.yaml")
        return
    search_depth = config["search_depth"]
    search_queries = config["seed_search_queries"]
    random.shuffle(search_queries)
    total_search_queries = len(search_queries)
    logger.info("Searching for " + str(total_search_queries) + " search queries")

    i = 0
    debug_level = config["debug_level"]
    search_results_all = []
    for search_query in search_queries:
        logger.info(str(i) + "/" + str(total_search_queries))
        try:
            search_results = SearchClient().search(search_query, search_depth, debug_level)
            for search_result in search_results:
                if debug_level == "debug":
                    logger.debug("Search result: " + str(search_result.model_dump()))
                search_results_all.append(search_result.model_dump())
            i += 1
            # save search queries to temporary file
            JSONClient().dump("muscrape/data/search_results_temp.json", search_results_all)
        except Exception as e:
            print("Exception e as :", e)
            logger.info("Exception found in searching, so skipping query : " + search_query)
    # write search results to json file
    JSONClient().dump("muscrape/data/search_results.json", search_results_all)
    logger.info("Search results written to muscrape/data/search_results.json")


if __name__ == "__main__":
    start()
