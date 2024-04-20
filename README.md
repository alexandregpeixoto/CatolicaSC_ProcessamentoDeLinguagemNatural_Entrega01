> **Trabalho 1: processamento de fala e expressões regulares**
>
> O trabalho consiste em desenvolver um buscador em áudio/vídeo. As
> seguintes tarefas para construção do buscador devem ser cumpridas:

1.  **Transcrever o conteúdo de um vídeo/áudio: utilizar a transcrição
    > automática do conteúdo da mídia;**

> O trecho de áudio utilizado foi extraído do Youtube Shorts no
> [[link]{.underline}](https://www.youtube.com/shorts/CW3_ELv-jtI).
> Video completo no
> [[link]{.underline}](https://www.youtube.com/watch?v=5t1vTLU7s40&t=182s&ab_channel=LexFridman).
> A transcrição foi criada utilizando uma implementação do Whisper da
> OpenAI via
> [[Hugginface]{.underline}](https://huggingface.co/spaces/SteveDigital/free-fast-youtube-url-video-to-text-using-openai-whisper).
> Segue transcrição:

+-----------------------------------------------------------------------+
| > There is a number of characteristics of intelligent behavior. For   |
| > example, the capacity to understand the world, understand the       |
| > physical world. The ability to remember and retrieve things,        |
| > process not memory. The ability to reason and the ability to plan.  |
| > Those are four essential characteristics of intelligent systems or  |
| > entities, humans, animals. L&Ns can do none of them. Or they can    |
| > only do them in a very primitive way. And they don\'t really        |
| > understand the physical world. They don\'t really have a system     |
| > memory. They can\'t really reason and they certainly can\'t plan.   |
| > And so, you know, if you expect a system to become intelligent,     |
| > but, you know, without having the possibility of doing those        |
| > things, you\'re making a mistake. That is not to say that photoreal |
| > receivet l&Ns are not useful. They\'re certainly useful. That       |
| > they\'re not interesting. That we can\'t build a whole ecosystem of |
| > applications around them. Of course we can, but as a path towards   |
| > human level intelligence, they\'re missing essential components.    |
+=======================================================================+
+-----------------------------------------------------------------------+

2.  **Quantificar o quanto a transcrição automatizada conseguiu
    > transcrever corretamente: comparar o texto original da mídia com o
    > que foi transcrito e identificar os termos identificados
    > incorretamente, se houverem. Essa análise pode ser manual ou
    > automatizada;**

> Análise manual:

+-----------------------------------------------------------------------+
| > There is a number of characteristics of intelligent behavior. For   |
| > example, the capacity to understand the world, understand the       |
| > physical world. The ability to remember and retrieve things,        |
| > **process not** memory. The ability to reason and the ability to    |
| > plan. Those are four essential characteristics of intelligent       |
| > systems or entities, humans, animals. **L&Ns** can do none of them. |
| > Or they can only do them in a very primitive way. And they don\'t   |
| > really understand the physical world. They don\'t really have a     |
| > system memory. They can\'t really reason and they certainly can\'t  |
| > plan. And so, you know, if you expect a system to become            |
| > intelligent, but, you know, without having the possibility of doing |
| > those things, you\'re making a mistake. That is not to say that     |
| > **photoreal receivet l&Ns** are not useful. They\'re certainly      |
| > useful. That they\'re not interesting. That we can\'t build a whole |
| > ecosystem of applications around them. Of course we can, but as a   |
| > path towards human level intelligence, they\'re missing essential   |
| > components.                                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

> Texto correto:

+-----------------------------------------------------------------------+
| > There is a number of characteristics of intelligent behavior. For   |
| > example, the capacity to understand the world, understand the       |
| > physical world. The ability to remember and retrieve things,        |
| > **persistent** memory. The ability to reason and the ability to     |
| > plan. Those are four essential characteristics of intelligent       |
| > systems or entities, humans, animals. **LLMs** can do none of them. |
| > Or they can only do them in a very primitive way. And they don\'t   |
| > really understand the physical world. They don\'t really have a     |
| > system memory. They can\'t really reason and they certainly can\'t  |
| > plan. And so, you know, if you expect a system to become            |
| > intelligent, but, you know, without having the possibility of doing |
| > those things, you\'re making a mistake. That is not to say that     |
| > **autoregressive LLMs** are not useful. They\'re certainly useful.  |
| > That they\'re not interesting. That we can\'t build a whole         |
| > ecosystem of applications around them. Of course we can, but as a   |
| > path towards human level intelligence, they\'re missing essential   |
| > components.                                                         |
+=======================================================================+
+-----------------------------------------------------------------------+

3.  **Solicitar um termo de busca e buscar uma frase que compreende esse
    > termo: mais do que buscar o termo no texto transcrito, o objetivo
    > e extrair toda a frase onde o termo está presente. Opcionalmente
    > pode ser retornado todas as frases que contém o termo.**

Código de busca implementado em python no
[[github]{.underline}](https://github.com/alexandregpeixoto/CatolicaSC_ProcessamentoDeLinguagemNatural_Entrega01/blob/main/FindWords.py).

4.  **A(s) frase(s) buscada(s) anteriormente deve(m) ter sintetizada(s)
    > por voz. Opcionalmente, pode também ser "tocado" o trecho
    > sintetizado na mídia original**

> Código com síntese de voz em python no
> [[github]{.underline}](https://github.com/alexandregpeixoto/CatolicaSC_ProcessamentoDeLinguagemNatural_Entrega01/blob/main/SpeakSentences.py).
