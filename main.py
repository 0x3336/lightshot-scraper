import random
import string
import requests
import time

def generate_random_url():
  # Generate a random string of 6 lowercase letters or numbers
  url_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
  return f"https://prnt.sc/{url_suffix}"

def send_url_to_discord(url):
  # Send the URL to the Discord webhook
  webhook_url = "put webhook here"
  requests.post(webhook_url, json={"content": url})

# Prompt the user for the number of URLs to generate and the delay between each URL
num_urls = int(input("Enter the number of URLs to generate: "))
delay = int(input("Enter the delay (in seconds) between each URL: "))

for i in range(num_urls):
  # Generate and send a random URL to the Discord webhook
  send_url_to_discord(generate_random_url())
  # Sleep for the specified delay
  time.sleep(delay)
