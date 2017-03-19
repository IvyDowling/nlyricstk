import sys
import re
from gtts import gTTS
import random as rand
# http://www.nltk.org/api/nltk.html#module-nltk.util

def run(fn, *inputfile):
    huge_list = []
    for f in inputfile:
        this_file = open(f)
        for ln in this_file:
            # \n
            ln = ln.strip()
            ln += " 'END'"
            if ln is not "":
                # splits on words
                words = re.split('([\w\-\']+)', ln)
                # delete spaces and empty strings
                words = [w for w in words
                         if (w is not " " and
                             w is not "" and
                             w is not '"')]
                for w in words:
                    huge_list.append(w)

    print("Got input file, now generating a song...")
    # 4-gram
    gram_size = 3
    ngram = list(zip(*[huge_list[i:] for i in range(gram_size)]))
    ngram = [list(i) for i in ngram]
    # generate song
    #
    song = ""
    phrase = ngram[rand.randint(0, len(ngram))]
    while True:
        if "'END'" in phrase:
            phrase = phrase[0: phrase.index("'END'")]
            phrase.append("\n")
            for p in phrase:
                song += " " + str(p)
            phrase = ngram[rand.randint(0, len(ngram))]
        swap = phrase.copy()
        for g in ngram:
            if g[:-1] == phrase[1:]:
                phrase.append(g[-1])
                window = phrase[-(gram_size - 1):]
        if swap == phrase:
            phrase = ngram[rand.randint(0, len(ngram))]
        if len(song) > 500:
            break
    print(song)
    # tts
    """
    tts = gTTS(text=result.content,lang='en')
    tts.save(result.title + '.mp3')
    """

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        run(sys.argv[1], sys.argv[2])
    else:
        print("try: nlyricstk.py newsong.mp3 *[inputfile.txt] ")
