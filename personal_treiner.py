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
