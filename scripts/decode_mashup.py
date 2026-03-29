import base64
import re
import zipfile
import xml.etree.ElementTree as ET

# O Excel salva as queries do Power Query encodificadas em Base64 dentro do DataMashup
mashup_file = r'h:\My Drive\PROJETOS\DASHBOARD SUPPRA FOODS\EXCEL\COMERCIAL_UNZIPPED\customXml\item49.xml'

try:
    tree = ET.parse(mashup_file)
    root = tree.getroot()
    # Pega o texto do elemento raiz (o base64 gigante)
    if root.text:
        base64_data = root.text
        decoded_bytes = base64.b64decode(base64_data)
        
        # O Power Query zipa o conteúdo dentro do base64. 
        # Nós procuramos assinaturas internas (PK) ou tentamos extrair strings.
        # Por segurança, vamos apenas procurar padrões SQL no texto decodificado
        # que mesmo parcialmente binário manterá strings ASCII visíveis.
        
        texto_decodificado = decoded_bytes.decode('utf-8', errors='ignore')
        
        print("Buscando padrões Select/From/Where...")
        queries = re.findall(r'(?i)(select\s+.*?from\s+.*?)(?:\s+where|\n|$)', texto_decodificado, re.DOTALL)
        if queries:
            print("\n=== QUERIES ECONTRADAS ===")
            for q in set(queries):
                if 'NUMPED' in q or 'DATA' in q or 'COD_OPER' in q: # Filtro básico pra não pegar lixo
                    print(q)
                    print("-" * 50)
        else:
            print("\nQueries SQL explícitas não encontradas no formato esperado. Talvez elas estejam dentro do zip interno da Mashup.")
            
            # Vamos tentar salvar o conteúdo como binário pra extrair o zip depois, se precisar
            with open('mashup.bin', 'wb') as f:
                f.write(decoded_bytes)
            print("Blob salvo como mashup.bin para análise se necessário.")
            
except Exception as e:
    print(f"Erro ao ler Mashup: {e}")
