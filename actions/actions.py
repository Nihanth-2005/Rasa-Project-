from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionTellTime(Action):
    def name(self) -> str:
        return "action_tell_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        now = datetime.now().strftime("%H:%M:%S")
        dispatcher.utter_message(text=f"The current time is {now}")
        return []



class ActionProcessDocument(Action):
    def name(self) -> str:
        return "action_process_document"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):

        url = "https://api.unstructuredapp.io/general/v0/general"
        headers = {
            "Authorization": "Bearer ZFWNuzNwRNgB0qtGcNnTbLvsUooWUv"
        }

        # Open the PDF file
        files = {
            "files": open(r"C:\Users\chips\OneDrive\Desktop\Rasa_bot_folder\actions\debate.pdf", "rb")  # Use your PDF file name
        }

        try:
            response = requests.post(url, headers=headers, files=files)
            if response.status_code == 200:
                data = response.json()
                dispatcher.utter_message(text=f"Processed document: {data}")
            else:
                dispatcher.utter_message(text=f"Error: {response.text}")
        except Exception as e:
            dispatcher.utter_message(text=f"API call failed: {str(e)}")

        return []
