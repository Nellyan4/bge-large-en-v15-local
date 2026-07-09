# bge-large-en-v1.5 local wheel

This package bundles the BAAI/bge-large-en-v1.5 model files into a Python wheel for local/offline use.

Original model: https://huggingface.co/BAAI/bge-large-en-v1.5

Usage:

```python
import bge_large_en_v15_local

model = bge_large_en_v15_local.load()
embeddings = model.encode(["hello world"], normalize_embeddings=True)

