with open(input()) as file, open('forbidden_words.txt') as cenz:
    text = file.read()
    for word in cenz.read().split():
        while word in text.lower():
            pos = text.lower().index(word)
            text = text[:pos] + '*' * len(word) + text[pos + len(word):]
    print(text)