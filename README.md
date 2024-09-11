🏋️‍♂️ Assistente de Personal Trainer - Gerador de Treino Ideal

Este projeto é um desafio de Prompt Engineer, onde o objetivo é criar um prompt que ajuda a montar o treino ideal para cada combinação de fatores, como biotipo corporal, disponibilidade de tempo e tipo de exercícios preferidos.
O assistente de personal trainer gerado por esse prompt será capaz de personalizar os treinos de acordo com as características e necessidades do usuário. O projeto deve ser feito utilizando as boas práticas de prompt engineer.

📋 Índice

📝 Introdução

💪 Biotipos Corporais

📅 Dias Disponíveis para Treino

🏋️ Tipos de Exercícios

🛠️ Regras de Negócio

📖 Material de Apoio

🎯 Prompt de Resposta Proposto

🖥️ Script Python Adicional

📜 Licença

ℹ️ Maiores Informações

📝 Introdução

Este projeto visa criar um assistente de personal trainer automatizado que ajuda a gerar treinos personalizados. O usuário fornecerá informações sobre seu biotipo corporal, a quantidade de dias disponíveis para treinar na semana e o tipo de exercício preferido. Com base nessas informações, o assistente gerará um plano de treino ideal. O objetivo é tornar a criação de um plano de treino mais acessível e eficaz, utilizando técnicas avançadas de engenharia de prompt.

💪 Biotipos Corporais

A primeira etapa para personalizar o treino é determinar o biotipo corporal do usuário. Os três biotipos principais são:

Biotipo	Descrição
Ectomorfo	Corpo mais magro, dificuldade em ganhar peso e massa muscular.
Mesomorfo	Corpo naturalmente musculoso, facilidade em ganhar massa muscular e perder gordura.
Endomorfo	Corpo com tendência a acumular gordura, dificuldade em perder peso.
Nota: Escolha o biotipo que mais se aproxima do seu corpo atual para que o treino seja mais eficiente.

📅 Dias Disponíveis para Treino

A segunda etapa é determinar quantos dias por semana o usuário pode treinar. Dependendo do número de dias, o treino sugerido pode variar:

Dias por Semana	Tipo de Treino Sugerido
1 dia	Treino Full Body
3 dias	Treino ABC
5 dias	Treino ABCDE
Full Body: Treino que trabalha o corpo todo em uma única sessão.
ABC: Divisão do treino em três dias, cada um focado em grupos musculares diferentes.
ABCDE: Divisão do treino em cinco dias, com foco mais específico em cada grupo muscular.

🏋️ Tipos de Exercícios

A terceira etapa é a escolha do tipo de exercício preferido. Aqui estão algumas categorias com exemplos:

Tipo de Treino	Descrição
Funcional	Exercícios que melhoram a funcionalidade do corpo, usando movimentos naturais.
Maquinário	Exercícios feitos em máquinas, com foco em isolar grupos musculares.
Peso Livre	Exercícios com pesos livres, como halteres e barras, para trabalhar vários grupos musculares.
Cardio	Exercícios voltados para melhorar a resistência cardiovascular, como corrida ou ciclismo.
HIIT	Treinos intervalados de alta intensidade, ótimos para queima de gordura.

🛠️ Regras de Negócio

Identifique seu biotipo corporal consultando a seção de biotipos.
Determine quantos dias por semana você pode treinar e escolha o tipo de treino mais adequado.
Selecione o tipo de exercício que prefere realizar e que se encaixa melhor nos seus objetivos.
Use o prompt do assistente para gerar um plano de treino personalizado.

📖 Material de Apoio

Aqui estão alguns recursos adicionais que podem ser úteis para entender melhor o projeto e as práticas de engenharia de prompt:

Fundamentos de Engenharia de Prompt
Boas Práticas de Prompt

🎯 Prompt de Resposta Proposto

Com as informações passadas anteriormente, o prompt de resposta para o assistente de personal trainer deve seguir o seguinte formato:

Prompt:prompt-v1.md


Você é um especialista personal treiner e vai me ajudar a montar um treino ideal, baseado nas três variáveis abaixo:

# Área de Variáveis

#{{biotipo }} = endomorfo
#{{periodização}} = 2 dias de treino
#{{tipo}} = funcional e cardio
{{biotipo}}: (Escolha entre: Ectomorfo, Mesomorfo, Endomorfo)
{{objetivo}}: (Escolha entre: Perda de peso, Ganho de massa muscular, Melhora de performance)
{{tipo}}: (Escolha entre: Funcional, Maquinário, Peso Livre, Cardio, HIIT)
{{periodização}}: (Escolha entre: 1 dia, 3 dias, 5 dias)


