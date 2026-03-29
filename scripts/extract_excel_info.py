import zipfile
import re

excel_file = r'h:\My Drive\PROJETOS\DASHBOARD SUPPRA FOODS\EXCEL\COMERCIAL.xlsx'

with zipfile.ZipFile(excel_file, 'r') as z:
    for filename in z.namelist():
        if 'connections.xml' in filename or 'query' in filename.lower() or 'customxml' in filename.lower():
            try:
                content = z.read(filename).decode('utf-8', errors='ignore')
                print(f"\n--- {filename} ---")
                
                # Extract CommandText for SQL
                cmd_match = re.search(r'commandText="([^"]+)"', content)
                if cmd_match:
                    cmd = cmd_match.group(1).replace('&#13;', '\n').replace('&#10;', '\n').replace('&quot;', '"').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
                    print("SQL Command Found:\n", cmd)
                
                # Power Query / Mashup
                if 'Provider=Microsoft.Mashup.OleDb' in content:
                    print("This uses Power Query (Mashup).")
                    
                # Look for other interesting pieces
                if 'connectionString' in content:
                    conn_match = re.search(r'connectionString="([^"]+)"', content)
                    if conn_match:
                        print("Connection String:", conn_match.group(1))
                        
            except Exception as e:
                print(f"Error reading {filename}: {e}")
