def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])
sentence = input() 
print(reverse_words(sentence))
