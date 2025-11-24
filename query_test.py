import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import time

# 1. بارگذاری وکتورهای دیتاست
xb = np.load('vectors.npy')
d = xb.shape[1]

# 2. ساختن ایندکس مثل قبل
nlist = 256
m = 16
nprobe = 16

index = faiss.index_factory(d, f"IVF{nlist},PQ{m}")
index.train(xb)
index.add(xb)
index.nprobe = nprobe

print("Index loaded, size:", index.ntotal)

# 3. مدل برای ساخت query embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

# 4. یک سوال نمونه
query = "What is the role of retrieval in large language models?"

# 5. تبدیل سوال به وکتور
q_vec = model.encode(query).astype('float32').reshape(1, -1)

# 6. جستجو
t0 = time.time()
D, I = index.search(q_vec, 5)
t1 = time.time()

print("Query:", query)
print("Retrieved IDs:", I)
print("Latency (ms):", (t1 - t0) * 1000)
