# Mini Simulados por Dominio

## Como usar

- 4 blocos de 5 questoes (20 no total).
- Tempo alvo: 8 a 10 minutos por bloco.
- Corrija na hora e registre o erro no caderno.

## Bloco A: Resiliencia

1. Cenario exige failover automatico entre zonas com minimo downtime.
A) Instancia unica maior. B) Multi-AZ com monitoramento e failover nativo. C) Backup semanal manual. D) Escala vertical apenas.

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** B

**Explicação:** Multi-AZ trata falha de AZ com troca automatica e menor indisponibilidade.

</details>

2. Aplicacao com pico imprevisivel precisa absorver carga sem perder requisicoes.
A) Fila desacoplada + consumidores elasticos. B) Processamento sincrono fixo. C) Retry manual no cliente. D) Bloquear requisicoes extras.

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:** Fila protege o produtor e permite escalar consumidores conforme backlog.

</details>

3. Requisito de DR com RPO baixo e custo moderado.
A) Backup anual. B) Pilot light. C) Sem replicacao. D) Apenas snapshots locais.

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** B

**Explicação:** Pilot light equilibra custo com recuperacao mais rapida que backup puro.

</details>

4. Alta disponibilidade de banco relacional transacional.
A) Read replica apenas. B) Multi-AZ. C) Cache local. D) Instancia Spot.

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** B

**Explicação:** Multi-AZ prioriza continuidade de escrita com failover gerenciado.

</details>

5. Distribuicao global de conteudo estatico com baixa latencia.
A) CloudFront. B) EC2 unica regiao. C) NAT Gateway. D) SQS.

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:** CloudFront entrega conteudo no edge e reduz latencia por distancia.

</details>

## Bloco B: Performance

6. Leitura massiva e repetitiva em dados quentes de sessao.
A) Cache gerenciado. B) Snapshot diario. C) Log manual. D) ASG sem cache.

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:** Cache in-memory reduz latencia e alivia o banco de dados.

</details>

7. API com throughput variavel e baixa operacao.
A) Serverless com escala automatica. B) EC2 fixa. C) Processo cron. D) Monolito sem balanceador.

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:** Serverless ajusta capacidade por demanda sem gerenciamento de servidor.

</details>

8. DynamoDB com leitura irregular e picos.
A) Capacity mode sob demanda. B) Provisionado estatico sem autoscaling. C) Banco local. D) Planilha CSV.

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:** On-demand absorve variacao e evita throttling por subprovisionamento.

</details>

9. Consulta analitica sobre dados em S3 sem cluster dedicado.
A) Athena. B) NAT Gateway. C) IAM Identity Center. D) Route 53.

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:** Athena executa SQL direto no S3 sem infraestrutura para gerenciar.

</details>

10. Conectividade privada a servico AWS sem sair para internet.
A) VPC Endpoint. B) NAT publico. C) Bastion obrigatorio. D) VPN on-prem para tudo.

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:** Endpoint privado evita internet publica e reduz superficie de ataque.

</details>

## Bloco C: Seguranca

11. Credencial de aplicacao com rotacao automatica.
A) Secrets Manager. B) Arquivo texto em EC2. C) Variavel fixa em pipeline. D) KMS sozinho.

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:** Secrets Manager gerencia armazenamento, acesso e rotacao de segredo.

</details>

12. Menor privilegio em IAM significa:
A) Politica ampla para simplificar. B) Permissao minima necessaria por funcao. C) Mesmo role para tudo. D) Sem logs.

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** B

**Explicação:** Least privilege reduz impacto de credencial comprometida.

</details>

13. Necessidade de trilha de auditoria de API calls.
A) CloudTrail. B) CloudFront. C) EFS. D) Snowball.

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:** CloudTrail registra chamadas API para investigacao e compliance.

</details>

14. Criptografia de dados em repouso com chave controlada.
A) KMS com CMK. B) SG inbound. C) ASG policy. D) IAM group.

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:** KMS com CMK oferece governanca de chave e auditoria de uso.

</details>

15. Segmentar trafego entre camadas na VPC.
A) Security Groups e NACLs por funcao. B) Tudo em subnet publica. C) Porta 0.0.0.0/0. D) Um unico SG amplo.

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:** Segmentacao por camada diminui blast radius e risco lateral.

</details>

## Bloco D: Custo

16. Dado raramente acessado, retencao longa.
A) Classe de arquivamento adequada. B) Standard para tudo. C) EBS io2 para backup frio. D) Replicar sem necessidade.

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:** Glacier/Archive reduz custo quando acesso e esporadico.

</details>

17. Carga previsivel 24x7 com EC2.
A) Compromisso de uso (Savings Plans/RI). B) Spot para banco critico unico. C) On-Demand sem analise. D) Escala manual diaria.

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:** Consumo estavel costuma se beneficiar de desconto por compromisso.

</details>

18. Lambda com execucao curta e esporadica para reduzir custo operacional.
A) Bom encaixe serverless. B) ECS permanente obrigatorio. C) Cluster dedicado fixo. D) Banco como fila.

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:** Pagar por invocacao evita custo fixo ocioso para carga eventual.

</details>

19. Evitar custo de transferencia indevida para servicos AWS internos.
A) Endpoints privados quando aplicavel. B) NAT para tudo. C) Tunnel manual. D) S3 publico.

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:** Endpoint privado remove salto desnecessario pela internet/NAT.

</details>

20. Processo de revisao de custo continuo.
A) Budgets + alertas + revisao mensal. B) Ver fatura so no fim do ano. C) Ignorar tags. D) Sem ownership.

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:** Governanca de custo exige monitoramento proativo e accountability.

</details>
---

## ☁️ Acompanhe a CloudStudy

Estamos construindo uma plataforma para ajudar brasileiros a estudarem AWS de forma mais prática, organizada e acessível.

Siga a CloudStudy para acompanhar novos materiais, atualizações e conteúdos sobre certificações AWS:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> Para transformar esta base de arquitetura em pratica com pipelines, dados e analytics, voce tambem pode seguir a trilha complementar: [Engenharia de Dados na AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).
