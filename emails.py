import requests
from lxml import html


def check_price():
    url = "https://www.amazon.com/Cyber-Acoustics-Headphones-Cancelling-AC-5002/dp/B074JHQ8M3/ref=sr_1_2_sspa?adgrpid=83059415018&gclid=CjwKCAjw7vuUBhBUEiwAEdu2pKbOqAayGKdkTwkmPs08Mxoo6shma6UcuqC__ETAFmTC4c4h_MOTdhoC_b0QAvD_BwE&hvadid=585479825708&hvdev=c&hvlocphy=1010283&hvnetw=g&hvqmt=e&hvrand=11241382114933501914&hvtargid=kwd-324007157714&hydadcr=29109_14574031&keywords=amazon+headset&qid=1654630042&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFJSURRMFhQU1VaSFEmZW5jcnlwdGVkSWQ9QTA5NjE4MTYzMTAzWElGVVQ1S01NJmVuY3J5cHRlZEFkSWQ9QTA5MjQzMDAyQklFNEZQRTVSVU82JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
    r = requests.get(url)
    print(r.text)


if __name__ == "__main__":
    check_price()