#Regras
Identifique o tipo corporal informado nas variáveis. Cada biotipo tem características que influenciam o plano de treino:

Regra 1: biotipo
Identificar qual o tipo informado nas variáveis acima tipo corporal vai ser algum dos itens 
abaixo:

- Ectomorfo	Corpo mais magro, difícil ganhar peso e massa muscular.
- Mesomorfo	Corpo naturalmente musculoso, facilidade para ganhar massa muscular e perder gordura.
- Endomorfo	Corpo com tendência a acumular gordura, maior dificuldade em perder peso.

Regra 2: periodização
Dependendo da quantidade mínima de dias informada, o plano de treino será:

- 1 dia	Treino Full Body
- 3 dias	Treino ABC
- 5 dias	Treino ABCDE


Regra 3: tipo
Escolha e descreva o tipo de treino com base nas opções informadas:

- Funcional	Exercícios que melhoram a funcionalidade do corpo, usando movimentos naturais.
- Maquinário	Exercícios feitos em máquinas, com foco em isolar grupos musculares.
- Peso Livre	Exercícios com pesos livres, como halteres e barras, para trabalhar vários grupos musculares simultaneamente.
- Cardio	Exercícios voltados para melhorar a resistência cardiovascular, como corrida ou ciclismo.
- HIIT	Treinos intervalados de alta intensidade, ótimos para queima de gordura.


Regra 4: Fornece recomendações alimentares gerais para apoiar o treinamento:

- Proteínas Consuma uma boa fonte de proteína em cada refeição para apoiar o crescimento e a recuperação muscular.
- Carboidratos Complexos Inclua carboidratos complexos para fornecer energia sustentada durante o treino e o dia.
- Gorduras Saudáveis Adicione gorduras saudáveis à sua dieta para suporte hormonal e recuperação.
- Hidratação Beba bastante água ao longo do dia para manter a hidratação e otimizar o desempenho durante os treinos.
- Refeições Pré-Treino Consuma uma refeição leve com proteínas e carboidratos complexos cerca de 1-2 horas antes do treino para garantir energia suficiente.
- Refeições Pós-Treino Após o treino, opte por uma refeição rica em proteínas e carboidratos para ajudar na recuperação muscular e reposição de energia.

Regra 5: Sugira o melhor horário para treinar com base em geral::

- Manhã Treinar pela manhã pode aumentar os níveis de energia e melhorar o humor para o dia. Pode ajudar a regular o metabolismo e promover a consistência.
- Tarde Se amanhã não for ideal, treinar à tarde pode ser benéfico, pois a temperatura corporal e a força muscular tendem a ser maiores, o que pode levar a um desempenho melhor.
- Noite Evite treinar muito próximo da hora de dormir para não prejudicar o sono. No entanto, se a noite for o único horário disponível, garanta que tenha tempo para relaxar antes de dormir.


# Resultado esperado

Biotipo: "Escolhido"
Periodização: "Dias escolhidos"
Tipo: "Tipo treino"
objetivo"Escolha o ojetivo"

com base nos valores informados na área de variáveis e com as guidelines, crie um treino ideal para a pessoa que corresponde a combinação desses 3 valores e informações regra 4 e regra 5 adequada a regra 1

#DICAS

- Avaliação: Após algumas semanas, avalie seu progresso verificando mudanças no peso, medidas corporais e nível de energia.
- Ajustes: Se necessário, ajuste o plano de treino, alimentação ou horários com base nos resultados e no feedback do progresso.
- Consulta Médica: Além disso, consulte um médico regularmente, especialmente para questões relacionadas ao cardio.

Coleta de Feedback: Use uma combinação de medidas objetivas (peso, medidas corporais) e feedback subjetivo (nível de energia, bem-estar) para avaliar o progresso.
Como Ajustar: Ajuste o plano com base no feedback recebido. Se a energia estiver baixa, considere ajustar a alimentação ou os horários. Se os resultados estiverem aquém das expectativas, revise a intensidade e o tipo de treino.

Motivação e Objetivos

Estabeleça Metas: Defina metas claras e alcançáveis, como melhorar a resistência, ganhar massa muscular ou perder um número específico de quilos.
Mantenha a Motivação: Encontre um parceiro de treino, varie os exercícios para manter o interesse e celebre pequenas vitórias ao longo do caminho.

Utilize este prompt para gerar planos de treino que atendam às necessidades específicas dos usuários e proporcionem um caminho claro e eficaz para alcançar seus objetivos de fitness.

