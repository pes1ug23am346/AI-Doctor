import os
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

DOCS_PATH = "data/medical_docs"

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

documents = []
file_names = []

for file in os.listdir(DOCS_PATH):

    if file.endswith(".txt"):

        path = os.path.join(
            DOCS_PATH,
            file
        )

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            text = f.read()

            documents.append(text)
            file_names.append(file)

embeddings = model.encode(
    documents
)

embeddings = np.array(
    embeddings
).astype("float32")

index = faiss.IndexFlatL2(
    embeddings.shape[1]
)

index.add(
    embeddings
)

faiss.write_index(
    index,
    "data/medical.index"
)

np.save(
    "data/file_names.npy",
    np.array(file_names)
)

print("FAISS index created")
print("Documents:", len(file_names))
