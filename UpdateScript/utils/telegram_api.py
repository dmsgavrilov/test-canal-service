import requests

import config


def send_notify(order_id: int) -> None:
    requests.get(url=config.NOTIFY_URL % order_id)
