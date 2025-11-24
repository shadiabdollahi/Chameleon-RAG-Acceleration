import numpy as np

np.random.seed(0)

# ابعاد واقعی مدل
d = 384         # ✔ مدل MiniLM نیز 384 است
N = 50000       # تعداد وکتورها

vectors = np.random.randn(N, d).astype('float32')
np.save('vectors.npy', vectors)

print("Saved vectors.npy with shape:", vectors.shape)
