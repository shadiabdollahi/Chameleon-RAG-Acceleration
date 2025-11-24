import numpy as np
import faiss
import time

# Load the vectors
xb = np.load('vectors.npy')
d = xb.shape[1]

# FAISS parameters
nlist = 256
m = 16
nprobe = 16

print("Training index...")

index = faiss.index_factory(d, f"IVF{nlist},PQ{m}")
index.train(xb)
index.add(xb)

print("Index size:", index.ntotal)

# Query
xq = np.random.randn(5, d).astype('float32')
index.nprobe = nprobe

t0 = time.time()
D, I = index.search(xq, 10)
t1 = time.time()

print("Search results:", I)
print("Average latency (ms):", (t1 - t0) / len(xq) * 1000)
