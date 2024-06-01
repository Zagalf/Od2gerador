import random

# Lista de prefixos, raízes e sufixos para os nomes
prefixes = [
    "Al", "Bran", "Dor", "Er", "Fro", "Gal", "Hel", "Ith", "Jar", "Kel", "Lor", "Mor", "Nor", "Or", "Pel", "Quin",
    "Ral", "Sor", "Thor", "Ul", "Var", "Wor", "Xal", "Yar", "Zor", "Gre", "Thul", "Gar", "Nar", "Zan", "Bar", "Ker",
    "Tor", "Vor", "Lur", "Mar", "Sin", "Bel", "Dur", "Gol", "Har", "Vax", "Zol", "Cul", "Fen", "Grim", "Ulg", "Drog",
    "Jor", "Kal", "Luk", "Mal", "Nim", "On", "Par", "Quor", "Rog", "Sar", "Tal", "Ur", "Vir", "Wen", "Xor", "Yor",
    "Ze", "Ba", "Da", "Fa", "Ga", "La", "Ma", "Na", "Pa", "Sa", "Ta", "Va", "Wa", "Xa", "Za", "Az", "Bael", "Cael",
    "Dael", "Fael", "Gael", "Hael", "Jael", "Kael", "Lael", "Mael", "Nael", "Pael", "Rael", "Sael", "Tael", "Vael",
    "Wael", "Xael", "Yael", "Zael", "Ael", "Bel", "Cel", "Del", "Fel", "Gel", "Hel", "Jel", "Kel", "Lel", "Mel", "Nel",
    "Pel", "Rel", "Sel", "Tel", "Vel", "Wel", "Xel", "Yel", "Zel"
]

roots = [
    "a", "e", "i", "o", "u", "ar", "er", "ir", "or", "ur", "an", "en", "in", "on", "un", "al", "el", "il", "ol", "ul",
    "am", "em", "im", "om", "um", "ath", "eth", "ith", "oth", "uth"
]

suffixes = [
    "ak", "bar", "dak", "eth", "gar", "han", "iath", "jar", "kar", "lan", "mir", "nar", "or", "par", "qar", "ral", 
    "sar", "tar", "ur", "var", "wan", "xar", "yar", "zor", "ath", "bath", "gath", "lath", "rath", "th", "dorn", "nath", 
    "thar", "vorn", "zor", "mar", "gorn", "thok", "nox", "dor", "mor", "ros", "las", "kar", "dir", "thas", "rax", "din", 
    "zor", "loth", "fax", "gon", "hin", "rox", "don", "koth", "lor", "fur", "tar", "zen", "jin", "xar", "tin", "ran", 
    "zen", "rak", "sar", "ton", "kar", "gar", "min", "dor", "vax", "kar", "sal", "vor", "tar", "mar", "lor", "dar", 
    "nar", "zan", "zor", "har", "lar", "zan", "xar", "gan", "dar", "sar", "var", "tar", "nar", "dar", "gan", "har", 
    "kar", "lar", "man", "nar", "ran", "san", "tan", "van", "wan", "xan", "yan", "zar", "bal", "dal", "fal", "gal", 
    "hal", "jal", "kal", "lal", "mal", "nal", "pal", "ral", "sal", "tal", "val", "wal", "xal", "yal", "zal", "bel", 
    "cel", "del", "fel", "gel", "hel", "jel", "kel", "lel", "mel", "nel", "pel", "rel", "sel", "tel", "vel", "wel", 
    "xel", "yel", "zel", "bir", "dir", "fir", "gir", "hir", "jir", "kir", "lir", "mir", "nir", "pir", "rir", "sir", 
    "tir", "vir", "wir", "xir", "yir", "zir", "bax", "dax", "fax", "gax", "jax", "kax", "lax", "max", "nax", "pax", 
    "rax", "sax", "tax", "vax", "wax", "xax", "yax", "zax", "bor", "cor", "dor", "for", "gor", "hor", "jor", "kor", 
    "lor", "mor", "nor", "por", "ror", "sor", "tor", "vor", "wor", "xor", "yor", "zor", "brak", "drak", "frak", 
    "grak", "hrak", "krak", "lrak", "mrak", "prak", "rrak", "trak", "vrak", "wrak", "xrak", "yrak", "zrak", "bryn", 
    "clyn", "dlyn", "flyn", "glyn", "hlyn", "jlyn", "klyn", "llyn", "mlyn", "nlyn", "plyn", "rlyn", "slyn", "tlyn", 
    "vlyn", "wlyn", "xlyn", "ylyn", "zlyn"
]

