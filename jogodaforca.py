palavras = ["Python", "JavaScript", "PHP", "Clojure", "Haskel", 
"Elixir", "Golang", "Cobol", "Assembly", "Julia", "Scala", "Ruby", 
"Erlang", "OCaml", "Rust", "Cpp", "Ada", "Swift", "Lisp", "Simula"]

# Função que escolhe uma palavra aleatoria da lista
from random import randint

sorteio = palavras[randint(0, len(palavras) -1)] # len = retorna quantas palavras tem na lista para sortear com randint
# lê-se: em palavras, escolha um item entre (randint) o primeiro (0) e o último (-1)

# Função que que oculta a palavra
# lambda: em sorteio(x), substitua(:) as letras da string por "-"
oculta = list(map(lambda x: '-', sorteio)) # gerar lista da palavra escondida
# palavra = ''.join(oculta)

# Função que verifica se a letra esta na palavra
def atualiza(letra, sorteio): # atualiza a palavra escondida
                       # enumerate = enumera cada letra da palavra sorteada
    for indice, valor in enumerate(sorteio):
        # Verifica se o chute do jogador é a atual letra da palavra
        if letra.lower() == valor.lower(): # transforma letra digitada em minuscula para aceitar a ou A
            # Caso o chute for correto substitui na palavra escondida
            oculta[indice] = valor

# Verifica se o jogador ganhou
def vitoria(sorteio, palavra):
    return sorteio == palavra

# Mecânica do jogo
chances = len(sorteio) + 5 # número de letras da palavra + 5 chances (margem de erro)

# Loop até vencer
while True:
    chances -= 1 # as chances vão diminuindo a cada jogada

    print("Você tem {} chances".format(chances))
    print("Palavra = {}".format(''.join(oculta))) # .join retira , e [] e junta tudo
    letra = input("Digite uma letra: ")
    print("")
    atualiza(letra, sorteio)

    # Derrota
    if chances == 0: # se as chances acabarem
        print("\nAcabaram suas chances, você é a vergonha da profissión.")
        break # quebra o loop

    # Vitória
    if vitoria(sorteio, ''.join(oculta)):
        print("\nParabéns, você ganhou um Pastel de Flango.")
        break # quebra o loop

print("A palavra secreta era {}.".format(sorteio))