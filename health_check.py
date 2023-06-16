#!/usr/bin/env python3

import shutil
import psutil
import socket
import emails
import os

sender = "automation@example.com"
receiver = "ENTERUSERNAME@example.com"
body = "Please check your system and resolve the issue as soon as possible."

du = shutil.disk_usage("/")
current_du = du.free/du.total * 100

# Checks Disk Usage, Sends an email if available space is less than 20%
if current_du < 20:
    subject = "Error - Available disk space is less than 20%"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)

# Checks CPU usage, sends an email if usage is over 80%
cpu_usage = psutil.cpu_percent(1)
if cpu_usage > 80:
    subject = "Error - CPU usage is over 80%"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)

# Checks available mem, if < 500MB, sends email
memory = psutil.virtual_memory()
x = 500 * 1024 * 1024
if memory.available < x:
    subject = "Error - Available memory is less than 500MB"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)

# Checks hostname, sends email if can't be resolved to 127.0.0.1
hostname = socket.gethostbyname('localhost')
if hostname != '127.0.0.1':
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)