def gerar_nome():
    prefix = random.choice(prefixes)
    root = random.choice(roots)
    suffix = random.choice(suffixes)
    nome = f"{prefix}{root}{suffix}"
    return nome

class Monstro:
    def __init__(self, nome, tipo, pv, ca, dv, jp, ataques, moral, movimento, alinhamento, habitat, tamanho, qt, ts, xp, descricao, utilidades, habilidades_especiais):
        self.nome = nome
        self.tipo = tipo
        self.pv = pv
        self.ca = ca
        self.dv = dv
        self.jp = jp
        self.ataques = ataques
        self.moral = moral
        self.movimento = movimento
        self.alinhamento = alinhamento
        self.habitat = habitat
        self.tamanho = tamanho
        self.qt = qt
        self.ts = ts
        self.xp = xp
        self.descricao = descricao
        self.utilidades = utilidades
        self.habilidades_especiais = habilidades_especiais

    def __str__(self):
        ataques_str = "\n".join(self.ataques)
        habilidades_str = f"Habilidades Especiais: {self.habilidades_especiais}\n" if self.habilidades_especiais > 0 else ""
        return (f"Nome: {self.nome}\n"
                f"Descrição: {self.descricao}\n"
                f"Tipo: {self.tipo}, Tamanho: {self.tamanho}, Alinhamento: {self.alinhamento}, Habitat: {', '.join(self.habitat)}\n\n"
                f"Encontros: {self.qt}\n"
                f"XP: {self.xp}\n"
                f"Tesouro: {self.ts}\n"
                f"Movimento: {self.movimento}\n\n"
                f"DV [PV]: {self.dv} [{self.pv}]\n"
                f"CA: {self.ca}\n"
                f"JP: {self.jp}\n"
                f"MO: {self.moral}\n\n"
                f"Ataques:\n{ataques_str}\n"
                f"{habilidades_str}"
                f"Utilidades: {self.utilidades}\n")

def sortear_tipo_monstro():
    tipos = [
        "Humanoide", "Humanoide Monstruoso", "Gigante", "Animal", "Inseto",
        "Constructo", "Morto-vivo", "Planta", "Gosma", "Dragão", "Besta"
    ]
    return random.choice(tipos)

def gerar_habitat():
    habitats = [
        "Qualquer", "Planície", "Floresta", "Subterrâneos", "Montanhas", "Geleiras", "Pântanos",
        "Extraplanar", "Desertos", "Colinas", "Oceanos", "Urbano"
    ]
    num_habitats = random.randint(1, 3)
    habitat = random.sample(habitats, num_habitats)
    if "Qualquer" in habitat:
        return ["Qualquer"]
    return habitat

def gerar_tamanho(tipo):
    if tipo == "Gigante":
        tamanhos_possiveis = ["Grande", "Imenso", "Colossal"]
    else:
        tamanhos_possiveis = ["Miúdo", "Pequeno", "Médio", "Grande", "Imenso", "Colossal"]
    return random.choice(tamanhos_possiveis)

