import pyodbc
import pandas as pd
from datetime import datetime
import os

# ==========================================
# CONFIGURAÇÕES DE CONEXÃO ODBC (PREENCHA AQUI)
# ==========================================
# Insira os dados da sua conexão (DSN) ou os parâmetros diretos
DB_NAME = "[NOME DO BANCO DE DADOS]" # O nome do banco será inserido aqui quando você informar
DSN = "[SEU_DSN_AQUI]"
UID = "[SEU_USUARIO_AQUI]"
PWD = "[SUA_SENHA_AQUI]"

# Se for usar DSN:
CONNECTION_STRING = f"DSN={DSN};UID={UID};PWD={PWD};DATABASE={DB_NAME}"

# Se for usar conexão direta sem DSN (exemplo caso seja SQL Server e precise do Server/Driver):
# DRIVER = "{ODBC Driver 17 for SQL Server}"
# SERVER = "[IP_OU_NOME_DO_SERVIDOR_VPN]"
# CONNECTION_STRING = f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DB_NAME};UID={UID};PWD={PWD}"

def extrair_dados_vendas():
    """
    Conecta ao banco de dados ERP, extrai e agrega os dados no nível estratégico (agrupamento mensal).
    """
    try:
        print("Estabelecendo conexão com o DB do ERP via ODBC...")
        # Descomente a linha abaixo quando preencher os dados reais.
        # conn = pyodbc.connect(CONNECTION_STRING)
        print("Conexão estabelecida com sucesso!")
        
        # A query abaixo assume a sintaxe do SQL Server como exemplo e traz a base agregada por mês.
        # Você deve ajustar NOME_DA_TABELA e o nome exato das colunas de acordo com o esquema do ERP.
        sql_query = """
        SELECT 
            -- Agrupamento por mês/ano. A função FORMAT depende do banco (SQL Server usado como exemplo).
            FORMAT(DATA_VENDA, 'yyyy-MM') AS Mes_Ano,
            
            -- Positivação: Contagem distinta de transações (pedidos ou notas fiscais)
            COUNT(DISTINCT NUMERO_TRANSACAO) AS Positivacao,
            
            -- Faturamento Total R$
            SUM(VALOR_FATURAMENTO) AS Faturamento_Total,
            
            -- Volume (Kg) Total
            SUM(VOLUME_KG) AS Volume_Total_Kg
            
        FROM 
            NOME_DA_TABELA_DE_VENDAS -- SUBSTITUA a tabela pela real do ERP
        WHERE 
            COD_OPER IN ('S', 'SM')
            -- Sugestão de filtro de período para agilizar a leitura, descomente se desejar:
            -- AND DATA_VENDA >= '2024-01-01' 
        GROUP BY 
            FORMAT(DATA_VENDA, 'yyyy-MM')
        ORDER BY 
            Mes_Ano DESC
        """
        
        print("Executando a query e extraindo dados...\n")
        # Descomente a linha abaixo quando tiver dados de conexão preenchidos.
        # df = pd.read_sql(sql_query, conn)
        
        # --- BLOCO DE TESTE MOCKADO (Remover/comentar assim que conectar com o DB real) ---
        dados_mock = {
            'Mes_Ano': ['2026-03', '2026-02', '2026-01'],
            'Positivacao': [1500, 1800, 1750],
            'Faturamento_Total': [250000.50, 310500.20, 290100.80],
            'Volume_Total_Kg': [12500.5, 15000.2, 14200.7]
        }
        df = pd.DataFrame(dados_mock)
        # ----------------------------------------------------------------------------------

        # Cálculo dos Tickets Médios no Pandas 
        # (É mais seguro calcular aqui do que no SQL para garantir flutuantes e evitar erros de divisão por zero)
        if not df.empty:
            df['Ticket_Medio_RS'] = df['Faturamento_Total'] / df['Positivacao']
            df['Ticket_Medio_KG'] = df['Volume_Total_Kg'] / df['Positivacao']
            
            # Arredondamentos e tratativas
            df['Faturamento_Total'] = df['Faturamento_Total'].round(2)
            df['Volume_Total_Kg'] = df['Volume_Total_Kg'].round(3)
            df['Ticket_Medio_RS'] = df['Ticket_Medio_RS'].round(2)
            df['Ticket_Medio_KG'] = df['Ticket_Medio_KG'].round(3)
        else:
            print("Aviso: Nenhum dado retornado pela query.")
            
        return df

    except Exception as e:
        print(f"Erro na conexão ou extração de dados: {e}")
        return None
    finally:
        # Garante o fechamento da conexão se ela foi instanciada
        if 'conn' in locals():
            # conn.close() # Descomente quando usar pyodbc
            print("Conexão fechada.")

def salvar_csv(df, nome_arquivo="dados_estrategicos_mensais.csv"):
    """
    Salva o DataFrame em um arquivo CSV para leitura no Looker Studio.
    """
    if df is not None and not df.empty:
        # Salva o arquivo no mesmo diretório em que esse script está localizado
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_arquivo = os.path.join(diretorio_atual, nome_arquivo)
        
        # Separador de colunas como ';' e decimal como ',' é o padrão pt-BR utilizado 
        # e reconhecido mais facilmente por algumas planilhas e o Data Studio
        df.to_csv(caminho_arquivo, index=False, sep=';', decimal=',')
        
        print(f"Sucesso! Arquivo '{nome_arquivo}' gerado em:\n{caminho_arquivo}\n")
        print("Prévia dos Dados Processados:")
        print(df.to_string(index=False))
    else:
        print("Não foi possível gerar o arquivo CSV pois os dados extraídos estão vazios.")

if __name__ == "__main__":
    print(f"=== ETL ESTRATÉGICO LOG - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ===")
    df_vendas = extrair_dados_vendas()
    salvar_csv(df_vendas)
    print("=== PROCESSO FINALIZADO ===")
