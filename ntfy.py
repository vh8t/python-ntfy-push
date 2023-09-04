""" ntfy.py - a simple python script to send push notifications to ntfy.sh """
import os
import subprocess
import sys

""" Install required modules if not installed """
try:
    import requests
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, "-m", "pip3", "install", "requests"])
    import requests

""" Post message to ntfy.sh server """


def post_message(_server, _message, _title, _priority, _tags):
    _headers = {
        "Title": _title,
        "Priority": _priority,
        "Tags": _tags
    }
    try:
        """ Send POST request to ntfy.sh server """
        requests.post(_server, data=_message, headers=_headers)
    except Exception as e:
        """ Print error and exit if something went wrong """
        print(e)
        exit(1)


""" Mapping of tags and priorities """
ntfy = """
        _     __
 _ __  | |_  / _| _   _
| '_ \ | __|| |_ | | | |
| | | || |_ |  _|| |_| |
|_| |_| \__||_|   \__, |
                  |___/
"""
tags_mapping = {
    "+1": "👍",
    "partying_face": "🥳",
    "tada": "🎉",
    "heavy_check_mark": "✔️ ",
    "loudspeaker": "📢",
    "-1": "👎️",
    "warning": "⚠️ ",
    "rotating_light": "🚨",
    "triangular_flag_on_post": "🚩",
    "skull": "💀",
    "facepalm": "🤦",
    "no_entry": "⛔",
    "no_entry_sign": "🚫",
    "cd": "💿",
    "computer": "💻",
}
priorities_mapping = {
    "max/urgent": "5",
    "high": "4",
    "default": "3",
    "low": "2",
    "min": "1"
}

""" Ask user for essential information """
os.system("clear")
s = input(f"{ntfy}\nDo you use default ntfy.sh server? (y/n): ")
os.system("clear")

if s.lower() == "y":
    server = input(f"{ntfy}\nA topic this message will be sent to\n Topic: ")
    server = f"https://ntfy.sh/{server}"
elif s.lower() == "n":
    server = input(f"{ntfy}\nA server this message will be sent to\n Server: ")
else:
    print(ntfy)
    print(f"Invalid input {s}!")
    exit(1)
os.system("clear")

title = input(f"{ntfy}\nA title of the push notification\n Title: ")
os.system("clear")

message = input(f"{ntfy}\nA message of the push notification\n Message: ")
os.system("clear")

priority = input(f"{ntfy}\nA priority of this message (to see all priorities type show)\n Priority: ")
os.system("clear")
if priority.lower() == "show":
    print(ntfy)
    print("\n".join([f"ID: {_id}   Name: {priority}" for priority, _id in priorities_mapping.items()]))
    priority = input(f"\nA priority of this message (either ID or Name)\n Priority: ")
    os.system("clear")

if priority.lower() not in priorities_mapping.keys():
    print(ntfy)
    print(f"Invalid priority {priority}!")
    exit(1)
if priority.lower() not in priorities_mapping.values():
    print(ntfy)
    print(f"Invalid priority {priority}!")
    exit(1)

tags = input(f"{ntfy}\nTags for the push notification, separate by ',' (to see all tags type show)\n Tags: ")
os.system("clear")
if tags.lower() == "show":
    print(ntfy)
    print("\n".join([f"Emoji: {emoji}   Tag: {tag}" for tag, emoji in tags_mapping.items()]))
    tags = input(f"\nTags for the push notification, separate by ',' (only Name)\n Tags: ")
    os.system("clear")

""" Check if all tags are valid """
_tags = tags.split(",")
for tag in _tags:
    """ Remove any whitespaces """
    tag.strip()
    if tag.lower() not in tags_mapping.keys():
        print(ntfy)
        print(f"Invalid tag {tag}!")
        exit(1)

""" Send POST request to ntfy.sh server """
post_message(server, message, title, priority, tags)