def gerar_dv(tamanho, tipo):
    dv_range = {
        "Miúdo": (1, 3),
        "Pequeno": (1, 4),
        "Médio": (3, 7),
        "Grande": (4, 11),
        "Imenso": (6, 15),
        "Colossal": (9, 30)
    }

    # Ajuste dos DV baseado no tipo de monstro
    tipo_modificadores = {
        "Humanoide": 0,
        "Humanoide Monstruoso": 1,
        "Inseto": -1,
        "Constructo": 1,
        "Morto-vivo": 1,
        "Planta": -1,
        "Gosma": 0,
        "Dragão": 3,
        "Gigante": 2,
        "Besta": 1
    }

    min_dv, max_dv = dv_range[tamanho]

    # Ajuste para chance de exceção (dois tamanhos para cima ou para baixo)
    probabilidade_excecao = random.randint(1, 100)
    if probabilidade_excecao <= 10:  # Ex: 10% de chance de exceção
        tamanhos = list(dv_range.keys())
        tamanho_atual_index = tamanhos.index(tamanho)

        if random.choice([True, False]):  # Determina se vai para cima ou para baixo
            novo_tamanho_index = min(tamanho_atual_index + 2, len(tamanhos) - 1)  # Ajuste para cima
        else:
            novo_tamanho_index = max(tamanho_atual_index - 2, 0)  # Ajuste para baixo

        novo_tamanho = tamanhos[novo_tamanho_index]
        min_dv, max_dv = dv_range[novo_tamanho]

    dv_base = random.randint(min_dv, max_dv)
    dv_final = dv_base + tipo_modificadores.get(tipo, 0)

    # Garantindo que os DVs não sejam negativos
    dv_final = max(1, dv_final)

    pv_medio = dv_final * 5
    return dv_final, pv_medio

def determinar_ataques_e_dano(dv):
    nomes_ataques = [
        "Garra", "Mordida", "Pancada", "Arma", "Toque", 
        "Chifre", "Ferrão", "Picada", "Espinhos", "Arco", 
        "Tentáculo","Cusparada","Pedrada"
    ]

    if dv < 1:
        qtd_ataques = 1
        base_ataque = 0
        danos_possiveis = ["1d3", "1d4", "1d6"]
    elif 1 <= dv <= 2:
        qtd_ataques = 1
        base_ataque = random.randint(1, 2)
        danos_possiveis = ["1d4", "1d6", "1d8"]
    elif 3 <= dv <= 4:
        qtd_ataques = 1
        base_ataque = random.randint(2, 4)
        danos_possiveis = ["1d4", "1d6", "2d4"]
    elif 5 <= dv <= 6:
        qtd_ataques = random.randint(1, 2)
        base_ataque = random.randint(4, 6)
        danos_possiveis = ["1d6", "1d8", "1d10"]
    elif 7 <= dv <= 8:
        qtd_ataques = random.randint(1, 2)
        base_ataque = random.randint(5, 8)
        danos_possiveis = ["1d6", "1d8", "2d8"]
    elif 9 <= 10:
        qtd_ataques = random.randint(1, 3)
        base_ataque = random.randint(7, 10)
        danos_possiveis = ["2d4", "2d6", "3d6"]
    elif 11 <= 15:
        qtd_ataques = random.randint(1, 3)
        base_ataque = random.randint(10, 12)
        danos_possiveis = ["2d4", "2d6", "2d8", "3d6"]
    elif 16 <= 20:
        qtd_ataques = random.randint(1, 3)
        base_ataque = random.randint(12, 14)
        danos_possiveis = ["2d6", "2d8", "3d6", "3d8"]
    elif 21 <= 25:
        qtd_ataques = random.randint(2, 4)
        base_ataque = random.randint(14, 16)
        danos_possiveis = ["3d6", "3d8", "4d6", "4d8"]
    elif 26 <= 30:
        qtd_ataques = random.randint(2, 4)
        base_ataque = random.randint(16, 18)
        danos_possiveis = ["3d8", "4d6", "4d8", "5d6"]

    ataques = []
    for i in range(qtd_ataques):
        dano = random.choice(danos_possiveis)
        num_ataques = random.randint(1, 3)
        nome_ataque = random.choice(nomes_ataques)
        nomes_ataques.remove(nome_ataque)  # Remover o ataque selecionado da lista
        
        # Chance de adicionar um bônus de dano fixo
        if random.randint(1, 100) <= 50:  # Ex: 50% de chance
            bonus_dano = random.randint(2, 5)
            dano += f"+{bonus_dano}"
        
        ataques.append(f"{num_ataques}x {nome_ataque} +{base_ataque}: {dano}")

    # Chance de exceção para monstro frágil com alto dano
    probabilidade_bonificacao = random.randint(1, 100)
    if dv <= 4 and probabilidade_bonificacao <= 20:  # Ex: 20% de chance
        ataques = [aumentar_dano(dano) for dano in ataques]

    # Chance de exceção para monstro robusto com baixo dano
    probabilidade_reducao = random.randint(1, 100)
    if dv > 4 and probabilidade_reducao <= 20:  # Ex: 20% de chance
        ataques = [reduzir_dano(dano) for dano in ataques]

    return ataques

