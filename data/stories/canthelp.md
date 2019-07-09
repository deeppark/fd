## chitchat
* canthelp
    - utter_canthelp

## greet + canthelp
* greet
    - utter_greet
* canthelp
    - utter_canthelp

## greet + revenue + canthelp + continue
* greet
    - utter_greet
* revenue_search
    - utter_can_do
    - revenue_search_form
    - form{"name": "revenue_search_form"}
* canthelp
    - utter_canthelp
    - utter_ask_continue_general
* affirm
    - utter_great
    - revenue_search_form
    - form{"name": null}
    - action_restart

## greet + revenue + canthelp + don't continue
* greet
    - utter_greet
* revenue_search
    - utter_can_do
    - revenue_search_form
    - form{"name": "revenue_search_form"}
* canthelp
    - utter_canthelp
    - utter_ask_continue_general
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}
    - action_restart

## greet + revenue + canthelp + continue
* greet
    - utter_greet
* interest_search
    - utter_can_do
    - interest_search_form
    - form{"name": "interest_search_form"}
* canthelp
    - utter_canthelp
    - utter_ask_continue_general
* affirm
    - utter_great
    - interest_search_form
    - form{"name": null}
    - action_restart

## greet + interest + canthelp + don't continue
* greet
    - utter_greet
* interest_search
    - utter_can_do
    - interest_search_form
    - form{"name": "interest_search_form"}
* canthelp
    - utter_canthelp
    - utter_ask_continue_general
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}
    - action_restart
