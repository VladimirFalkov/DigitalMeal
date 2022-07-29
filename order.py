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
            "variant_id": 77277687,
            "quantity": 2
          }
        ],
        "client": {
          "name": "Vasya",
          "email": "vasya@example.com",
          "phone": "79111112233"
        },
        "shipping_address_attributes": {
          "address": "Moscow, Krasnaya Presna 24",
          "full_locality_name": "г Москва"
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
