"""

openScraper
============================

Author: 0xPcket
Date: 10.4.2026

============================
"""

# +===============---================+
# + Imports
# +===============---================+
from ast import arg
from unittest import result

from pydantic import BaseModel, ConfigDict
import requests

# +===============---================+
# + Expose
# +===============---================+

__all__ = ['scrape']

# +===============---================+
# + Base Models
# +===============---================+

class arguments(BaseModel):
    limit: int | None = 20
    before: str | None


class new_search(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, frozen=True)
    token: str
    channel_id: str
    arguments: arguments | None

# +===============---================+
# + Api Endpoints
# +===============---================+

host = "https://discord.com"
channel_endpoint = "/api/v9/channels/%d/messages"

# +===============---================+
# + Functions
# +===============---================+

def scrape(args: new_search):
    # Setup
    arguments: dict[str, str | int] | None = {}
    channel = channel_endpoint % int(args.channel_id)

    # Extra arguments parsing
    if args.arguments is not None:
        if args.arguments.limit is not None:
            arguments['limit'] = args.arguments.limit
        elif args.arguments.before is not None:
            arguments['before'] = str(args.arguments.limit)
    else:
        arguments = None

    # Authorization
    headers = {
        "Authorization": f"{args.token}",
    }

    # Requests
    r = None
    if arguments != None:
        r = requests.get(url=f"{host}{channel}", data=arguments, headers=headers)
    else:
        r = requests.get(url=f"{host}{channel}", headers=headers)

    if r.status_code == 200:
        return [True, r.json]

    return [False, None]
