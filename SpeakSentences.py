import re
import pyttsx3
from difflib import SequenceMatcher

def find_in_sentences(text, word):
    """
    Esta função divide o texto em frases e retorna uma lista de frases que contenham uma palavra com uma similaridade de pelo menos 80%.

    Argumentos:
    text: A string de texto de entrada.
    word: A palavra a ser buscada.

    Retorna:
    Uma lista de frases que contenham uma palavra com uma similaridade de pelo menos 80%.
    """
    # Define o padrão regex para encontrar pontos finais seguidos de espaços em branco
    pattern = re.compile(r'\.\s+')

    # Substitui o ponto final seguido de espaços em branco por apenas um ponto final
    text = re.sub(pattern, '.', text)

    # Divide o texto em frases usando o ponto final como delimitador
    sentences = text.split(".")

    # Remove espaços em branco das extremidades de cada frase
    sentences = [sentence.strip() for sentence in sentences]

    # Verifica a similaridade de cada palavra na frase com a palavra fornecida
    matches = []
    for sentence in sentences:
        words = sentence.split()
        for w in words:
            similarity = SequenceMatcher(None, word.lower(), w.lower()).ratio()
            if similarity >= 0.8:
                matches.append(sentence)
                break

    return matches

# Função para falar as frases encontradas
def speak_sentences(sentences):
    engine = pyttsx3.init()
    for sentence in sentences:
        engine.say(sentence)
        engine.runAndWait()

while True:
    text = input("Texto de entrada: ")
    word = input("Palavra para encontrar: ")

    results = find_in_sentences(text, word)

    if results:
        print("Frases contendo uma palavra similar a", word, ":")
        for sentence in results:
            print("-", sentence)
        speak_sentences(results)
    else:
        print("Nenhuma frase encontrada com uma palavra similar a", word)

    choice = input("Buscar novamente? (s/n): ")
    if choice.lower() != "s":
        break

print("Fim...")
