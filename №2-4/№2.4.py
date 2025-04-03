import re

def find_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)

def find_phones(text):
    pattern = r'\+7-\d{3}-\d{3}-\d{2}-\d{2}\b'
    return re.findall(pattern, text)

def find_capital_words(text):
    pattern = r'\b[A-ZА-ЯЁ][a-zа-яё]*\b'
    return re.findall(pattern, text)

with open('text.txt', 'r', encoding='utf-8') as file:
    content = file.read()

emails = find_emails(content)
phones = find_phones(content)
capital_words = find_capital_words(content)

with open('emails.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(emails))

with open('phones.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(phones))

with open('capital_words.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(capital_words))

