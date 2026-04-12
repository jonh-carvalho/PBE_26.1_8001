# Brainstorm Inicial - Projeto de Estágio

## Tema
Validação automática do relatório final de estágio na aplicação web de gestão de estágio.

## Problema que queremos resolver
- Revisão manual demora e gera fila de aprovação.
- Erros simples (campos faltando e formatação) chegam para análise humana.
- Falta de padronização dificulta comparar relatórios.

## Objetivo do brainstorm
- Levantar ideias de funcionalidades, regras e fluxo.
- Identificar riscos e dúvidas antes da implementação.
- Definir um MVP realista para as primeiras iterações.

## Ideias de funcionalidades
- Checklist automático de campos obrigatórios do relatório.
- Validação de estrutura mínima: capa, introdução, atividades, resultados, conclusão.
- Verificação de tamanho mínimo/máximo por seção.
- Regras de formatação: fonte, espaçamento, margens, paginação, referências.
- Validação de anexos obrigatórios (termo, assinatura, comprovantes).
- Pontuação por critérios (completude, conformidade, clareza).
- Feedback detalhado por seção com sugestões de correção.
- Reenvio de versão corrigida com histórico de alterações.
- Painel para coordenador com status: aprovado, pendente, rejeitado com ajuste.
- Configuração de regras por curso ou turma.

## Ideias técnicas
- Pipeline de validação em etapas: sintática, estrutural e semântica.
- Motor de regras configurável (JSON/YAML ou tela administrativa).
- Processamento assíncrono para arquivos maiores (fila + worker).
- Logs de validação para auditoria e rastreabilidade.
- API para integração com módulo de relatórios já existente.
- Geração de relatório de validação em PDF para registro.

## Fluxo sugerido do usuário
1. Estagiário envia o relatório final.
2. Sistema faz validações automáticas e gera feedback imediato.
3. Se houver erro bloqueante, estagiário corrige e reenvia.
4. Se aprovado automaticamente, vai para revisão final do coordenador.
5. Coordenador confirma aprovação ou solicita ajuste pontual.

## Critérios iniciais de validação (exemplos)
- Campos obrigatórios preenchidos: nome, matrícula, empresa, período, orientador.
- Documento no formato permitido (PDF/DOCX) e tamanho limite.
- Presença das seções obrigatórias no texto.
- Mínimo de páginas e/ou palavras definido pela coordenação.
- Referências bibliográficas em padrão definido pelo curso.

## Riscos e desafios
- Falsos positivos ou negativos na análise automática.
- Diferença de padrão entre cursos e orientadores.
- Custo de processamento de arquivos grandes.
- Resistência de usuários se o feedback não for claro.
- Dependência de OCR quando houver anexos digitalizados.

## Perguntas abertas
- Quais regras são realmente bloqueantes e quais são apenas alertas?
- O coordenador pode sobrescrever uma reprovação automática?
- Como versionar regras sem quebrar relatórios já enviados?
- Quais formatos de arquivo serão suportados no MVP?
- Qual prazo de processamento aceitável por relatório?

## MVP proposto (primeira entrega)
- Validação de campos obrigatórios.
- Verificação de formato e tamanho de arquivo.
- Checagem de seções mínimas no relatório.
- Feedback objetivo de erros e status final.
- Painel simples para coordenador visualizar pendências.

## Métricas de sucesso
- Redução do tempo médio de análise inicial.
- Percentual de relatórios aprovados sem retrabalho manual.
- Tempo médio entre submissão e resposta automática.
- Taxa de reenvio por erro de formatação.
- Satisfação de estagiários e coordenadores.

## Próximos passos
1. Validar com coordenadores as regras prioritárias.
2. Definir modelo de dados para regras e resultados de validação.
3. Prototipar tela de feedback para o estagiário.
4. Implementar MVP e medir métricas da primeira turma.
