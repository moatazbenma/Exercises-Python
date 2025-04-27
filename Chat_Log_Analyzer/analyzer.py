# analyzer.py
from collections import Counter
from datetime import datetime
import re

def count_messages(messages):
    counts = Counter(msg['name'] for msg in messages)
    return counts

def unique_words(messages):
    word_map = {}
    for msg in messages:
        name = msg['name']
        words = re.findall(r'\b\w+\b', msg['message'].lower())
        if name not in word_map:
            word_map[name] = set()
        word_map[name].update(words)
    return word_map

def most_active_hours(messages):
    hour_count = Counter()
    for msg in messages:
        try:
            time_obj = datetime.strptime(msg['datetime'], '%m/%d/%Y, %I:%M %p')
            hour_count[time_obj.hour] += 1
        except ValueError:
            continue
    return hour_count
