# Lab Guiado

## Objetivo

Montar um fluxo minimo funcional que demonstre **Decisoes de arquitetura guiadas por pilares AWS**, com validacao clara de comportamento e custo controlado para ambiente de estudo.

## Servicos usados

Well-Architected Tool, Trusted Advisor, CloudWatch.

## Faixa de custo esperada

- Ambiente de estudo curto: baixo custo se executado por poucas horas.
- Evite manter recursos ativos apos validacao.
- Priorize camada gratuita quando disponivel.

## Passo a passo

1. Crie os recursos essenciais do fluxo em uma conta de laboratorio.
2. Configure politicas minimas de acesso e observabilidade basica.
3. Execute carga de teste pequena para validar resposta funcional.
4. Simule uma falha simples (interrupcao de componente) e observe recuperacao.
5. Registre metrica-chave e ajuste uma configuracao para comparar resultado.

## Validacao

- Fluxo de ponta a ponta executa sem erro critico.
- Logs/metricas mostram comportamento esperado.
- Existe evidencia de decisao entre desempenho e custo.

## Cleanup

1. Remova recursos criados no laboratorio.
2. Apague dados temporarios e snapshots nao necessarios.
3. Revise faturamento no dia seguinte para confirmar encerramento.

## Takeaway para prova

O ponto principal e identificar qual servico reduz risco operacional mantendo aderencia ao requisito central do cenario.
---

## ☁️ Acompanhe a CloudStudy

Estamos construindo uma plataforma para ajudar brasileiros a estudarem AWS de forma mais prática, organizada e acessível.

Siga a CloudStudy para acompanhar novos materiais, atualizações e conteúdos sobre certificações AWS:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> Quando quiser levar este tema para cenarios de dados, lakehouse e projetos hands-on, use como proximo passo: [Engenharia de Dados na AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).
