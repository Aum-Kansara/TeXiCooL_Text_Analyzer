from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag,download

# download required nltk packages
# download stopwords
download('stopwords')

# required for tokenization
download('punkt')
# required for parts of speech tagging
download('averaged_perceptron_tagger')

def removePunctuation(word_list):
    punctuations='''!()-[]{};:'’"\,<>./?@#$%^&*_~'''
    new_list=[]
    for word in word_list:
        temp_word=""
        for char in word:
            if char in punctuations:
                temp_word+=''
            else:
                temp_word+=char
        if temp_word.strip()!='':
            new_list.append(temp_word)
    return new_list

def removeStopWords(word_list):
    stop_words=stopwords.words('english')
    new_list=[]
    for i in word_list:
        if i.strip().lower() in stop_words:
            continue
        new_list.append(i.strip())
    
    return new_list

def getNumberOfSentences(txt):
    return len(sent_tokenize(txt))

def getNumberOfWords(txt):
    return len(removePunctuation(word_tokenize(txt)))

def getWordsPerSentence(txt):
    words_per_sentences=[]
    sentances=sent_tokenize(txt)
    for i in sentances:
        words_per_sentences.append(getNumberOfWords(i))
    return "{:.2f}".format(sum(words_per_sentences)/len(words_per_sentences))

def getCharPerWords(txt):
    char_per_words=[]
    words=word_tokenize(txt)
    for i in words:
        char_per_words.append(getCharacters(i,including_space=True))
    return "{:.2f}".format(sum(char_per_words)/len(char_per_words))

def getCharacters(txt,including_space=False):
    count=0
    if including_space:
        return len(txt)
    for i in txt:
        if i!=' ':
            count+=1
    return count

def getNumberOfParagraph(txt):
    count=1
    for i in range(len(txt)):
        if txt[i]=='\n':
            if i+1<len(txt):
                if txt[i+1]!='\n':
                    count+=1
    return count


def getBagOfWords(word_list):
    bag_of_words=[]
    new_words=[]
    for i in word_list:
        new_words.append(i.lower())
    unique_words=set(new_words)
    for i in unique_words:
        bag_of_words.append(i)
    
    return bag_of_words

def getWordFrequencyList(word_list):
    freq_list=[]
    unique_words=set(word_list)
    for i in unique_words:
        freq_list.append([i,word_list.count(i)])
    
    return sorted(freq_list,key=lambda x:x[1],reverse=True)


def getPOSTaggedWords(word_list):
    return pos_tag(word_list)

if __name__=="__main__":
    text = """Elon Musk has shared a photo of the spacesuit designed by SpaceX. This is the second image shared of the new design and the first to feature the spacesuit's full-body look.\n"""
    
    unique_word_freq=getWordFrequencyList(removeStopWords(removePunctuation(word_tokenize(text))))
    unique_word_list=[i[0] for i in unique_word_freq]
    pos_tagged_words=getPOSTaggedWords(unique_word_list)
    for i in range(len(pos_tagged_words)):
        unique_word_freq[i].append(pos_tagged_words[i][1])
    print(unique_word_freq)