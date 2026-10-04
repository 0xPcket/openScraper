from openscraper.core import request

def main() -> None:
    token = ""
    channel_id = ""

    res = request.scrape(args=request.new_search(token=token, channel_id=channel_id, arguments=None))
    print(res)
