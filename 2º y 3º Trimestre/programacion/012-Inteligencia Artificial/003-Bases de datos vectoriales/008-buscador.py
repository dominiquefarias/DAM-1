#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import math
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

def cosine_similarity(a, b) -> float:
    dot = 0.0
    na = 0.0
    nb = 0.0
    for x, y in zip(a, b):
        dot += x * y
        na += x * x
        nb += y * y
    denom = math.sqrt(na) * math.sqrt(nb)
    return dot / denom if denom != 0.0 else 0.0

def clamp01(x: float) -> float:
    if x < 0.0:
        return 0.0
    if x > 1.0:
        return 1.0
    return x

def main():
    # Debe coincidir con el script de inserción
    persist_dir = os.path.abspath("./chroma_data")
    collection_name = "sentencias_es"

    # Modelo (mismo que usaste para insertar; así es consistente)
    model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

    # Abrir Chroma
    client = chromadb.PersistentClient(
        path=persist_dir,
        settings=Settings(anonymized_telemetry=False)
    )
    collection = client.get_collection(name=collection_name)

    # Cargar todas las frases almacenadas + embeddings
    stored = collection.get(include=["documents", "embeddings", "ids", "metadatas"])
    docs = stored.get("documents") or []
    embs = stored.get("embeddings") or []
    ids = stored.get("ids") or []

    if not docs or not embs:
        print("No hay frases almacenadas en la colección. Inserta primero con el script de inserción.")
        return

    print(f"Cargadas {len(docs)} frases desde Chroma ({collection_name})")
    print("Escribe una frase para comparar (ENTER para salir)\n")

    while True:
        query = input("Tu frase> ").strip()
        if not query:
            print("Saliendo.")
            break

        q_emb = model.encode(query, normalize_embeddings=True).tolist()

        # Similitud con cada frase (coseno) -> porcentaje
        scored = []
        for doc_id, doc, emb in zip(ids, docs, embs):
            sim = cosine_similarity(q_emb, emb)  # en [-1,1] (normalmente >= 0 en este caso)
            pct = clamp01(sim) * 100.0           # lo mostramos como 0..100%
            scored.append((pct, doc_id, doc))

        # Ordenar por mayor similitud
        scored.sort(reverse=True, key=lambda x: x[0])

        print("\nSimilitudes (mayor -> menor):")
        for pct, doc_id, doc in scored:
            print(f"- {pct:6.2f}%  ({doc_id})  {doc}")

        print()

if __name__ == "__main__":
    main()