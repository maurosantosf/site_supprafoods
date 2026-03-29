import sys
import zipfile
import re
import base64
import zlib

def extract_m_code_from_excel(filepath):
    """Extrai os códigos M (Power Query) embutidos em um arquivo Excel (.xlsx)."""
    try:
        with zipfile.ZipFile(filepath, 'r') as z:
            
            customXml_files = [f for f in z.namelist() if f.startswith('customXml/item') and f.endswith('.xml')]
            
            for file in customXml_files:
                content = z.read(file).decode('utf-8', errors='ignore')
                
                if '<DataMashup' in content:
                    
                    b64_match = re.search(r'>([^<]+)</DataMashup>', content)
                    if b64_match:
                        try:
                            blob = base64.b64decode(b64_match.group(1))
                            
                            # O Power Query Mashup Blob tem uma estrutura bem específica
                            # As Queries "M" estão em plain text no meio do binário (UTF-8 ou UTF-16)
                            # ou compactadas. Vamos forçar uma busca de texto.
                            
                            text_utf8 = blob.decode('utf-8', errors='ignore')
                            
                            # M Code features costumam ter "let" e "in", ou "Odbc.DataSource"
                            if 'Odbc.' in text_utf8 or 'Sql.' in text_utf8 or 'let' in text_utf8:
                                print(f"\n--- POTENCIAL CÓDIGO M ENCONTRADO EM {file} ---")
                                
                                # Extração rudimentar: Pega blocos que pareçam com M Code (let ... in ...)
                                m_blocks = re.findall(r'(let[\s\S]+?in[\s\S]+?)(?:\x00|PK)', text_utf8)
                                for idx, block in enumerate(m_blocks):
                                    if 'Odbc' in block or 'Sql' in block or 'SELECT' in block.upper():
                                        print(f"\n[BLOCO {idx+1}]")
                                        # Limpa binários em volta
                                        clean_block = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]', '', block)
                                        print(clean_block.strip())
                                        
                        except Exception as e:
                            print(f"Erro ao processar blob em {file}: {e}")

    except Exception as e:
        print(f"Erro ao abrir arquivo Excel: {e}")

if __name__ == '__main__':
    excel_file = r'h:\My Drive\PROJETOS\DASHBOARD SUPPRA FOODS\EXCEL\COMERCIAL.xlsx'
    extract_m_code_from_excel(excel_file)
