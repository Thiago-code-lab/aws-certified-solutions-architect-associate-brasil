# Questões de Revisão

## Questão 1

Uma aplicação web precisa continuar disponível durante falha de uma zona de disponibilidade. O tráfego deve ser distribuído automaticamente entre instâncias saudáveis. Qual abordagem é mais aderente?

A) Uma instância EC2 única com snapshot diário.
B) Auto Scaling Group em múltiplas AZs atrás de um Application Load Balancer.
C) Uma instância EC2 maior em uma subnet pública.
D) Backup manual da AMI antes de cada deploy.

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** B

**Explicação:**
ASG multi-AZ com ALB distribui tráfego para destinos saudáveis e mantém capacidade mesmo com falha em uma AZ.

**Por que a alternativa A está errada:**
Snapshot ajuda recuperação, mas não entrega alta disponibilidade durante a falha.

</details>

## Questão 2

Uma empresa quer reduzir custo de acesso ao S3 a partir de workloads privados em uma VPC, sem expor tráfego à internet. Qual escolha é mais indicada?

A) NAT Gateway para todo acesso ao S3.
B) Internet Gateway associado à subnet privada.
C) VPC Gateway Endpoint para S3.
D) Elastic IP em cada instância privada.

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** C

**Explicação:**
Gateway Endpoint para S3 mantém o tráfego na rede AWS e reduz dependência de NAT Gateway para esse acesso.

**Por que a alternativa A está errada:**
Funciona para saída, mas adiciona custo e não é a opção mais direta para S3 privado.

</details>

## Questão 3

Um banco relacional precisa de failover automático com mínima interrupção. O objetivo principal não é escalar leitura. Qual recurso atende melhor?

A) RDS Multi-AZ.
B) Read Replica em outra região.
C) Exportação para S3 a cada hora.
D) EC2 com banco instalado manualmente.

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:**
RDS Multi-AZ oferece alta disponibilidade com failover gerenciado para o banco principal.

**Por que a alternativa B está errada:**
Read Replica ajuda leitura e DR, mas não substitui Multi-AZ para failover síncrono gerenciado no mesmo escopo.

</details>

## Questão 4

Uma API recebe picos imprevisíveis e precisa desacoplar produtores e consumidores, aceitando processamento assíncrono. Qual serviço reduz melhor o risco operacional?

A) Amazon SQS.
B) Amazon EFS.
C) AWS WAF.
D) AWS Direct Connect.

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:**
SQS absorve picos, desacopla componentes e permite processamento assíncrono por consumidores em ritmos diferentes.

**Por que a alternativa B está errada:**
EFS é armazenamento de arquivos compartilhado, não uma fila de desacoplamento.

</details>

## Questão 5

Durante a revisão final, um estudante erra questões de IAM porque escolhe permissões amplas. Qual prática corrige melhor esse padrão?

A) Usar políticas administradas com permissões totais para evitar bloqueios.
B) Revisar menor privilégio, escopo de recursos e condições nas políticas.
C) Ignorar IAM e focar apenas em redes.
D) Decorar nomes de serviços sem analisar ações permitidas.

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** B

**Explicação:**
Questões de segurança no SAA-C03 frequentemente cobram menor privilégio, escopo correto e controle explícito de acesso.

**Por que a alternativa A está errada:**
Permissões amplas aumentam risco e normalmente contradizem requisitos de segurança da prova.

</details>
---

## ☁️ Acompanhe a CloudStudy

Estamos construindo uma plataforma para ajudar brasileiros a estudarem AWS de forma mais prática, organizada e acessível.

Siga a CloudStudy para acompanhar novos materiais, atualizações e conteúdos sobre certificações AWS:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> Quando quiser levar este tema para cenarios de dados, lakehouse e projetos hands-on, use como proximo passo: [Engenharia de Dados na AWS](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).