def aumentar_dano(dano):
    # Lógica para aumentar o dano
    # Exemplo: multiplicar dano
    if "d4" in dano:
        return dano.replace("d4", "d6")
    elif "d6" in dano:
        return dano.replace("d6", "d8")
    elif "d8" in dano:
        return dano.replace("d8", "d10")
    else:
        return dano + "+"

def reduzir_dano(dano):
    # Lógica para reduzir o dano
    # Exemplo: reduzir a faixa de dano
    if "d10" in dano:
        return dano.replace("d10", "d8")
    elif "d8" in dano:
        return dano.replace("d8", "d6")
    elif "d6" in dano:
        return dano.replace("d6", "d4")
    else:
        return dano.replace("+", "")

def determinar_ca(dv, tamanho, agilidade, couraca):
    if dv < 1:
        if tamanho in ["Miúdo", "Pequeno"] or agilidade:
            ca_range = (12, 14)
        else:
            ca_range = (10, 12)
    elif 1 <= dv <= 2:
        if tamanho in ["Miúdo", "Pequeno"] or agilidade:
            ca_range = (12, 14)
        else:
            ca_range = (11, 13)
    elif 3 <= dv <= 4:
        if tamanho in ["Miúdo", "Pequeno"] or agilidade:
            ca_range = (13, 15)
        else:
            ca_range = (12, 14)
    elif 5 <= dv <= 6:
        if tamanho in ["Miúdo", "Pequeno"] or agilidade:
            ca_range = (14, 16)
        else:
            ca_range = (13, 15)
    elif 7 <= dv <= 8:
        if tamanho in ["Miúdo", "Pequeno"] or agilidade:
            ca_range = (15, 17)
        else:
            ca_range = (14, 16)
    elif 9 <= dv <= 10:
        if tamanho in ["Miúdo", "Pequeno"] or agilidade:
            ca_range = (16, 18)
        else:
            ca_range = (15, 17)
    else:
        if tamanho in ["Miúdo", "Pequeno"] or agilidade:
            ca_range = (17, 20)
        else:
            ca_range = (16, 18)

    ca = random.randint(*ca_range)

    # Adicionar chance de variabilidade
    probabilidade_bonificacao = random.randint(1, 100)
    if probabilidade_bonificacao <= 20:
        if tamanho in ["Grande", "Imenso", "Colossal"] and agilidade:
            ca += 2  # Monstro grande mas difícil de acertar
        elif tamanho in ["Miúdo", "Pequeno"] and  agilidade:
            ca -= 2  # Monstro pequeno mas lento
    elif couraca:
        ca += 3  # Couraça adiciona bônus de CA

    return ca

def sortear_alinhamento():
    alinhamentos = ["Caótico", "Neutro", "Ordeiro"]
    return random.choice(alinhamentos)