🖥️ Script Python Adicional

Além do prompt de resposta, um script Python foi desenvolvido para automatizar o processo de criação de treinos. Este script solicita informações do usuário e gera um plano de treino com base nas respostas fornecidas.

Funcionalidades do Script personal_treiner.py

Obtenção de Entradas: Solicita e valida o biotipo, objetivo, tipo de treino e periodização.
Geração de Recomendações: Baseado nas entradas, gera um plano de treino, dicas de alimentação e horários recomendados.
Recomendações Personalizadas: Oferece sugestões para avaliação de progresso e ajustes no plano.
###################
def obter_entrada(mensagem, opcoes):
    """Função para obter entrada do usuário com validação."""
    while True:
        entrada = input(mensagem).strip().lower()
        if entrada in opcoes:
            return entrada
        else:
            print(f"Opção inválida. Escolha entre: {', '.join(opcoes)}")

def obter_multiplas_opcoes(mensagem, opcoes):
    """Função para obter múltiplas opções do usuário com validação."""
    while True:
        entradas = input(mensagem).strip().lower().split(',')
        entradas = [entrada.strip() for entrada in entradas]
        if all(entrada in opcoes for entrada in entradas):
            return entradas
        else:
            print(f"Alguma(s) opção(ões) inválida(s). Escolha entre: {', '.join(opcoes)}")

def obter_numero(mensagem, opcoes):
    """Função para obter um número do usuário com validação."""
    while True:
        entrada = input(mensagem).strip()
        if entrada in opcoes:
            return entrada
        else:
            print(f"Opção inválida. Escolha entre: {', '.join(opcoes)}")

def sugerir_objetivo(biotipo):
    """Sugere um objetivo com base no biotipo escolhido."""
    sugestoes_objetivo = {
        "ectomorfo": "ganho de massa muscular",
        "mesomorfo": "melhora de performance",
        "endomorfo": "perda de peso"
    }
    return sugestoes_objetivo.get(biotipo, "objetivo não definido")

def sugerir_tipos(biotipo):
    """Sugere tipos de treino com base no biotipo escolhido."""
    sugestoes_treino = {
        "ectomorfo": ["peso livre", "funcional", "cardio"],
        "mesomorfo": ["peso livre", "funcional", "cardio", "hiit"],
        "endomorfo": ["funcional", "cardio", "hiit"]
    }
    return sugestoes_treino.get(biotipo, [])

# Definindo opções
biotipos = ["ectomorfo", "mesomorfo", "endomorfo"]
objetivos = ["perda de peso", "ganho de massa muscular", "melhora de performance"]
tipos = ["funcional", "maquinário", "peso livre", "cardio", "hiit"]

# Obtendo entradas do usuário
biotipo = obter_entrada(f"Escolha o biotipo ({', '.join(biotipos)}): ", biotipos)

objetivo_sugerido = sugerir_objetivo(biotipo)
print(f"Objetivo sugerido para o seu biotipo ({biotipo}): {objetivo_sugerido.capitalize()}")
objetivo = obter_entrada(f"Confirme ou ajuste o objetivo ({', '.join(objetivos)}): ", objetivos)

tipos_sugeridos = sugerir_tipos(biotipo)
print("Sugestões de tipos de treino com base no seu biotipo:")
print(", ".join(tipos_sugeridos))

tipos_selecionados = obter_multiplas_opcoes(f"Escolha os tipos de treino ({', '.join(tipos_sugeridos)}), separados por vírgula: ", tipos_sugeridos)

print("Escolha a periodização:")
print("1 - 1 dia: Treino Full Body")
print("3 - 3 dias: Treino ABC")
print("5 - 5 dias: Treino ABCDE")
periodizacao = obter_numero("Digite o número correspondente: ", ["1", "3", "5"])

# Funções para criar o plano de treino
def treino_full_body(tipo):
    return f"Treino Full Body com os tipos: {', '.join(tipo)}."

def treino_abc(tipo):
    return (f"Treino ABC com foco em {', '.join(tipo)}:\n"
            "Dia A: Exercícios Funcionais\n"
            "Dia B: Cardio\n"
            "Dia C: HIIT")

def treino_abcde(tipo):
    return (f"Treino ABCDE com foco em {', '.join(tipo)}:\n"
            "Dia A: Funcional\n"
            "Dia B: Cardio\n"
            "Dia C: HIIT\n"
            "Dia D: Funcional\n"
            "Dia E: Cardio")

