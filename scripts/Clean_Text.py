def clean_text(data):
    data_length = []
    lemmatizer = WordNetLemmatizer()
    cleaned_text = []
    for sentence in tqdm(data.posts):
        sentence = sentence.lower()

        #         removing links from text data
        sentence = re.sub('https?://[^\s<>"]+|www\.[^\s<>"]+', ' ', sentence)

        #         removing other symbols
        sentence = re.sub('[^0-9a-z]', ' ', sentence)

        data_length.append(len(sentence.split()))
        cleaned_text.append(sentence)
    return cleaned_text, data_length


