import re
from difflib import SequenceMatcher

def find_in_sentences(text, word):
  """
    Esta função divide o texto em frases e retorna uma lista de frases que contenham a palavra.

    Argumentos:
    text: A string de texto de entrada.
    word: A palavra a ser buscada.

    Retorna:
    Uma lista de frases que contenham a palavra.
  """
  # Código para encontrar as frases sem Regex
  # sentences = text.split(".")  # Split pelo ponto final
  # sentences = [sentence.strip() for sentence in sentences]  # Remove espaço em branco
  # matches = [sentence for sentence in sentences if word.lower() in sentence.lower()]  # Busca case sensitive

  # Código para encontrar as frases com Regex
  # Define o padrão regex para encontrar pontos finais seguidos de espaços em branco
  pattern = re.compile(r'\.\s+')
  # Substitui o ponto final seguido de espaços em branco por apenas um ponto final
  text = re.sub(pattern, '.', text)
  # Divide o texto em frases usando o ponto final como delimitador
  sentences = text.split(".")
  # Remove espaços em branco das extremidades de cada frase
  sentences = [sentence.strip() for sentence in sentences]

  # Busca por correspondências case insensitive
  matches = [sentence for sentence in sentences if re.search(re.escape(word), sentence, re.IGNORECASE)]

  # Verifica a similaridade de cada palavra na frase com a palavra fornecida
  # Somente similaridade superior a 80%
  """
  similarity = 0.8
  matches = []
  for sentence in sentences:
      words = sentence.split()
      for w in words:
          similarity = SequenceMatcher(None, word.lower(), w.lower()).ratio()
          if similarity >= similarity:
              matches.append(sentence)
              break
  """

  return matches

while True:
  text = input("Texto de entrada: ")
  word = input("Palavra para encontrar: ")

  results = find_in_sentences(text, word)

  if results:
    print("Frases contendo a palavra solicitada", word, ":")
    for sentence in results:
      print("-", sentence)
  else:
    print("Nenhuma frase encontrada", word)

  choice = input("Buscar novamente? (s/n): ")
  if choice.lower() != "s":
    break

print("Fim...")
