"""Muscrape is a Python package for scraping music data from the web."""
# Path: muscrape/muscrape_init.py

from muscrape.lib.yaml_client import YAMLClient
from muscrape.lib.json_client import JSONClient
from muscrape.lib.search_client import SearchClient

def main():
    """Main function"""
    print("Welcome to Muscrape!")
    config = YAMLClient().load("muscrape/config.yaml")
    if config.get("seed_search_queries") is None:
        print("No seed search queries found in config.yaml")
        return
    search_depth = config["search_depth"]
    search_queries = config["seed_search_queries"]
    debug_level = config["debug_level"]
    search_results_all = []
    for search_query in search_queries:
        search_results = SearchClient().search(search_query, search_depth, debug_level)
        for search_result in search_results:
            if debug_level == "debug":
                print("search_result", search_result.model_dump())
            search_results_all.append(search_result.model_dump())
    # print(len(search_results_all))
    # print("search result all first", search_results_all[0])
    # write search results to json file
    JSONClient().dump("muscrape/data/search_results.json", search_results_all)


if __name__ == "__main__":
    main()
