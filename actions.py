# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

import pandas as pd
import os
# This is a simple example for a custom action which utters "Hello World!"
from tkinter import EventType
from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction





class ActionSaveData(Action):

    def name(self) -> Text:
        return "action_save_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        DataStore()

        dispatcher.utter_message(text="Data Store Succesfully!")

        return []

class FormDataCollect(FormAction):
    def name(self) -> Text:
        return "Form_info"

    @staticmethod
    def required_slots(tracker:"Tracker") -> List[Text]:
        return ["name","phone_number","email_id","occupation"]

    def slot_mappings(self) -> Dict[Text,Union[Dict,List[Dict[Text,Any]]]]:
        return {
            "name":[self.from_text()],
            "phone_number":[self.from_entity(entity="phone_number")],
            "email_id":[self.from_entity(entity="email_id")],
            "occupation":[self.from_text()],
        }

    def submit(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        dispatcher.utter_message("Here re the information that your provided..Do you wnt to save it?\nName:{0},\nMobile Number:{1},\nEmail:{2},\nOccupation:{3}".format(
            tracker.get_slot("name"),
            tracker.get_slot("phone_number"),
            tracker.get_slot("email_id"),
            tracker.get_slot("occupation"),
        ))
        return []

def DataStore(name, phone_number, email_id, occupation):
    if os.path.isfile("user_data.xlsx"):
        df = pd.read_excel("user_data.xlsx")
        df.append([name, phone_number, email_id, occupation])
        df.to_excel("user_data.xlsx", index=False)
    else:
        df = pd.DataFrame([name, phone_number, email_id, occupation],
                          columns=["name", "phone_number", "email_id", "occupation"])
        df.to_excel("user_data.xlsx", index=False)
