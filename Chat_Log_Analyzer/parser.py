# parser.py

def read_chat(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    messages = []

    for line in lines:
        try:
            date_time, rest = line.strip().split('] ', 1)
            date_time = date_time[1:] 
            name, message = rest.split(': ', 1)
            messages.append({
                'datetime': date_time,
                'name': name,
                'message': message
            })
        except ValueError:
            continue  

    return messages
