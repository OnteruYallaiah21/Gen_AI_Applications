from gensim.models import Word2Vec


sentences = [
    ["the", "boy", "is", "playing", "with", "the", "ball"],
    ["the", "girl", "is", "playing", "with", "the", "doll"],
    ["the", "king", "is", "sitting", "on", "his", "throne"],
    ["the", "queen", "is", "ruling", "the", "kingdom"],
    ["the", "mango", "is", "sweet", "and", "ripe"],
    ["the", "apple", "is", "red", "and", "juicy"]
]

# Train Word2Vec model
model = Word2Vec(sentences, min_count=1, vector_size=50, window=3, sg=1)

# Check vector for "king"
print("Vector for 'king':", model.wv['king'])

# Find words similar to "king"
similar_words = model.wv.most_similar('king', topn=3)
print("Words similar to 'king':", similar_words)
