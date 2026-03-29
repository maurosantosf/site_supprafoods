import zipfile
import re

excel_path = r'h:\My Drive\PROJETOS\DASHBOARD SUPPRA FOODS\EXCEL\COMERCIAL.xlsx'

sql_encontrado = []

try:
    with zipfile.ZipFile(excel_path, 'r') as z:
        for filename in z.namelist():
            # Muitas vezes queries nativas ou strings de conexão vazam em plain text no customXml
            if filename.startswith('customXml/item') and filename.endswith('.xml'):
                content = z.read(filename).decode('utf-8', errors='ignore')
                
                # Busca por Selects
                matches = re.findall(r'(?i)(select\s+.*?(?:from|where)\s+[^<]+)', content)
                for m in matches:
                    if len(m) > 20 and 'sqlite' not in m.lower():
                        sql_encontrado.append(f"Fonte: {filename}\nQuery: {m.strip()}\n")

    print(f"=== BUSCA DIRETA CONCLUÍDA ===")
    if sql_encontrado:
        for s in set(sql_encontrado):
            print(s)
            print("-" * 50)
    else:
        print("Nenhuma query explícita em texto legível encontrada. As queries estão totalmente binárias no Mashup.")
                
except Exception as e:
    print(f"Erro ao ler pacote Excel: {e}")