def determinar_jp(dv, ligacao_magica):
    if dv < 1:
        jp_range = (4, 5) if ligacao_magica else (4, 4)
    elif 1 <= dv <= 2:
        jp_range = (5, 6) if ligacao_magica else (5, 5)
    elif 3 <= dv <= 4:
        jp_range = (6, 7) if ligacao_magica else (6, 6)
    elif 5 <= dv <= 6:
        jp_range = (8, 9) if ligacao_magica else (8, 8)
    elif 7 <= dv <= 8:
        jp_range = (10, 11) if ligacao_magica else (10, 10)
    elif 9 <= dv <= 10:
        jp_range = (11, 12) if ligacao_magica else (11, 11)
    elif 11 <= dv <= 12:
        jp_range = (12, 14) if ligacao_magica else (12, 12)
    elif 13 <= dv <= 14:
        jp_range = (13, 15) if ligacao_magica else (13, 13)
    elif 15 <= dv <= 19:
        jp_range = (14, 16) if ligacao_magica else (14, 14)
    elif 20 <= dv <= 39:
        jp_range = (15, 17) if ligacao_magica else (15, 15)
    elif 40 <= dv <= 69:
        jp_range = (17, 19) if ligacao_magica else (17, 17)
    else:
        jp_range = (19, 19)  # Independente de ligação mágica

    return random.randint(*jp_range)

def determinar_moral():
    return random.randint(2, 12)

def determinar_habilidades_especiais():
    tem_habilidades = random.choice([True, False])
    if tem_habilidades:
        return random.randint(1, 5)
    else:
        return 0

def calcular_xp(dv, habilidades_especiais):
    tabela_xp = {
        0: 5,
        1: 15,
        2: 35,
        3: 75,
        4: 125,
        5: 175,
        6: 270,
        7: 420,
        8: 650,
        9: 925,
        10: 1250
    }
    
    if dv <= 10:
        xp_base = tabela_xp[dv]
    else:
        xp_base = 1250 + 350 * (dv - 10)
    
    bonus_habilidades = habilidades_especiais * (habilidades_especiais * 5)
    return xp_base + bonus_habilidades

def determinar_encontros():
    grupos = ["1", "1d3", "1d6", "2d6", "2d4", "2d10", "1d10", "3d10", "1d4", "4d4"]
    return random.choice(grupos)

def determinar_tesouro():
    tesouros = [chr(i) for i in range(ord('A'), ord('V') + 1)]
    return random.choice(tesouros)

def determinar_movimento():
    movimentos_normais = [3, 6, 9, 10, 12, 15, 18, 21]
    tipos_movimento = ["V", "N", "E", "C", "O"]

    # Determinar movimento normal
    movimento_normal = random.choice(movimentos_normais)

    # Chance de adicionar movimento especial
    movimento_especial = ""
    if random.randint(1, 100) <= 30:  # Ex: 20% de chance de movimento especial
        movimento_especial_tipo = random.choice(tipos_movimento)
        movimento_especial_valor = random.choice(movimentos_normais)
        movimento_especial = f" / {movimento_especial_valor}{movimento_especial_tipo}"

    return f"{movimento_normal}{movimento_especial}"

    # Função para gerar característica física fragmentada
    def gerar_caracteristica_fisica():
        partes_corpo = [
            "cauda", "pele", "olhos", "asas", "chifres", 
            "garras", "dentes", "escamas", "patas", "membros"
        ]
        atributos = [
            "afiadas", "pontiagudos", "escamosa", "brilhantes", "enormes", 
            "curvos", "coriácea", "retráteis", "preênsil", "musculoso",
            "venenosas", "flamejantes", "gélidas", "petrificantes", "venenosas"
        ]
        cores_adicionais = [
            "vermelha", "verde", "azul", "negra", "dourada", 
            "prateada", "translúcida", "luminescente", "iridescente", "sombria",
            "púrpura", "branca", "acinzentada", "marrom", "amarela"
        ]

        parte_corpo = random.choice(partes_corpo)
        atributo = random.choice(atributos)
        cor_adicional = random.choice(cores_adicionais)
        return f"{parte_corpo} {atributo} {cor_adicional}"

    # Selecionar atributos aleatoriamente
    rep = random.choice(reputacao)
    ativ = random.choice(atividade)
    caract_fisica = gerar_caracteristica_fisica()
    tipo_sociedade = random.choice(tipos_sociedade)
    caract_ataque = random.choice(caracteristica_ataque)
    subst = random.choice(substantivos)
    final = random.choice(finalidade)

    # Definir templates com base no tipo de monstro
    if tipo == "Humanoide":
        templates = [
            "{nome} são {reputacao} por suas {atividade} nas {habitat}.",
            "{nome} são {reputacao} por suas {tipos_sociedade} onde usam seus {caracteristica_ataque} como {substantivos}."
        ]
    elif tipo == "Humanoide Monstruoso":
        templates = [
            "{nome} são {reputacao} e conhecidos por {atividade} nas {habitat}.",
            "{nome} habitam {habitat} e são {reputacao}, utilizando {caracteristica_ataque} para {finalidade}."
        ]
    # Adicione mais condições para os outros tipos conforme necessário
    else:
        templates = [
            "{nome} é um {tipo} que habita {habitat}. Eles são conhecidos por serem {reputacao} e possuem {caracteristica_fisica}."
        ]

    # Selecionar e preencher um template aleatoriamente
    template = random.choice(templates)
    descricao = template.format(
        nome=nome,
        tipo=tipo,
        habitat=habitat,
        reputacao=rep,
        atividade=ativ,
        caracteristica_fisica=caract_fisica,
        tipos_sociedade=tipo_sociedade,
        caracteristica_ataque=caract_ataque,
        substantivos=subst,
        finalidade=final
    )
    return descricao

