## chitchat
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt OR ask_whatspossible
    - action_chitchat

## deny ask_whatspossible
* ask_whatspossible
    - action_chitchat
* deny
    - utter_nohelp

## more chitchat
* greet
    - utter_greet
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot  OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot  OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat

## ask_whatspossible
* greet
    - utter_greet
* ask_whatspossible
    - action_chitchat

## ask_whatspossible more
* greet
    - utter_greet
* ask_whatspossible
    - action_chitchat
* ask_whatspossible
    - action_chitchat

## just revenue + confirm
* greet
    - utter_greet
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot  OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
* revenue_search
    - utter_can_do
	- revenue_search_form
	- form{"name": "revenue_search_form"}
	- form{"name": null}
    - action_restart
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just revenue, continue, + confirm
* greet
    - utter_greet
* revenue_search
    - utter_can_do
	- revenue_search_form
	- form{"name": "revenue_search_form"}
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot  OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt OR ask_whatspossible
    - action_chitchat
    - utter_ask_continue_general
* affirm
    - utter_great
    - revenue_search_form
    - form{"name": null}
    - action_restart
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just revenue, don't continue, + confirm
* greet
    - utter_greet
* revenue_search
    - utter_can_do
	- revenue_search_form
	- form{"name": "revenue_search_form"}
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot  OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt OR ask_whatspossible
    - action_chitchat
    - utter_ask_continue_general
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}
    - action_restart
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just revenue (with client already) + confirm
* greet
    - utter_greet
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot  OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
* revenue_search{"client":"pimco"}
	- slot{"client":"pimco"}
	- revenue_search_form
	- form{"name": "revenue_search_form"}
	- form{"name": null}
    - action_restart
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just revenue (with client already)
* greet
    - utter_greet
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot  OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
* revenue_search{"client":"pimco"}
	- slot{"client":"pimco"}
	- revenue_search_form
	- form{"name": "revenue_search_form"}
	- form{"name": null}
    - action_restart
    - utter_ask_feedback

## just revenue
* greet
    - utter_greet
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot  OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
* revenue_search
    - utter_can_do
    - revenue_search_form
    - form{"name": "revenue_search_form"}
    - form{"name": null}
    - action_restart
    - utter_ask_feedback

## just revenue, continue
* greet
    - utter_greet
* revenue_search
    - utter_can_do
	- revenue_search_form
	- form{"name": "revenue_search_form"}
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot  OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt OR ask_whatspossible
    - action_chitchat
    - utter_ask_continue_general
* affirm
    - utter_great
    - revenue_search_form
    - form{"name": null}
    - action_restart
    - utter_ask_feedback

## just revenue, don't continue
* greet
    - utter_greet
* revenue_search
    - utter_can_do
    - revenue_search_form
	- form{"name": "revenue_search_form"}
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot  OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt OR ask_whatspossible
    - action_chitchat
    - utter_ask_continue_general
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}
    - action_restart
    - utter_ask_feedback

## just interest + confirm
* greet
    - utter_greet
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot  OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
* interest_search
    - utter_can_do
	- interest_search_form
	- form{"name": "interest_search_form"}
	- form{"name": null}
    - action_restart
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just interest, continue, + confirm
* greet
    - utter_greet
* interest_search
    - utter_can_do
	- interest_search_form
	- form{"name": "interest_search_form"}
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot  OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt OR ask_whatspossible
    - action_chitchat
    - utter_ask_continue_general
* affirm
    - utter_great
    - interest_search_form
    - form{"name": null}
    - action_restart
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just interest, don't continue, + confirm
* greet
    - utter_greet
* interest_search
    - utter_can_do
	- interest_search_form
	- form{"name": "interest_search_form"}
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot  OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt OR ask_whatspossible
    - action_chitchat
    - utter_ask_continue_general
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}
    - action_restart
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just interest (with client already) + confirm
* greet
    - utter_greet
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot  OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
* interest_search{"client":"pimco"}
	- slot{"client":"pimco"}
	- interest_search_form
	- form{"name": "interest_search_form"}
	- form{"name": null}
    - action_restart
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just interest (with client already)
* greet
    - utter_greet
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot  OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
* interest_search{"client":"pimco"}
	- slot{"client":"pimco"}
	- interest_search_form
	- form{"name": "interest_search_form"}
	- form{"name": null}
    - action_restart
    - utter_ask_feedback

## just interest
* greet
    - utter_greet
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot  OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
* interest_search
    - utter_can_do
    - interest_search_form
    - form{"name": "interest_search_form"}
    - form{"name": null}
    - action_restart
    - utter_ask_feedback

## just interest, continue
* greet
    - utter_greet
* interest_search
    - utter_can_do
	- interest_search_form
	- form{"name": "interest_search_form"}
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot  OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt OR ask_whatspossible
    - action_chitchat
    - utter_ask_continue_general
* affirm
    - utter_great
    - interest_search_form
    - form{"name": null}
    - action_restart
    - utter_ask_feedback

## just interest, don't continue
* greet
    - utter_greet
* interest_search
    - utter_can_do
    - interest_search_form
	- form{"name": "interest_search_form"}
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot  OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt OR ask_whatspossible
    - action_chitchat
    - utter_ask_continue_general
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}
    - action_restart
    - utter_ask_feedback

