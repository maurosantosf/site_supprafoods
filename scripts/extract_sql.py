import re

try:
    with open('mashup.bin', 'rb') as f:
        data = f.read().decode('utf-8', errors='ignore')

    print("--- INICIANDO BUSCA DE SQL ---")
    
    # Procura blocos que se pareçam com comandos SQL. 
    # Como o arquivo pode ter sujeira binária, o regex busca algo no formato:
    # "select ... from ..." ou outras keywords
    matches = re.findall(r'(?i)(select\s+[^\n]+?from\s+[^\n\"]+)', data)
    
    if not matches:
        print("Nenhum SELECT explícito de linha única encontrado, tentando busca mais flexível...")
        # Busca mais ampla, pega palavras chave perto
        matches = re.findall(r'(?i)(select[\s\S]{10,500}from[\s\S]{5,100}where.*)', data)
        
    for m in set(matches):
        # Ignora lixos do Power Query muito curtos ou consultas internas de sistema
        if len(m) > 30 and 'sqlite' not in m.lower():
            print("\n> Possível Query Encontrada:")
            print(m.strip()[:1000]) # Imprime até 1000 chars

    print("\n--- BUSCA FINALIZADA ---")

except Exception as e:
    print(f"Erro: {e}")
