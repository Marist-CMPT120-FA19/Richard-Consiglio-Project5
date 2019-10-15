def sentenceStatistics():
    sentence = input("Enter a sentence to get stats: ")
    print("the amount of characters in your sentence is")
    print(len(sentence))
    print ("the amount of words in your sentence is")
    print(len(sentence.split()))
    print("the average word length in your sentence is")
    words = sentence.split()
    wordCount = len(words)
    sum = 0
    for word in words:
        ch = len(word)
        sum = sum + ch
    avg = sum / wordCount
    if avg is 1:
        print ("In the sentence the average word length is", avg,"letter.")
    else:
        print ("In the sentence the average word length is", avg,"letters.")
sentenceStatistics()
