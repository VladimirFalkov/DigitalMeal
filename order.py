import requests
import json
from settings import (
  INSALES_API_URL
                    )


def place_order_by_API():
    api_url = INSALES_API_URL
    order = {
      "order": {
        "order_lines_attributes": [
          {
            "variant_id": 243602670,
            "quantity": 2
          }
        ],
        "client": {
          "name": 'Vladimir',
          "email": "falkoff@mail.ru",
          "phone": "89250998585"
        },
        "shipping_address_attributes": {
          "address": "Красноармейская 29",
          "full_locality_name": "Москва"
        },
        "delivery_variant_id": 2551032,
        "payment_gateway_id": 1348310
      }
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(api_url, data=json.dumps(order), headers=headers)
    response.json()
    print(response.json())
    response.status_code
    print(response.status_code)
    return response.json
# 77277687
