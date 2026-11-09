# # Processo Seletivo JWC: Aquecimento de volta ao Python

# ## Contexto da Avaliação

# A empresa de Tecnologia JWC atua na área de desenvolvimento de aplicações web, atendendo diversos clientes de médio e grande porte.

# A sede da organização está localizada no centro do Rio de Janeiro, contando com 20 colaboradores na equipe de desenvolvimento e 30 na área administrativa.

# Com uma grande demanda recebida na área de educação, o diretor identificou a necessidade de contratar novos programadores Full Stack.

# O departamento de Recursos Humanos propôs que o processo de contratação fosse feito em etapas, nas quais os candidatos recebem diversos desafios práticos.

# Para avançar, você deve demonstrar a capacidade de desenvolver algoritmos e resolver problemas lógicos e aritméticos.

# ## Desafio 1: Manipulação Básica de Variáveis

# Enunciado: O recrutador solicita que você faça o seu primeiro código com manipulação básica de variáveis.

# Desenvolva um algoritmo declarando duas variáveis utilizando tipos primitivos adequados:

# - `nome_projeto` (tipo string/texto): para armazenar o nome de um projeto educacional (ex: "Portal Educacional JWC").

# - `orcamento_projeto` (tipo float/decimal): para armazenar o orçamento destinado a ele (ex: 45000.50).

# Em seguida, utilize comandos de saída (`print`) para exibir essas duas informações de forma clara e formatada na tela.

# Resolução:
# nome_projeto = "Portal Educacional JWC"
# orcamento_projeto = 45000.50

# print(f"Nome do Projeto: {nome_projeto}")
# print(f"Orçamento do Projeto: R$ {orcamento_projeto:.2f}")

# ## Desafio 2: Expressões Aritméticas

# Enunciado: É necessário realizar cálculos simples para o sistema financeiro da empresa.

# Construa um algoritmo que utilize comandos de entrada (`input`) para solicitar ao usuário o valor da hora de um desenvolvedor e armazene na variável `valor_hora` (convertida para `float`).

# Defina uma variável `horas_trabalhadas` (tipo `int`) com a carga horária mensal padrão de 160 horas.

# Crie uma variável `custo_total` que receba o resultado da multiplicação entre `valor_hora` e `horas_trabalhadas`.

# Por fim, utilize um comando de saída (`print`) para exibir o custo operacional mensal formatado com duas casas decimais.

# Resolução:
# valor_hora = float(input("Digite o valor da hora do desenvolvedor: "))
# horas_trabalhadas = 160
# custo_total = valor_hora * horas_trabalhadas
# print(f"Custo Operacional Mensal: R$ {custo_total:.2f}")

# ## Desafio 3: Versionamento de Código

# Enunciado: A equipe técnica da JWC precisa trabalhar com o código de forma simultânea em máquinas diferentes.

# Descreva, em formato de lista ou comentários, qual é a sequência exata de comandos do GIT (`git init`, `git status`, `git add`, `git commit`) necessária para:

# 1. Inicializar um novo repositório local.

# 2. Verificar o estado atual dos arquivos modificados ou não rastreados.

# 3. Adicionar todos os arquivos alterados para a área de preparação (staging area).

# 4. Criar o marco de salvamento local com uma mensagem descritiva.

# Explique brevemente a função de cada um desses 4 comandos.

# Resolução:
# 1. `git init`: Inicializa um novo repositório Git local no diretório atual.
# 2. `git status`: Exibe o estado atual do repositório, mostrando arquivos modificados, não rastreados e prontos para commit. 
# 3. `git add`: Adiciona todos os arquivos alterados para a área de preparação.
# 4. `git commit`: Cria o marco de salvamento local com uma mensagem descritiva. 

# ## Desafio 4: Estruturas Condicionais

# Enunciado: O recrutador entregou uma atividade relacionada às condicionais.

# Crie uma variável `nota_tecnica` (tipo `float`) que receba a nota de um candidato (de 0.0 a 10.0) via entrada de dados (`input`).

# Utilize estruturas condicionais (`if`, `elif`, `else`) para classificar e exibir o resultado do candidato de acordo com as seguintes regras:

    # - Maior ou igual a 9.0: "Excelente - Aprovado Direto"

    # - Maior ou igual a 7.0 (e menor que 9.0): "Bom - Aprovado para a próxima fase"

    # - Maior ou igual a 5.0 (e menor que 7.0): "Regular - Em lista de espera"

    # - Menor que 5.0: "Insuficiente - Reprovado"

# Resolução:
# nota_tecnica = float(input("Digite a nota técnica do candidato (0.0 a 10.0): "))
# if nota_tecnica >= 9.0:
#     print("Excelente - Aprovado Direto")
# elif nota_tecnica >= 7.0:
#     print("Bom - Aprovado para a próxima fase")
# elif nota_tecnica >= 5.0:
#     print("Regular - Em lista de espera")
# else:
#     print("Insuficiente - Reprovado")

