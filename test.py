from transformers import pipeline
pipe = pipeline("text-classification", model="OnePieceModel", device=0)

def classify(text):
    return pipe(text)

a = classify("why so serius mate")
print(a)