def gerar_descricao(nome, tipo, habitat):
    reputacao = [
        "temidos", "respeitados", "temíveis", "admirados", "odiados",
        "venerados", "desprezados", "reconhecidos", "infames", "celebrados","corajosos","leais","traiçoeiros",
        "famosos", "covardes"
    ]
    atividade = [
        "caçar", "vigiar", "proteger", "explorar", "pilhar", 
        "construir", "destruir", "colecionar artefatos", "cultivar", "patrulhar","adorar","exterminar"
    ]
    tipos_sociedade = [
        "anárquica", "teológica", "tribal", "monárquica", "comunista", 
        "democrática", "feudal", "militarista", "nomádica", "oligárquica", 
        "autocrática", "mercantilista", "tecnocrática"
    ]
    caracteristica_ataque = [
        "força bruta", "agilidade", "magia poderosa", "habilidade de furtividade", 
        "veneno letal", "poderes psíquicos", "resistência", "velocidade", 
        "regeneração", "armadura natural"
    ]
    substantivos = [
        "símbolos de poder", "armas temíveis", "ferramentas de guerra", "talismãs", 
        "artefatos antigos", "relíquias", "amuletos", "poções", 
        "mascotes de guerra", "escudos"
    ]
    finalidade = [
        "dominar territórios", "proteger seus lares", "caçar presas", "conquistar reinos", 
        "defender seu líder", "buscar vingança", "expandir seus domínios", "realizar rituais", 
        "estabelecer colônias", "extrair recursos"
    ]

    # Função para gerar característica física fragmentada
    def gerar_caracteristica_fisica():
        partes_corpo = [
            "cauda", "pele", "olhos", "asas", "chifres", 
            "garras", "dentes", "escamas", "patas", "membros"
        ]
        atributos = [
            "afiadas", "pontiagudos", "escamosa", "brilhantes", "enormes", 
            "curvos", "coriácea", "retráteis", "preênsil", "musculoso",
            "venenosas", "flamejantes", "gélidas", "petrificantes", "venenosas"
        ]
        cores_adicionais = [
            "vermelha", "verde", "azul", "negra", "dourada", 
            "prateada", "translúcida", "luminescente", "iridescente", "sombria",
            "púrpura", "branca", "acinzentada", "marrom", "amarela"
        ]

        parte_corpo = random.choice(partes_corpo)
        atributo = random.choice(atributos)
        cor_adicional = random.choice(cores_adicionais)
        return f"{parte_corpo} {atributo} {cor_adicional}"

    # Selecionar atributos aleatoriamente
    rep = random.choice(reputacao)
    ativ = random.choice(atividade)
    caract_fisica = gerar_caracteristica_fisica()
    tipo_sociedade = random.choice(tipos_sociedade)
    caract_ataque = random.choice(caracteristica_ataque)
    subst = random.choice(substantivos)
    final = random.choice(finalidade)

    # Definir templates com base no tipo de monstro
    if tipo == "Humanoide":
        templates = [
            "{nome} são {reputacao} por suas {atividade} nas {habitat}.",
            "{nome} são {reputacao} por suas {tipos_sociedade} onde usam seus {caracteristica_ataque} como {substantivos}."
        ]
    elif tipo == "Humanoide Monstruoso":
        templates = [
            "{nome} são {reputacao} e conhecidos por {atividade} nas {habitat}.",
            "{nome} habitam {habitat} e são {reputacao}, utilizando {caracteristica_ataque} para {finalidade}."
        ]
    elif tipo == "Inseto":
        templates = [
            "{nome} são frequentemente vistos em {habitat}, conhecidos por serem {reputacao} e possuírem {caracteristica_fisica}.",
            "Nas {habitat}, {nome} são {reputacao} e se destacam por suas {caracteristica_fisica} e {atividade}."
        ]
    elif tipo == "Constructo":
        templates = [
            "{nome}, criados para {finalidade}, são encontrados em {habitat} e são {reputacao}.",
            "Esses {nome} são {reputacao}, construídos para {atividade} nas {habitat}."
        ]
    elif tipo == "Morto-vivo":
        templates = [
            "{nome} são {reputacao}, vagando pelas {habitat} com suas {caracteristica_fisica}.",
            "Nas {habitat}, {nome} são {reputacao}, conhecidos por {atividade} e {caracteristica_fisica}."
        ]
    elif tipo == "Planta":
        templates = [
            "{nome} crescem nas {habitat}, onde são {reputacao} e possuem {caracteristica_fisica}.",
            "Nas {habitat}, {nome} são {reputacao}, destacando-se por suas {caracteristica_fisica} e {atividade}."
        ]
    elif tipo == "Gosma":
        templates = [
            "{nome} são {reputacao}, frequentemente encontrados em {habitat}, onde suas {caracteristica_fisica} são notáveis.",
            "Nas {habitat}, {nome} são {reputacao} e se distinguem por suas {caracteristica_fisica} e {atividade}."
        ]
    elif tipo == "Dragão":
        templates = [
            "{nome} são {reputacao}, reinando sobre as {habitat} com suas {caracteristica_fisica}.",
            "Esses {nome} são {reputacao}, conhecidos por {atividade} nas {habitat}."
        ]
    elif tipo == "Gigante":
        templates = [
            "{nome} são {reputacao}, vagando pelas {habitat} com suas {caracteristica_fisica}.",
            "Nas {habitat}, {nome} são {reputacao}, utilizando {caracteristica_ataque} para {finalidade}."
        ]
    elif tipo == "Besta":
        templates = [
            "{nome} são {reputacao}, encontrados em {habitat}, conhecidos por suas {caracteristica_fisica}.",
            "Esses {nome} habitam {habitat} e são {reputacao}, destacando-se por {atividade} e {caracteristica_fisica}."
        ]
    else:
        templates = [
            "{nome} é um {tipo} que habita {habitat}. Eles são conhecidos por serem {reputacao} e possuem {caracteristica_fisica}."
        ]

    # Selecionar e preencher um template aleatoriamente
    template = random.choice(templates)
    descricao = template.format(
        nome=nome,
        tipo=tipo,
        habitat=", ".join(habitat),  # Usar o mesmo habitat gerado
        reputacao=rep,
        atividade=ativ,
        caracteristica_fisica=caract_fisica,
        tipos_sociedade=tipo_sociedade,
        caracteristica_ataque=caract_ataque,
        substantivos=subst,
        finalidade=final
    )
    return descricao

