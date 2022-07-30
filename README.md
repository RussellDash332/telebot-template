# Telebot Template

A template for myself creating any kinds of Telegram bots.

## Setup

This part assumes you have obtained the bot token and have modified `env.py.example` to the actual `env.py`.

To install all packages and dependencies locally, run the following line.

```bash
pip install -r requirements.txt
```

This file should not be removed so that Heroku can process this part when the bot is just being deployed.

## Boilerplate

The main functions of the bot lies inside `bot.py`. Feel free to expand further and add complexities on your bot.

### Structure of a Telegram update

This is an important section so that you can code the bot interactions easier. For more information, go to https://core.telegram.org/api/updates.

(To convert from `telegram.update.Update` to a Python dictionary or JSON-looking object, use the `__dict__` attribute)

#### Private chat
```json
{
    "update_id": 1,
    "message": {
        "chat": {
            "username": "username",
            "last_name": "lastname",
            "id": 10001,
            "first_name": "firstname",
            "type": "private"
        },
        "new_chat_members": [],
        "delete_chat_photo": false,
        "channel_chat_created": false,
        "message_id": 1,
        "group_chat_created": false,
        "entities": [
            {
                "type": "bot_command",
                "offset": 0,
                "length": 6
            }
        ],
        "date": 100001,
        "text": "/start some extra message here",
        "photo": [],
        "supergroup_chat_created": false,
        "caption_entities": [],
        "new_chat_photo": [],
        "from": {
            "is_bot": false,
            "last_name": "lastname",
            "first_name": "firstname",
            "language_code": "en",
            "id": 10001,
            "username": "username"
        }
    }
}
```

#### Group chat
```json
{
    "update_id": 1,
    "message": {
        "message_id": 1,
        "group_chat_created": false,
        "new_chat_photo": [],
        "chat": {
            "id": -100001,
            "type": "group",
            "title": "group name",
            "all_members_are_administrators": true
        },
        "new_chat_members": [],
        "entities": [
            {
                "length": 6,
                "type": "bot_command",
                "offset": 0
            }
        ],
        "photo": [],
        "supergroup_chat_created": false,
        "caption_entities": [],
        "channel_chat_created": false,
        "date": 100001,
        "text": "/start",
        "delete_chat_photo": false,
        "from": {
            "id": 10001,
            "is_bot": false,
            "language_code": "en",
            "first_name": "firstname",
            "last_name": "lastname",
            "username": "username"
        }
    }
}
```

## Deploying on Heroku

In `Procfile`, make sure you have the line

```
worker: python3 bot.py
```

This tells what Heroku must do upon a deploy command. In this case, I am assigning a worker to run `bot.py`.

Next, create `Pipfile` (and `Pipfile.lock`) by ensuring that `requirements.txt` is existent and running the command below.

```bash
pipenv shell
pipenv install -r requirements.txt
```

Go to **Heroku CLI** (sign up for one :wink:) and create an application by typing the following command.

```bash
heroku create this_is_an_example_application_name
```

Next, create a Git repository (if you haven't), commit all the changes and run this command.

```bash
git push heroku {branch_name}
```

You can omit `{branch_name}` if you are pushing the current branch to Heroku.

### Checking logs

Simply run `heroku logs -t`.
