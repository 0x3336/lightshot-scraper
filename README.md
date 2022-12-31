# lightshot-scraper
This Python script generates random URLs in the format "https://prnt.sc/XXXXXX" where XXXXXX is a string of 6 random lowercase letters or numbers, and then sends the URLs to a Discord webhook.

## Requirements

- Python 3.6 or later
- The `requests` library (can be installed with `pip install requests`)

## Usage

1. Replace `YOUR_WEBHOOK_URL_HERE` in the script with the actual URL of your Discord webhook.
2. Run the script: `main.py`
3. Follow the prompts to enter the number of URLs to generate and the delay between each URL.

## Output

The script will generate and send the specified number of URLs to the Discord webhook, with the specified delay between each URL.

## Notes

- The `requests` library is used to make a POST request to the Discord webhook URL with the URL as the message payload.
- The `random` and `string` modules are used to generate the random URLs.
- The `time` module is used to add a delay between each URL.

## Further Reading

- [requests documentation](https://requests.readthedocs.io/)
- [random module documentation](https://docs.python.org/3/library/random.html)
- [string module documentation](https://docs.python.org/3/library/string.html)
- [time module documentation](https://docs.python.org/3/library/time.html)
- [Discord webhooks documentation](https://discordjs.guide/webhooks/)
