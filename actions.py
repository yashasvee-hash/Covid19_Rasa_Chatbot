# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher 
import json as json

# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ActionCoronaCount(Action):

     def name(self) -> Text:
         return "action_corona_count"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         response = requests.get("https://api.covid19india.org/data.json").json()
         print()
         
         print("Length", len(response["statewise"]))
         message = "Please enter correct STATE name"

         entities = tracker.latest_message['entities']
         print("Last Message Now", entities)
         state = None
         for e in entities:
             if e['entity'] == "coronaState":
                 state = e['value']

         print("State", state)
         if state == "corona":
             state = "Total"
         if state == "india":
             state = "Total"

         message = "Please enter correct STATE name"
         if (state != None):
             message = "Please enter correct STATE name"
             for data in response["statewise"]:
                 if data["state"] == state.title():
                     print(data)
                     message = "Active: "+data["active"] +" Confirmed: " + data["confirmed"] +" Recovered: " + data["recovered"] +" On "+data["lastupdatedtime"]
         dispatcher.utter_message(message)
         return []