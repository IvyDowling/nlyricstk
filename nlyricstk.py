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
            # there are a bunch of credit headers above the songs
            if "[" not in ln:
                # if you leave these in, it naturally breaks lines
                # ln = ln.strip()
                if ln is not "":
                    # splits on words
                    words = re.split('([\w\-\']+)', ln)
                    # delete spaces and empty strings
                    [huge_list.append(w) for w in words
                         if (w is not " " and
                             w is not "" and
                             w is not "(" and
                             w is not ")" and
                             w is not '"')]

    print("Got input file, now generating a song...")
    # 4-gram
    gram_size = 3
    ngram = list(zip(*[huge_list[i:] for i in range(gram_size)]))
    ngram = [list(i) for i in ngram]
    # generate song
    song = ""
    phrase = ngram[rand.randint(0, len(ngram))]
    while True:
        swap = phrase.copy()
        for g in ngram:
            # print(str(g[:-1]) + " " + str(phrase[2:]))
            if g[0] == phrase[-1]:
                phrase.extend(g[1:])
                window = phrase[-(gram_size - 1):]
                rand.shuffle(ngram)
                break
        if swap == phrase:
            for p in phrase:
                song += " " + str(p)
            song += "\n"
            phrase = ngram[rand.randint(0, len(ngram))]


        if len(phrase) > 200:
            for p in phrase:
                song += " " + str(p)
            song += "\n"
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
