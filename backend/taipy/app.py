import json
import time
import openai
import requests
import pandas as pd
from taipy.gui import Gui, notify

openai.api_key = "[redacted]"
INITIAL_PROMPT = "You are an assistant that gives details about blockchain "
MAX_TOKENS = 150


def generate_completion(messages, model="gpt-3.5-turbo", temperature=1):
    print(messages)
    res = openai.ChatCompletion.create( 
        model=model,
        messages=messages)
    print(res)
    return res['choices'][0]['message']['content']

saved_messages = [
    {"role": "system", "content": INITIAL_PROMPT},
]

user_message = ""


def messages_to_data(messages):
    result = []
    for message in messages:
        result_message = {}
        result_message["Role"] = message["role"]
        result_message["Message"] = message["content"]
        if result_message["Role"] == "system":
            result_message["Role"] = "GPT-4"
        else:
            result_message["Role"] = "You"
        result.append(result_message)
    return pd.DataFrame(result)


def on_send_click(state):
    notify(state, "info", "Generating response...")
    message = state.user_message
    message = message.strip('\n')
    state.saved_messages.append({"role": "user", "content": message})
    state.saved_messages = state.saved_messages
    state.user_message = ""
    time.sleep(0.1)
    response = generate_completion(state.saved_messages)
    state.saved_messages.append({"role": "system", "content": response})
    state.saved_messages = state.saved_messages
    notify(state, "success", "GPT-4 generated a response!")


page = """
# Chat with **GPT-3**{: .color-primary}

<|{messages_to_data(saved_messages)}|table|show_all|width=100%|>

<br/>

<|{user_message}|input|multiline=True|lines_shown=2|label=Your Message|class_name=fullwidth|>

<|Send|button|on_action=on_send_click|>
"""

Gui(page).run()