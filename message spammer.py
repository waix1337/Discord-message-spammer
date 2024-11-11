import requests
import sys
import time

class skibidi:

    def __init__(self, token, channel, message):
        self.token = token
        self.channel_id = channel
        self.message = message
        self.headers = {'Authorization': token}
        self.session = requests.Session()

    def _generate_message(self, m1):
        return m1

    def execute(self):
        return self.session.post(f'https://discordapp.com/api/v9/channels/{self.channel_id}/messages', headers=self.headers, json={'content': self._generate_message(self.message)})

    
def main():

    token = "REPLACE WITH YOUR TOKEN"
    channel_id = 123123123123 #replace with channel id you want the message to get spammed in
    message = "your message"

    epicness = skibidi(token, channel_id, message)

    while True:
        epicness.execute()


if __name__ == '__main__':
    main()
