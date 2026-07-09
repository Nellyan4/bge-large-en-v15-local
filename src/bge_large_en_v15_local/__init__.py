from importlib.resources import files
from sentence_transformers import SentenceTransformer


def model_path() -> str:
    return str(files("bge_large_en_v15_local").joinpath("model"))


def load(**kwargs):
    return SentenceTransformer(model_path(), **kwargs)
