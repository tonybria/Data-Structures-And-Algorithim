import string

def word_frequency(sentence):
    words = sentence.translate(str.maketrans("","",string.punctuation))
    words = words.lower().split()

    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)