# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, ActionExecutionRejection
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from random import randint
from rasa_core_sdk.events import SlotSet, AllSlotsReset, Restarted, ConversationPaused, UserUtteranceReverted
import logging
import json

logger = logging.getLogger(__name__)

class RevenueSearchForm(FormAction):
    """Collects revenue information and provides t clients"""

    def name(self):
        return "revenue_search_form"

    @staticmethod
    def required_slots(tracker):
        return ["client"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "client": [
                self.from_entity(entity="client"),
                self.from_text(intent="revenue_search"),
            ],
        }


    # def validate_client(self, value, dispatcher, tracker, domain):
    #     if any(tracker.get_latest_entity_values("client")):
    #         # entity was picked up, validate slot
    #         return {"client": value}
    #     else:
    #         # no entity was picked up, we want to ask again
    #         dispatcher.utter_template("utter_ask_client", tracker)
    #         return {"client": None}


    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        
        client = tracker.get_slot("client")

        try:            
            utter_message = "Revenue for client '{}' is {}".format(client, randint(100000,1000000))
            dispatcher.utter_message(utter_message) #send the response back to the user	
            return []
        except Exception:
            logger.error(
                "Failed to find revenue. Error: ",
                exc_info=True,
            )
            return []

class InterestSearchForm(FormAction):
    """Collects interest/recommendation information and provides t clients"""

    def name(self):
        return "interest_search_form"

    @staticmethod
    def required_slots(tracker):
        return ["client"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "client": [
                self.from_entity(entity="client"),
                self.from_text(intent="interest_search"),
            ],
        }


    # def validate_client(self, value, dispatcher, tracker, domain):
    #     if any(tracker.get_latest_entity_values("client")):
    #         # entity was picked up, validate slot
    #         return {"client": value}
    #     else:
    #         # no entity was picked up, we want to ask again
    #         dispatcher.utter_template("utter_ask_client", tracker)
    #         return {"client": None}


    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        
        client = tracker.get_slot("client")

        try:            
            utter_message = "There are {} clients interested in '{}'".format(randint(10,20), client)
            dispatcher.utter_message(utter_message) #send the response back to the user	
            return []
        except Exception:
            logger.error(
                "Failed to find interest. Error: ",
                exc_info=True,
            )
            return []

class CreateContactForm(FormAction):
    """Create a contact"""

    def name(self):
        return "create_contact_form"

    @staticmethod
    def required_slots(tracker):
        return ["firstname", 'lastname','primaryemail']

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "firstname": [
                self.from_entity(entity="firstname"),
                self.from_text(intent=["create_contact", "enter_data"]),
            ],
            "lastname": [
                self.from_entity(entity="lastname"),
                self.from_text(intent=["create_contact", "enter_data"]),
            ],
            "primaryemail": [
                self.from_entity(entity="primaryemail"),
                self.from_text(intent=["create_contact", "enter_data"]),
            ],
        }


    # def validate_client(self, value, dispatcher, tracker, domain):
    #     if any(tracker.get_latest_entity_values("client")):
    #         # entity was picked up, validate slot
    #         return {"client": value}
    #     else:
    #         # no entity was picked up, we want to ask again
    #         dispatcher.utter_template("utter_ask_client", tracker)
    #         return {"client": None}


    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        
        email = tracker.get_slot("primaryemail")

        try:            
            utter_message = "Contact created for email id '{}' with id {}.".format(email,randint(10,20))
            dispatcher.utter_message(utter_message) #send the response back to the user	
            return []
        except Exception:
            logger.error(
                "Failed to create a contact. Error: ",
                exc_info=True,
            )
            return []

class ActionRestarted(Action):
    """ This is for restarting the chat"""

    def name(self):
        return "action_restart"

    def run(self, dispatcher, tracker, domain):
        return [Restarted()]

class ActionChitchat(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self):
        return "action_chitchat"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message["intent"].get("name")

        # retrieve the correct chitchat utterance dependent on the intent
        if intent in [
            "ask_builder",
            "ask_weather",
            "ask_howdoing",
            "ask_whatspossible",
            "ask_isbot",
            "ask_howold",
            "ask_languagesbot",
            "ask_time",
            "ask_wherefrom",
            "ask_whoami",
            "handleinsult",
            "nicetomeeyou",
            "telljoke",
            "ask_whatismyname",
            "ask_howbuilt",
            "ask_whoisit",
        ]:
            dispatcher.utter_template("utter_" + intent, tracker)
        return []


class ActionDefaultAskAffirmation(Action):
    """Asks for an affirmation of the intent if NLU threshold is not met."""

    def name(self) -> Text:
        return "action_default_ask_affirmation"

    def __init__(self) -> None:
        import pandas as pd

        self.intent_mappings = pd.read_csv("data/" "intent_description_mapping.csv")
        self.intent_mappings.fillna("", inplace=True)
        self.intent_mappings.entities = self.intent_mappings.entities.map(
            lambda entities: {e.strip() for e in entities.split(",")}
        )

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List["Event"]:

        intent_ranking = tracker.latest_message.get("intent_ranking", [])
        if len(intent_ranking) > 1:
            diff_intent_confidence = intent_ranking[0].get(
                "confidence"
            ) - intent_ranking[1].get("confidence")
            if diff_intent_confidence < 0.2:
                intent_ranking = intent_ranking[:2]
            else:
                intent_ranking = intent_ranking[:1]
        first_intent_names = [
            intent.get("name", "")
            for intent in intent_ranking
            if intent.get("name", "") != "out_of_scope"
        ]

        message_title = (
            "Sorry, I'm not sure I've understood " "you correctly 🤔 Do you mean..."
        )

        entities = tracker.latest_message.get("entities", [])
        entities = {e["entity"]: e["value"] for e in entities}

        entities_json = json.dumps(entities)

        buttons = []
        for intent in first_intent_names:
            logger.debug(intent)
            logger.debug(entities)
            buttons.append(
                {
                    "title": self.get_button_title(intent, entities),
                    "payload": "/{}{}".format(intent, entities_json),
                }
            )

        buttons.append({"title": "Something else", "payload": "/out_of_scope"})

        dispatcher.utter_button_message(message_title, buttons=buttons)

        return []

    def get_button_title(self, intent: Text, entities: Dict[Text, Text]) -> Text:
        default_utterance_query = self.intent_mappings.intent == intent
        utterance_query = (
            self.intent_mappings.entities == entities.keys() & default_utterance_query
        )

        utterances = self.intent_mappings[utterance_query].button.tolist()

        if len(utterances) > 0:
            button_title = utterances[0]
        else:
            utterances = self.intent_mappings[default_utterance_query].button.tolist()
            button_title = utterances[0] if len(utterances) > 0 else intent

        return button_title.format(**entities)



class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List["Event"]:

        # Fallback caused by TwoStageFallbackPolicy
        if (
            len(tracker.events) >= 4
            and tracker.events[-4].get("name") == "action_default_ask_affirmation"
        ):

            dispatcher.utter_template("utter_restart_with_button", tracker)

            return [SlotSet("feedback_value", "negative"), ConversationPaused()]

        # Fallback caused by Core
        else:
            dispatcher.utter_template("utter_default", tracker)
            return [UserUtteranceReverted()]
