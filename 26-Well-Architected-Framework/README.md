# Well Architected Framework

## Visao Geral

Este modulo cobre **Decisoes de arquitetura guiadas por pilares AWS** com foco no tipo de decisao que aparece no SAA-C03. A ideia central e transformar requisitos de negocio em escolhas tecnicas objetivas, equilibrando resiliencia, desempenho, seguranca e custo. Em prova, o diferencial nao e decorar servico isolado: e identificar qual restricao do cenario pesa mais e escolher o padrao que reduz risco operacional.

## Conceitos-Chave

- Papel dos servicos: Well-Architected Tool, Trusted Advisor, CloudWatch.
- Priorizacao por requisito dominante (latencia, disponibilidade, conformidade ou custo).
- Integracao entre servicos com desacoplamento e observabilidade minima.
- Escolha de arquitetura com menor complexidade viavel para o contexto.

## Relevancia para o Exame

No SAA-C03, este dominio costuma aparecer em perguntas com duas alternativas tecnicamente possiveis. O desempate normalmente vem de detalhes como: modelo de consistencia, estrategia de failover, custo de operacao recorrente, impacto de throughput e nivel de automacao exigido. Por isso, estudar este modulo significa treinar criterio de escolha, nao apenas nomenclatura.

## Sinais Praticos (3 a 5)

1. Quando o enunciado pede resposta elastica com pouca operacao manual, privilegie servicos gerenciados.
2. Quando houver dependencia entre componentes, valide se existe desacoplamento para absorver pico e falha parcial.
3. Quando houver restricao de seguranca, confirme criptografia em transito/repouso e menor privilegio.
4. Se o custo for parte do requisito, compare classes de consumo, modo de capacidade e padrao de acesso.
5. Se o cenario for global, valide rota de trafego, latencia e estrategia de distribuicao.

## Armadilhas Comuns

- Escolher recurso premium sem necessidade real do cenario.
- Confundir recurso de alta disponibilidade com recurso de escala de leitura.
- Ignorar limites de servico e comportamento em falha.
- Resolver requisito de seguranca com ferramenta inadequada para ciclo de vida do segredo.

## Proximo Passo de Revisao

1. Revise o cheatsheet.md para consolidar sinais de decisao.
2. Resolva questoes.md sem consulta para testar julgamento tecnico.
3. Use flashcards.md em revisao curta diaria para fixar diferencas criticas.

## Estudos Complementares

Para reforco de fundamentos AWS antes de aprofundar cenarios arquiteturais:
https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil

Para conectar arquitetura com IA generativa e Bedrock em trilha complementar:
https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil
---

## ☁️ Acompanhe a CloudStudy

Estamos construindo uma plataforma para ajudar brasileiros a estudarem AWS de forma mais prática, organizada e acessível.

Siga a CloudStudy para acompanhar novos materiais, atualizações e conteúdos sobre certificações AWS:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> Para consolidar arquitetura com projetos reais de dados na AWS, mantenha no radar a trilha complementar: [Engenharia de Dados na AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).
