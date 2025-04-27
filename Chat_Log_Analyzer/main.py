from parser import read_chat
from analyzer import count_messages, unique_words, most_active_hours

messages = read_chat('sample_chat.txt')


msg_count = count_messages(messages)
print("\n📨 Messages Sent:")
for name, count in msg_count.items():
    print(f"{name}: {count} messages")


word_map = unique_words(messages)
print("\n📝 Unique Words:")
for name, words in word_map.items():
    print(f"{name}: {len(words)} unique words")


hour_map = most_active_hours(messages)
most_active = hour_map.most_common(3)
print("\n⏰ Most Active Hours:")
for hour, count in most_active:
    print(f"{hour}:00 - {count} messages")
