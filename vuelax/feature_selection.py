import string

punctuation = set(string.punctuation)


def is_punctuation(token):
    return token in punctuation


def is_numeric(token):
    try:
        float(token.replace(",", ""))
        return True
    except:
        return False


def featurise_token(sentence_tokens, sentence_positions, sentence_pos, current_idx):
    token = sentence_tokens[current_idx]
    position = sentence_positions[current_idx]
    pos = sentence_pos[current_idx]
    token_count = len(sentence_tokens)

    # Shared features across tokens
    features = [
        'bias',
        f'word.lower={token.lower()}',
        f'word.istitle={token.istitle()}',
        f'word.isdigit={is_numeric(token)}',
        f'word.ispunct={is_punctuation(token)}',
        f'word.position={position}',
        f'word.token_count={token_count}',
        f'postag={pos}'
    ]

    if current_idx > 0:  # The word is not the first one...
        prev_token = sentence_tokens[current_idx - 1]
        prev_pos = sentence_pos[current_idx - 1]
        features.extend([
            f'-1:word.lower={prev_token.lower()}',
            f'-1:word.istitle={prev_token.istitle()}',
            f'-1:word.isdigit={is_numeric(prev_token)}',
            f'-1:word.ispunct={is_punctuation(prev_token)}',
            f'-1:postag={prev_pos}'
        ])
    else:
        features.append('BOS')

    if current_idx < len(sentence_tokens) - 1:  # The word is not the last one...
        next_token = sentence_tokens[current_idx + 1]
        next_pos = sentence_pos[current_idx + 1]
        features.extend([
            f'+1:word.lower={next_token.lower()}',
            f'+1:word.istitle={next_token.istitle()}',
            f'+1:word.isdigit={is_numeric(next_token)}',
            f'+1:word.ispunct={is_punctuation(next_token)}',
            f'+1:postag={next_pos}'
        ])
    else:
        features.append('EOS')

    return features


def featurise_sentence(sentence_tokens, sentence_positions, sentence_pos):
    features = []
    for i in range(len(sentence_tokens)):
        features.append(featurise_token(sentence_tokens, sentence_positions, sentence_pos, i))
    return features
