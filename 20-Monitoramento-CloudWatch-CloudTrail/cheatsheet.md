# Guia Rapido

## Tabela de decisao

| Sinal do enunciado | Quando usar | Quando evitar | Armadilha de prova |
|---|---|---|---|
| Baixa operacao manual | Servico gerenciado com automacao nativa | Solucao autogerenciada sem necessidade | Confundir controle total com melhor custo total |
| Pico imprevisivel | Escala horizontal e desacoplamento | Capacidade fixa e ajuste manual | Dimensionar para media e falhar no pico |
| Requisito de seguranca forte | Menor privilegio + criptografia + auditoria | Permissao ampla por conveniencia | Achar que criptografia sozinha resolve governanca |
| Custo como restricao explicita | Escolha por perfil de consumo e acesso | Classe unica para todo dado | Reduzir custo sem validar impacto funcional |

## Sinais de servico

- **CloudWatch**: priorize quando o cenario precisa de integracao nativa e menor carga operacional.
- **CloudTrail**: use quando houver necessidade de elasticidade controlada e comportamento previsivel em pico.

## Quando usar este modulo na revisao

- Antes de simulados de arquitetura com foco em trade-offs.
- Quando houver erro recorrente de escolha entre duas alternativas parecidas.
- Na reta final para calibrar criterio de eliminacao de opcoes.

## Armadilhas recorrentes

- Resolver disponibilidade com recurso de performance.
- Trocar simplicidade por arquitetura superdimensionada.
- Ignorar observabilidade ao definir desenho final.
---

## ☁️ Acompanhe a CloudStudy

Estamos construindo uma plataforma para ajudar brasileiros a estudarem AWS de forma mais prática, organizada e acessível.

Siga a CloudStudy para acompanhar novos materiais, atualizações e conteúdos sobre certificações AWS:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> Este modulo tambem conversa com projetos de dados na nuvem; para praticar esse lado, veja a trilha complementar: [Engenharia de Dados na AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).