def gerar_recomendacoes(biotipo, periodizacao, tipo, objetivo):
    if periodizacao == "1":
        treino = treino_full_body(tipo)
    elif periodizacao == "3":
        treino = treino_abc(tipo)
    elif periodizacao == "5":
        treino = treino_abcde(tipo)
    else:
        treino = "Período de treino não reconhecido."

    alimentacao = ("Dicas de Alimentação:\n"
                   "- Consuma uma boa fonte de proteína em cada refeição para apoiar o crescimento e a recuperação muscular.\n"
                   "- Inclua carboidratos complexos para fornecer energia sustentada durante o treino e o dia.\n"
                   "- Adicione gorduras saudáveis à sua dieta para suporte hormonal e recuperação.\n"
                   "- Beba bastante água ao longo do dia para manter a hidratação e otimizar o desempenho durante os treinos.\n"
                   "- Consuma uma refeição leve com proteínas e carboidratos complexos cerca de 1-2 horas antes do treino para garantir energia suficiente.\n"
                   "- Após o treino, opte por uma refeição rica em proteínas e carboidratos para ajudar na recuperação muscular e reposição de energia.")

    horario = ("Melhor Horário para Treino:\n"
               "- Manhã: Treinar pela manhã pode aumentar os níveis de energia e melhorar o humor para o dia. Pode ajudar a regular o metabolismo e promover a consistência.\n"
               "- Tarde: Se a manhã não for ideal, treinar à tarde pode ser benéfico, pois a temperatura corporal e a força muscular tendem a ser maiores, o que pode levar a um desempenho melhor.\n"
               "- Noite: Evite treinar muito próximo da hora de dormir para não prejudicar o sono. No entanto, se a noite for o único horário disponível, garanta que tenha tempo para relaxar antes de dormir.")

    avaliacao_ajustes = ("Avaliação e Ajustes:\n"
                         "- Após algumas semanas, avalie seu progresso verificando mudanças no peso, medidas corporais e nível de energia.\n"
                         "- Se necessário, ajuste o plano de treino, alimentação ou horários com base nos resultados e no feedback do progresso.\n"
                         "- Consulte um médico regularmente, especialmente para questões relacionadas ao cardio.\n"
                         "- Use uma combinação de medidas objetivas (peso, medidas corporais) e feedback subjetivo (nível de energia, bem-estar) para avaliar o progresso.\n"
                         "- Ajuste o plano com base no feedback recebido. Se a energia estiver baixa, considere ajustar a alimentação ou os horários. Se os resultados estiverem aquém das expectativas, revise a intensidade e o tipo de treino.")

    motivacao = ("Motivação e Objetivos:\n"
                 "- Estabeleça metas claras e alcançáveis, como melhorar a resistência, ganhar massa muscular ou perder um número específico de quilos.\n"
                 "- Mantenha a motivação encontrando um parceiro de treino, variando os exercícios para manter o interesse e celebrando pequenas vitórias ao longo do caminho.")

    return (f"Resultado esperado:\n\n"
            f"Biotipo: {biotipo.capitalize()}\n"
            f"Periodização: {periodizacao} dias\n"
            f"Tipo de Treino: {', '.join(tipo).capitalize()}\n"
            f"Objetivo: {objetivo.capitalize()}\n\n"
            f"Plano de Treino:\n{treino}\n\n"
            "\n"    
            f"{alimentacao}\n\n"
             "\n"  
            f"{horario}\n\n"
             "\n"  
            f"{avaliacao_ajustes}\n\n"
             "\n"  
            f"{motivacao}")

# Gerar e imprimir o plano de treino
print(gerar_recomendacoes(biotipo, periodizacao, tipos_selecionados, objetivo))

#################

@Como Executar o Script

Instalação: Certifique-se de ter o Python instalado. Não são necessárias bibliotecas adicionais para este script.

Execução: Salve o código acima em um arquivo chamado gerador_treino.py e execute-o com o comando:

python gerador_treino.py

Interação: Siga as instruções fornecidas pelo script para inserir suas preferências e obter seu plano de treino personalizado.

Este script pode ser adaptado e expandido conforme necessário para atender a requisitos adicionais.


📜 Licença

Este projeto é licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.


ℹ️ Maiores Informações

Para mais informações e suporte, você pode acessar os seguintes links:

https://portifolionavinfo.netlify.app/ 

Diversos: https://www.dio.me/users/nav_info_suporte    

GitHub:  https://github.com/Fabianonavarro 

LinkedIn: https://www.linkedin.com/in/fabiano-de-navarro

