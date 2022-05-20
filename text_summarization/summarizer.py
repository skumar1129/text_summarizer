import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

def analyze_text(text: str) -> dict: 
    # words and characters we don't care about
    extra_words = list(STOP_WORDS) + list(punctuation) + ['\n']
    nlp = spacy.load('en_core_web_sm')
    docx = nlp(text)
    # create word frequency dictionary
    word_frequencies: dict[str, float] = {}
    for word in docx:
        if word.text.lower() not in extra_words:
            if word.text.lower() not in word_frequencies.keys():
                word_frequencies[word.text.lower()] = 1
            else:
                word_frequencies[word.text.lower()] += 1
    # create headline based on words used most often
    val = sorted(word_frequencies.values())
    max_freq = val[-3:]
    headline = ''
    for word, freq in word_frequencies.items():
        if freq in max_freq:
            headline += f'{word} '
    # create TFIDF dict
    maximum_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequency)
    
    # create sentence strength dict
    sentence_list = [ sentence for sentence in docx.sents ]
    sentence_strength: dict[str, float] = {}
    for sentence in sentence_list:
        for word in sentence:
            if word.text.lower() not in sentence_strength.keys():
                # Hack needed since words in the sentences were not in word frequency dict
                if word.text.lower() not in word_frequencies.keys():
                    continue
                sentence_strength[sentence] = word_frequencies[word.text.lower()]
            else:
                sentence_strength[sentence] += word_frequencies[word.text.lower()]
    # get most important sentences 
    sentence_list = [ sentence for sentence in docx.sents ]
    top_sentences=(sorted(sentence_strength.values())[::-1])
    top30percent_sentence=int(0.3*len(top_sentences))
    top_sent=top_sentences[:top30percent_sentence]
    # create final summary 
    summary = ''
    for sent, strength in sentence_strength.items():
        if strength in top_sent:
            summary += f'{sent} '
    print(summary)
    return {'headline': headline, 'summary': summary}
    