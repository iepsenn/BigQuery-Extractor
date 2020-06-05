# BigQuery-Extractor

Extrator simples usando a [API fo Google BigQuery](https://cloud.google.com/bigquery/docs/reference/libraries#client-libraries-usage-python) para extrair as tabelas em formato csv.

# Arquivos

### config.yaml
Arquivo contendo uma lista com as informações das tabelas que devem ser extraídas, onde o formato é o seguinte:

```
tables_params:
   - [nome da tabela, nome do conjunto, nome do projeto, diretório que deve ser salvo]
```
### bq_extract.py
Código responsável por executar as extrações.

## Como executar
Uma variável de ambiente chamada `GOOGLE_APPLICATION_CREDENTIALS` deve conter o caminho para o arquivo contendo as credenciais do BigQuery, caso ainda não exista um valor para essa varíável é atribuido como valor padrão **./bq_credentials.json**.

Para extrair as tabelas basta executar o script principal.
