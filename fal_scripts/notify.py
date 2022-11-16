import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

CHANNEL_ID = os.getenv("SLACK_BOT_CHANNEL")
SLACK_TOKEN = os.getenv("SLACK_BOT_TOKEN")

assert (
    CHANNEL_ID and SLACK_TOKEN
), "warning: CHANNEL_ID and/or SLACK_TOKEN is not set, so can't send a message"

client = WebClient(token=SLACK_TOKEN)
message_text = (
    f"Model: {context.current_model.name}. Status: {context.current_model.status}."
)

try:
    response = client.chat_postMessage(channel=CHANNEL_ID, text=message_text)
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"]
