
from yoomoney import Authorize
import config


Authorize(
    client_id=config.api_ID_YMANI,
    redirect_uri="https://vk.com/club201553116",
    scope=["account-info",
           "operation-history",
           "operation-details",
           "incoming-transfers",
           "payment-p2p",
           "payment-shop",
           ]
    )