def gerar_utilidades(nome, tipo):
    usos = [
        "pode ser usado como ingrediente em poções",
        "serve como material para fabricar armas",
        "é utilizado em rituais mágicos",
        "pode ser vendido por um bom preço",
        "é procurado por colecionadores",
        "tem propriedades curativas",
        "é usado para criar armaduras",
        "tem um sabor exótico",
        "é um componente em alquimia",
        "é usado para encantamentos"
    ]

    propriedades = [
        "curativas", "venenosas", "explosivas", "luminescentes", 
        "mágicas", "petrificantes", "regenerativas", "flamejantes", 
        "gélidas", "psíquicas", "telepáticas", "telecinéticas", 
        "hipnóticas", "metamórficas", "antimagia", "repelentes"
    ]

    aplicacoes = [
        "na medicina", "na alquimia", "na criação de itens mágicos", 
        "na construção", "na culinária", "em rituais", "em combates", 
        "em armadilhas", "em estratégias de guerra", "em defesas"
    ]

    # Selecionar atributos aleatoriamente
    uso = random.choice(usos)
    propriedade = random.choice(propriedades)
    aplicacao = random.choice(aplicacoes)

    # Definir templates
    templates = [
        "{nome} {uso} e tem propriedades {propriedade}.",
        "As partes de {nome} são {uso} e são muito valiosas {aplicacao}.",
        "{nome} é conhecido por suas propriedades {propriedade}, tornando-o útil {aplicacao}."
    ]

    # Selecionar e preencher um template aleatoriamente
    template = random.choice(templates)
    utilidade = template.format(
        nome=nome,
        uso=uso,
        propriedade=propriedade,
        aplicacao=aplicacao
    )
    return utilidade


