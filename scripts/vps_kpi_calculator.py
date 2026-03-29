import pandas as pd
import datetime

# ==============================================================================
# SCRIPT DE PROCESSAMENTO E KPI DE NÍVEL ESTRATÉGICO
# Ambiente: VPS
# Finalidade: Ler os dados filtrados gerados pelo ETL principal e calcular
#             indicadores agregados (Rankings, YoY temporais) prontos para BD ou Front.
# ==============================================================================

def calculate_ticket_medio(df_raw):
    """
    Positivação (Qtd) = Contagem de transações ativas
    Ticket Médio (Faturamento / Qtd) e (Volume / Qtd)
    """
    if df_raw.empty:
        return pd.DataFrame()
        
    df_agrupado = df_raw.groupby(['ANO', 'MES']).agg(
        FATURAMENTO_TOTAL=('FATURAMENTO', 'sum'),
        VOLUME_TOTAL=('VOLUME_KG', 'sum'),
        POSITIVACAO_QTD=('TRANSAÇÃO', 'nunique')
    ).reset_index()
    
    df_agrupado['TICKET_MEDIO_R$'] = df_agrupado['FATURAMENTO_TOTAL'] / df_agrupado['POSITIVACAO_QTD']
    df_agrupado['TICKET_MEDIO_KG'] = df_agrupado['VOLUME_TOTAL'] / df_agrupado['POSITIVACAO_QTD']
    
    return df_agrupado

def calculate_top10_brands(df_raw):
    """
    Lista Top 10 Marcas em Faturamento e Volume
    """
    if df_raw.empty:
        return pd.DataFrame()
        
    df_marcas = df_raw.groupby('MARCA').agg(
        FATURAMENTO=('FATURAMENTO', 'sum'),
        VOLUME=('VOLUME_KG', 'sum')
    ).reset_index()
    
    # Ordenar por Faturamento
    df_top_10 = df_marcas.sort_values(by='FATURAMENTO', ascending=False).head(10)
    return df_top_10

if __name__ == "__main__":
    print("[*] Script de cálculo de KPIs pode ser importado via módulos.")
