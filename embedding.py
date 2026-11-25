from sentence_transformers import SentenceTransformer, util


model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def find_closest(query, sentences):
    embeddings = model.encode(sentences)
    query_embedding = model.encode(query)

    closest_index = 0
    closest_score = -1

    for index, vector in enumerate(embeddings):
        similarity = util.cos_sim(vector, query_embedding).item()

        if similarity>closest_score:
            closest_index = index
            closest_score = similarity

    return sentences[closest_index]



sentences = [
    "That is a happy person",
    "That is a happy dog",
    "That is a very happy person",
    "Today is a sunny day"
]

query = "I love sun"

print(find_closest(query,sentences))