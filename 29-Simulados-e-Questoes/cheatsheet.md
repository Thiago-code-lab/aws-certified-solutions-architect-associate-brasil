# Guia Rapido

## Tabela de decisao

| Sinal do enunciado | Melhor escolha | Evite | Armadilha comum |
|---|---|---|---|
| “Acesso minimo necessario” | IAM policy granular + role | User com permissao ampla | Confundir agilidade com permissao total |
| “Pico imprevisivel” | ASG + ALB + desacoplamento | Instancia unica vertical | Dimensionar para media e colapsar no pico |
| “Sem internet publica” | VPC Endpoint/PrivateLink | NAT para trafego interno AWS | Pagar mais e ampliar superficie de risco |
| “RPO baixo / RTO curto” | Multi-AZ ou warm standby conforme meta | Backup eventual sem teste | Escolher DR barato demais para meta agressiva |
| “Custo com uso previsivel” | Savings Plans/RI + rightsizing | On-Demand sem analise | Ignorar compromisso em carga estavel |

## Checklist de eliminacao rapida

1. A opcao viola requisito explicito de seguranca?
2. A opcao adiciona componentes sem necessidade?
3. A opcao aumenta operacao manual sem ganho tecnico?
4. Existe servico gerenciado que resolve com menor risco?

## Trincas que mais confundem no SAA-C03

- **SG vs NACL**: SG e stateful na ENI; NACL e stateless na subnet.
- **Multi-AZ vs Read Replica**: Multi-AZ = disponibilidade; replica = escala de leitura.
- **SQS vs SNS vs EventBridge**: fila duravel, pub/sub fan-out, roteamento por evento.

## Uso na reta final

- Revisar antes de cada mini-simulado.
- Marcar em qual linha da tabela voce errou a decisao.
- Atualizar o caderno de erros com a regra correta.
---

## ☁️ Acompanhe a CloudStudy

Estamos construindo uma plataforma para ajudar brasileiros a estudarem AWS de forma mais prática, organizada e acessível.

Siga a CloudStudy para acompanhar novos materiais, atualizações e conteúdos sobre certificações AWS:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> Quando quiser levar este tema para cenarios de dados, lakehouse e projetos hands-on, use como proximo passo: [Engenharia de Dados na AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).
