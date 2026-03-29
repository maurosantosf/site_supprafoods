import os
import json
import zipfile

# Vamos criar um arquivo .pbit (Power BI Template) básico
# que já contenha a string ODBC e as DAX prontas. 
# O .pbit é um arquivo ZIP contendo o modelo (DataMashup e Model) em XML/JSON.

# Porém, gerar um PBIT/PBIX nativo do zero estrutural completo com M-Code e DAX
# via script reverso sem uma API oficial da Microsoft instalada é extremamente complexo
# porque exige compilar os hashes de segurança do Analysis Services.

# MAS, nós PODEMOS usar a nova feature do Power BI chamada "Power BI Project (PBIP)" 
# que permite salvar relatórios como pastas com arquivos JSON editáveis.

def create_pbip_project(base_path):
    project_name = "Dashboard_Comercial_Supra"
    project_dir = os.path.join(base_path, f"{project_name}.Report")
    dataset_dir = os.path.join(base_path, f"{project_name}.Dataset")
    
    os.makedirs(project_dir, exist_ok=True)
    os.makedirs(dataset_dir, exist_ok=True)
    
    # 1. Cria a configuração de projeto Dataset
    model_bim = {
      "name": "SemanticModel",
      "compatibilityLevel": 1550,
      "model": {
        "culture": "pt-BR",
        "dataAccessOptions": {
          "legacyRedirects": True,
          "returnErrorValuesAsNull": True
        },
        "defaultPowerBIDataSourceVersion": "powerBI_V3",
        "tables": [
          {
            "name": "fVendas",
            "partitions": [
              {
                "name": "fVendas",
                "mode": "import",
                "source": {
                  "type": "m",
                  "expression": [
                    "let",
                    "    Fonte = Odbc.Query(\"dsn=FS\", \"SELECT#(lf)    N.NUMPED,#(lf)    N.NUMNOTA,#(lf)    N.NUMTRANS,#(lf)    DECODE(N.POSICAO,#(lf)           'B', 'BLOQUEADO',#(lf)           'L', 'LIBERADO',#(lf)           'P', 'PENDENTE',#(lf)           'F', 'FATURADO',#(lf)           'C', 'CANCELADO') AS POSICAO,#(lf)    N.CODOPER,#(lf)    TIPO_DOC.DESCRICAO AS OPERACAO,#(lf)#(lf)    C.CODCLI,#(lf)    C.NOME,#(lf)    C.FANTASIA,#(lf)    C.BAIRRO,#(lf)#(lf)    N.DTEMISSAO,#(lf)    NVL(N.DTSAIDA, N.DTEMISSAO) AS DTSAIDA,#(lf)    N.CODVENDEDOR,#(lf)    FUNC.NOME AS VENDEDOR,#(lf)#(lf)    P.CODPROD,#(lf)    P.CODBARRA,                       -- código de barras padrão#(lf)    CEMB.CODBARRA AS \"\"Cod. Barra Emb.\"\",#(lf)    CEMB.DESCRICAO AS \"\"Descricao Emb.\"\",#(lf)#(lf)    P.DESCRICAO AS DESCRICAO_PRODUTO,#(lf)    P.UNIDADE,#(lf)    P.EMBALAGEM,#(lf)    P.CODMARCA,#(lf)    MARCA_PROD.MARCA AS MARCA,#(lf)    P.CODSEC,#(lf)    SECAO_PROD.DESCRICAO AS SECAO,#(lf)#(lf)    -- QUANTIDADE (AGORA SEM SINAL)#(lf)    ROUND(M.QT, 2) AS QT,#(lf)#(lf)    -- PREÇO UNITÁRIO#(lf)    ROUND(M.PUNIT, 2) AS PUNIT,#(lf)#(lf)    -- VALOR DO PRODUTO (AGORA SEM SINAL)#(lf)    ROUND(M.VLPROD, 2) AS VLPROD,#(lf)#(lf)    ROUND(NVL(NULLIF(M.CONF_PESO, 0), M.PESO_BRUTO), 4) AS PESO_BRUTO#(lf)#(lf)FROM#(lf)    MSCLIENTE C#(lf)    JOIN MSNF N           ON C.CODCLI    = N.CODCLI#(lf)    JOIN MSMOV M          ON N.NUMTRANS  = M.NUMTRANS#(lf)    JOIN MSPRODUTO P      ON M.CODPROD   = P.CODPROD#(lf)#(lf)    LEFT JOIN MSCODBARRA CEMB #(lf)           ON CEMB.CODPROD      = P.CODPROD#(lf)          AND CEMB.DTEXCLUSAO   IS NULL#(lf)#(lf)    LEFT JOIN MSTIPODOC TIPO_DOC #(lf)           ON TIPO_DOC.CODOPER  = N.CODOPER#(lf)    LEFT JOIN MSFUNC FUNC #(lf)           ON FUNC.MATRICULA    = N.CODVENDEDOR#(lf)    LEFT JOIN MSMARCA MARCA_PROD #(lf)           ON MARCA_PROD.CODMARCA = P.CODMARCA#(lf)    LEFT JOIN MSSECAO SECAO_PROD #(lf)           ON SECAO_PROD.CODSEC   = P.CODSEC#(lf)#(lf)WHERE#(lf)    M.DTCANCEL IS NULL#(lf)    AND N.CODOPER IN ('S', 'SM', 'EDS', 'EDF')#(lf)    AND N.DTSAIDA > TO_DATE('31/12/2023','DD/MM/YYYY')\")",
                    "in",
                    "    Fonte"
                  ]
                }
              }
            ],
            "measures": [
              {
                "name": "Faturamento Total",
                "expression": "SUM('fVendas'[VLPROD])",
                "formatString": "\"R$\"\\ #,0.00;-\"R$\"\\ #,0.00;\"R$\"\\ #,0.00"
              },
              {
                "name": "Volume Total (Kg)",
                "expression": "SUM('fVendas'[PESO_BRUTO])",
                "formatString": "#,0.00"
              },
              {
                "name": "Positivação",
                "expression": "DISTINCTCOUNT('fVendas'[NUMTRANS])",
                "formatString": "0"
              },
               {
                "name": "Ticket Médio Ticket (R$)",
                "expression": "DIVIDE([Faturamento Total], [Positivação], 0)",
                "formatString": "\"R$\"\\ #,0.00;-\"R$\"\\ #,0.00;\"R$\"\\ #,0.00"
              },
               {
                "name": "Mix por Transação (Kg)",
                "expression": "DIVIDE([Volume Total (Kg)], [Positivação], 0)",
                "formatString": "#,0.00"
              },
               {
                "name": "Preço Médio por Kg (R$/Kg)",
                "expression": "DIVIDE([Faturamento Total], [Volume Total (Kg)], 0)",
                 "formatString": "\"R$\"\\ #,0.00;-\"R$\"\\ #,0.00;\"R$\"\\ #,0.00"
              }
            ]
          }
        ]
      }
    }

    with open(os.path.join(dataset_dir, 'model.bim'), 'w', encoding='utf-8') as f:
        json.dump(model_bim, f, ensure_ascii=False, indent=2)

    definition_pbir = {
      "version": "1.0",
      "datasetReference": {
        "byPath": {
          "path": f"../{project_name}.Dataset"
        },
        "byConnection": None
      }
    }
    with open(os.path.join(project_dir, 'definition.pbir'), 'w', encoding='utf-8') as f:
         json.dump(definition_pbir, f, ensure_ascii=False, indent=2)

    pbip_file = os.path.join(base_path, f"{project_name}.pbip")
    pbip_content = {
      "version": "1.0",
      "artifacts": [
        {
          "report": {
            "path": f"{project_name}.Report"
          }
        }
      ],
      "settings": {
        "enableAutoRecovery": True
      }
    }
    with open(pbip_file, 'w', encoding='utf-8') as f:
        json.dump(pbip_content, f, ensure_ascii=False, indent=2)

    print(f"Projeto PBIP gerado em: {pbip_file}")
    print("Para abrir esse projeto, é necessário que o Power BI Desktop esteja configurado para suportar arquivos .pbip")
    
if __name__ == "__main__":
    base_dir = r"h:\My Drive\PROJETOS\DASHBOARD SUPPRA FOODS\POWER_BI"
    os.makedirs(base_dir, exist_ok=True)
    create_pbip_project(base_dir)
