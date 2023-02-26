from flask import Flask,render_template,request
from Tokenizer import *
app=Flask(__name__)


@app.route("/",methods=["GET","POST"])
def hello_world():
    if request.method=="POST":
        text=request.form.get('input_para')
        if text.strip()!='':
            no_of_sentences=getNumberOfSentences(text)
            no_of_para=getNumberOfParagraph(text)
            no_of_words=getNumberOfWords(text)
            char_with_space=getCharacters(text,including_space=True)
            char_without_space=getCharacters(text)
            words_per_sentence=getWordsPerSentence(text)
            char_per_words=getCharPerWords(text)
            unique_word_freq=getWordFrequencyList(removeStopWords(removePunctuation(map(lambda x:x.lower(),word_tokenize(text)))))
            unique_word_list=[i[0] for i in unique_word_freq]
            pos_tagged_words=getPOSTaggedWords(unique_word_list)
            for i in range(len(pos_tagged_words)):
                unique_word_freq[i].append(pos_tagged_words[i][1])
            return render_template("index.html",output="1",no_of_sentences=no_of_sentences,no_of_para=no_of_para,no_of_words=no_of_words,char_with_space=char_with_space,char_without_space=char_without_space,words_per_sentence=words_per_sentence,char_per_words=char_per_words,pos_tagged_words=unique_word_freq)
    return render_template("index.html",output=None)

if __name__=="__main__":
    app.run()