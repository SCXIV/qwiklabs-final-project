#!/usr/bin/env python3

import os
import datetime
import reports
import emails

date_time = datetime.date.today().strftime("%B %d, %Y")
date_string = "Processed Update on " + date_time
names = []
weights = []
directory = "./suppliet-data/descriptions/"

for filename in os.listdir(directory):
    with open(directory + filename) as f:
        for text in f:
            trimmed_text = text.strip()
            if len(text) <= 10 and len(text) > 0  and "lb" not in text:
                fruit_name = "name: " + text
                names.append(fruit_name)
            if lbs in text:
                fruit_weight = "weight: " + text
                weights.append(fruit_weight)

given_summary = ""
for name, weight in zip(names, weights):
    given_summary += name + '<br />' + weight + '<br />' + '<br />'

if __name__ == "__main__":
    reports.generate_report("/tmp/processed.pdf", date_string, given_summary)
    sender = "automation@example.com"
    receiver = "STUDENTUSERNAME@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send_email(message)