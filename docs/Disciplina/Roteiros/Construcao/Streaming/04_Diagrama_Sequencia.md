# 16 - Diagrama de Sequência (Básico)

## Objetivo

Construir um diagrama de sequência para representar, de forma simples, a interação entre cliente, API e banco de dados no app Streaming.

## Cenário sugerido

Use o caso principal: **usuário autenticado publica um conteúdo**.

## Participantes

- Ator: Usuário
- Fronteira: Frontend Web
- Controle: API Django REST (`ContentViewSet`)
- Entidade: Modelo `Content`
- Persistência: Banco de Dados (SQLite/PostgreSQL)

## Passo a passo

1. Defina o início do fluxo no ator (Usuário clica em "Publicar").
2. Mostre a chamada HTTP do Frontend para a API (`POST /api/contents/`).
3. Represente a validação de autenticação (token/sessão).
4. Represente a validação de regras de negócio:
   - `description` obrigatória
   - `thumbnail_url` obrigatória
   - `title` único por criador
5. Mostre a persistência no banco (`INSERT` na tabela de conteúdos).
6. Finalize com o retorno da API:
   - Sucesso: `201 Created`
   - Falha: `400 Bad Request` ou `401 Unauthorized`

## Exemplo básico em PlantUML

```plantuml
@startuml
actor Usuario
participant "Frontend Web" as FE
participant "API Django REST" as API
participant "Validação (Serializer/Model)" as VAL
database "DB" as DB

Usuario -> FE: Preenche formulário e clica em Publicar
FE -> API: POST /api/contents/ (dados + token)
API -> API: Verifica autenticação

alt Não autenticado
    API --> FE: 401 Unauthorized
    FE --> Usuario: Exibe mensagem de login
else Autenticado
    API -> VAL: Validar campos e regras

    alt Dados inválidos
        VAL --> API: Erro de validação
        API --> FE: 400 Bad Request
        FE --> Usuario: Exibe erros do formulário
    else Dados válidos
        VAL --> API: OK
        API -> DB: INSERT Content
        DB --> API: Registro criado
        API --> FE: 201 Created + payload
        FE --> Usuario: Confirma publicação
    end
end
@enduml
```

## Entregável mínimo

- 1 diagrama de sequência contendo:
  - ator, frontend, API, validação e banco
  - fluxo principal de sucesso
  - ao menos 1 fluxo alternativo de erro

## Critérios de avaliação sugeridos

- Correção da ordem das mensagens
- Presença de validações e autenticação
- Clareza na separação entre sucesso e erro
- Consistência com endpoints já implementados no projeto

## Extensão opcional

Após concluir o fluxo de publicação, modele também:

- Consumo de conteúdo (`GET /api/contents/`)
- Criação de playlist com associação N:N
- Filtro de conteúdos por tipo (`audio`/`video`)
