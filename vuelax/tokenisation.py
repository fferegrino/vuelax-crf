from nltk.tokenize import TweetTokenizer

TWEET_TOKENIZER = TweetTokenizer()


def index_emoji_tokenize(string, return_flags=False):
    flag = ''
    ix = 0
    tokens, positions = [], []
    for t in TWEET_TOKENIZER.tokenize(string):
        ix = string.find(t, ix)
        if len(t) == 1 and ord(t) >= 127462:  # this is the code for 🇦
            if not return_flags: continue
            if flag:
                tokens.append(flag + t)
                positions.append(ix - 1)
                flag = ''
            else:
                flag = t
        else:
            tokens.append(t)
            positions.append(ix)
        ix = +1
    return tokens, positions