def generate_monster():
    nome = gerar_nome()  # Gerar o nome do monstro
    tipo = sortear_tipo_monstro()  # Sortear o tipo do monstro
    tamanho = gerar_tamanho(tipo)  # Gerar o tamanho do monstro com base no tipo
    dv, pv_medio = gerar_dv(tamanho, tipo)  # Gerar DV e PV médios
    ca = determinar_ca(dv, tamanho=tamanho, agilidade=True, couraca=False)  # Determinar CA
    jp = determinar_jp(dv, ligacao_magica=True)  # Determinar JP
    moral = determinar_moral()  # Determinar moral
    movimento = determinar_movimento()  # Determinar movimento
    alinhamento = sortear_alinhamento()  # Sortear alinhamento
    habitat = gerar_habitat()  # Gerar habitat
    qt = determinar_encontros()  # Determinar encontros
    ts = determinar_tesouro()  # Determinar tesouro
    habilidades_especiais = determinar_habilidades_especiais()  # Determinar habilidades especiais
    xp = calcular_xp(dv, habilidades_especiais)  # Calcular XP
    descricao = gerar_descricao(nome, tipo, habitat)  # Gerar a descrição
    utilidades = gerar_utilidades(nome, tipo)  # Gerar a utilidade
    ataques = determinar_ataques_e_dano(dv)  # Determinar ataques e dano

    monstro = Monstro(nome, tipo, pv_medio, ca, dv, jp, ataques, moral, movimento, alinhamento, habitat, tamanho, qt, ts, xp, descricao, utilidades, habilidades_especiais)
    return {
        'nome': monstro.nome,
        'descricao': monstro.descricao,
        'tipo': monstro.tipo,
        'tamanho': monstro.tamanho,
        'alinhamento': monstro.alinhamento,
        'habitat': monstro.habitat,
        'qt': monstro.qt,
        'xp': monstro.xp,
        'ts': monstro.ts,
        'movimento': monstro.movimento,
        'dv': monstro.dv,
        'pv': monstro.pv,
        'ca': monstro.ca,
        'jp': monstro.jp,
        'moral': monstro.moral,
        'ataques': monstro.ataques,
        'habilidades_especiais': monstro.habilidades_especiais,
        'utilidades': monstro.utilidades
    }

if __name__ == "__main__":
    monstro_gerado = generate_monster()
    print(monstro_gerado)