# ## Desafio 5: Operadores Lógicos

# Enunciado: Um módulo do sistema web exige validações duplas.

# Crie duas variáveis recebidas via `input`:

# - `cargo` (tipo `str`): para armazenar o cargo do usuário.

# - `nivel_acesso` (tipo `int`): para armazenar o nível de acesso numérico.

# Aplique operadores lógicos (`and`) em uma estrutura condicional (`if/else`) para validar o acesso. O sistema deve exibir "Acesso permitido" apenas se o `cargo` for exatamente igual a `"Programador"` E o `nivel_acesso` for estritamente maior que 2. Caso contrário, deve exibir "Acesso negado".

# Resolução:
# cargo = input("Digite o cargo do usuário:")
# nivel_acesso = int(input("Digite o nível de acesso do usuário:"))

# if cargo == "Programador" and nivel_acesso > 2:
#     print("Acesso permitido")
# else:
#     print("Acesso negado")

# ## Desafio 6: Estruturas de Repetição

# Enunciado: O RH necessita automatizar o envio de notificações para os candidatos aprovados.

# Utilize uma estrutura de repetição (`for` ou `while`) com um contador finito (variável `i` ou `contador`) que vá de 1 até 5.

# A cada iteração do loop, exiba na tela uma mensagem simulando o envio, indicando o número do e-mail atual (ex: "E-mail 1 enviado com sucesso.", "E-mail 2 enviado com sucesso.", etc.).

# Resolução:
# for i in range(1, 6):
#     print(f"E-mail {i} enviado com sucesso.")

# ## Desafio 7: Execução em Ordem Decrescente

# Enunciado: O portal educacional precisa de um contador regressivo antes de entrar no ar.

# Crie uma variável `contador` inicializada com o valor 5 (tipo `int`).

# Utilize um laço de repetição (`while` ou `for`) que realize a contagem em ordem decrescente até chegar ao 1, exibindo cada número na tela.

# Garanta estruturalmente que a variável `contador` seja decrementada a cada passo para evitar um looping infinito. Ao finalizar o loop, exiba a mensagem "Portal no ar!".

# Resolução:
# contador = 5
# while contador > 0:
#     print(contador)
#     contador -= 1
# print("Portal no ar!")

# ## Desafio 8: Teste de Mesa

# Enunciado: O recrutador quer avaliar a compreensão de pensamento computacional e testes de mesa.

# Analise o código abaixo e simule a execução passo a passo como o computador faria.

# Em formato de comentário, descreva:

# 1. O valor da variável `vagas` antes do loop e a cada iteração.

# 2. A saída exata que será impressa na tela do monitor linha por linha.

# Código fornecido pelo recrutador:

# vagas = 3

# while vagas > 0:

# print(f"Temos {vagas} vagas abertas.")

# vagas = vagas - 1

# print("Processo encerrado.")

# Resolução:
# vagas = 3
# while vagas > 0:
#     print(f"Temos {vagas} vagas abertas.")
#     vagas = vagas - 1
# print("Processo encerrado.")

# ## Desafio 9: Modularização com Funções

# Enunciado: O desenvolvimento da JWC baseia-se na modularização de sistemas.

# Crie uma função chamada `calcular_bonus` que receba um parâmetro chamado `salario` (tipo `float`).

# Dentro da função, calcule o valor de um bônus de 10% sobre esse salário e armazene em uma variável `bonus`, retornando esse valor utilizando a palavra-chave `return`.

# Fora da função, crie uma variável `salario_atual` (ex: 5000.00), chame a função passando essa variável como argumento, armazene o resultado em `valor_bonus` e exiba ambos os valores na tela.

# Resolução:
# def calcular_bonus(salario:float) -> float:
#     bonus = salario * 0.10
#     return bonus
    
# salario_atual = 5000.00
# valor_bonus = calcular_bonus(salario_atual)

# print(f"Salário Atual: R$ {salario_atual:.2f}")
# print(f"Valor do Bônus (10%): R$ {valor_bonus:.2f}")

# ## Desafio 10: Manipulação de Vetores

# Enunciado: O recrutador entregou uma atividade relacionada a Vetores (Listas em Python).

# Crie uma lista chamada `tecnologias` contendo inicialmente três strings representando tecnologias exigidas pela vaga: `"Python"`, `"JavaScript"` e `"SQL"`.

# Exiba a lista inicial na tela.

# Em seguida, utilize a função nativa adequada (`.append()`) para adicionar uma quarta tecnologia (ex: `"Git"`) ao final dessa lista e exiba a lista atualizada na tela.

# Resolução:
# tecnologias = ["Python", "JavaScript", "SQL"]
# print("Lista inicial de tecnologias:", tecnologias)
# tecnologias.append("Git")
# print("Lista atualizada de tecnologias:", tecnologias)