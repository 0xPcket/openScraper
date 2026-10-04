from openscraper.core import request

def main() -> None:
    request.scrape(args=request.new_search(token="abcdefghijklmnopqrstuvwxyz", channel_id="12345678901234567890", arguments=None))
