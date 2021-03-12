
import json
from rest_framework import status
from rest_framework.test import APITestCase
from fpApi.models import *


class ReviewTests(APITestCase):
    def setUp(self):

        url = "/register"
        data = {
            "username": "steve",
            "password": "Admin8*",
            "email": "steve@stevebrownlee.com",
            "first_name": "Steve",
            "last_name": "Brownlee",
        }

        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)
        self.token = json_response["token"]
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # create restaurant
        url = "/restaurants"
        data = {
            "name": "Logans Road House"
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response['name'], "Logans Road House")

        # create menu
        url = "/menus"
        data = {
            "rest_id": 1
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response["rest_id"], 1)

        # create menu item
        url = "/menuitems"
        data = {
            "menu_id": 1,
            "name": "Peel n' Eat Shrimp",
            "description": "HELLO",
            "price": 10.99,
            "category": "Appetizer"
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response["menu_id"], 1)
        self.assertEqual(json_response["name"], "Peel n' Eat Shrimp")
        self.assertEqual(json_response["description"], "HELLO")
        self.assertEqual(json_response["price"], 10.99)
        self.assertEqual(json_response["category"], "Appetizer")

    def test_create_review(self):

        url = "/reviews"
        data = {
            "user": 1,
            "rating": 3,
            "comment": "wow this was so good",
            "menu_item_id": 1
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        response = self.client.post(url, data, format='json')

        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json_response["user"], 1)
        self.assertEqual(json_response["rating"], 3)
        self.assertEqual(json_response["comment"], "very wow")
        self.assertEqual(json_response["menu_item_id"], 1)
