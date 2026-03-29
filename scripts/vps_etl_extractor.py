import pyodbc
import pandas as pd
import datetime
import os
import sys

# ==============================================================================
# SCRIPT DE EXTRAÇÃO E PROCESSAMENTO - NÍVEL ESTRATÉGICO
# Ambiente: VPS
# Finalidade: Conectar via ODBC ao ERP GTEX (ou outro DB de origem),
#             extrair vendas, aplicar filtros de negócio e salvar dados prontos.
# ==============================================================================

def get_db_connection():
    """
    Estabelece conexão com o banco de dados via ODBC configurado na VPS.
    Ajuste as strings de conexão conforme o DSN ou driver do SQL Server/Firebird.
    """
    try:
        # Exemplo com string de DSN:
        # conn_str = 'DSN=GTEX_BETA;UID=usuario;PWD=senha'
        
        # Exemplo com driver direto (SQL Server):
        conn_str = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=SEU_SERVIDOR_AQUI;"
            "DATABASE=SEU_BANCO_DE_DADOS;"
            "UID=SEU_USUARIO;"
            "PWD=SUA_SENHA;"
        )
        # conn = pyodbc.connect(conn_str)
        # return conn
        print("[-] Parâmetros de conexão ODBC aguardando preenchimento manual pelo usuário.")
        return None
    except Exception as e:
        print(f"[ERROR] Falha ao conectar no ODBC: {e}")
        sys.exit(1)

def extract_commercial_data():
    """
    Puxa os dados brutos e já aplica os filtros de negócio (nível estratégico).
    """
    conn = get_db_connection()
    if not conn:
        print("[-] Simulando dados extraídos para o desenvolvimento inicial.")
        return simulate_data()

    # Query SQL aplicando o filtro da regra de negócio (S e SM)
    query = """
    SELECT 
        DATA_EMISSAO,
        NUMTRANS AS TRANSAÇÃO,
        COD_CLIENTE,
        MARCA,
        VLPROD AS FATURAMENTO,
        PESO_BRUTO AS VOLUME_KG,
        COD_OPER AS OPERACAO
    FROM MOVIMENTACOES
    WHERE COD_OPER IN ('S', 'SM') 
      AND DATA_EMISSAO >= DATEADD(year, -2, GETDATE())
    """
    print("[*] Extraindo dados via Banco de Dados ODBC...")
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def simulate_data():
    """
    Retorna um DataFrame simulado para testar e validar o código antes da conexão real.
    """
    dados = {
        'DATA_EMISSAO': [datetime.date(2025, 1, 15), datetime.date(2025, 2, 20), datetime.date(2026, 1, 10), datetime.date(2026, 2, 18)],
        'TRANSAÇÃO': [1001, 1002, 2001, 2002],
        'COD_CLIENTE': ['C001', 'C002', 'C001', 'C003'],
        'MARCA': ['Marca A', 'Marca B', 'Marca A', 'Marca C'],
        'FATURAMENTO': [1500.00, 2300.50, 1800.00, 3100.20],
        'VOLUME_KG': [50.5, 80.0, 60.0, 120.5],
        'OPERACAO': ['S', 'SM', 'S', 'S']
    }
    return pd.DataFrame(dados)

def process_strategic_kpis(df):
    """
    Processa os indicadores estratégicos.
    Como o volume do Looker Studio já agrega o somatório, a principal lógica
    aqui é consolidar a tabela base e garantir a qualidade dos campos.
    """
    print("[*] Iniciando transformação de KPIs Estratégicos...")
    
    # 1. Garantir tipos de dados corretos
    df['DATA_EMISSAO'] = pd.to_datetime(df['DATA_EMISSAO'])
    df['ANO'] = df['DATA_EMISSAO'].dt.year
    df['MES'] = df['DATA_EMISSAO'].dt.month
    
    # 2. Agregações para tabelas intermediárias destinadas ao Looker Studio ou BD (PostgreSQL/MySQL)
    print("[-] Preparando tabela Fato limpa (Vendas_Filtradas_Estrategico)")
    # O df extraído já está filtrado (COD_OPER = S, SM)
    
    return df

def main():
    print("==================================================")
    print(" ETL COMERCIAL ESTRATÉGICO - SUPPRA FOODS - VPS")
    print("==================================================")
    
    # 1. Extração
    df_raw = extract_commercial_data()
    print(f"[+] Linhas extraídas: {len(df_raw)}")
    
    # 2. Transformação (Cálculos de Regras Base)
    df_processed = process_strategic_kpis(df_raw)
    
    # 3. Carga (Exportar para BD Local ou CSV para consumo do Looker/PowerBI)
    output_dir = r"h:\Meu Drive\PROJETOS\DASHBOARD SUPPRA FOODS\SISTEMA ERP - GTEX"
    os.makedirs(output_dir, exist_ok=True)
    out_file = os.path.join(output_dir, "vps_fato_comercial_estrategico.csv")
    
    df_processed.to_csv(out_file, index=False, sep=';', decimal=',')
    print(f"[+] Dados salvos com sucesso em: {out_file}")
    
    # O Looker Studio deverá apontar para a tabela no novo Banco de Dados (ou para esse CSV, por enquanto).

if __name__ == "__main__":
    main()
