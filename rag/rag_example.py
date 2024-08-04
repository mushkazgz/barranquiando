from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration

# Cargar el tokenizer
tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-base")

# Cargar el retriever
retriever = RagRetriever.from_pretrained("facebook/rag-token-base", index_name="exact", use_dummy_dataset=True, trust_remote_code=True)

# Cargar el modelo RAG
model = RagSequenceForGeneration.from_pretrained("facebook/rag-token-base", retriever=retriever)

# Preparar la consulta
input_text = "What is artificial intelligence?"
input_ids = tokenizer(input_text, return_tensors="pt").input_ids

# Generar la respuesta con parámetros ajustados
generated_ids = model.generate(
    input_ids,
    max_new_tokens=100,  # Aumentar la longitud máxima de la respuesta
    num_return_sequences=1,  # Número de respuestas a generar
    num_beams=5  # Utilizar beam search para mejorar la calidad de la respuesta
)

# Decodificar la respuesta generada
generated_text = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(generated_text)
