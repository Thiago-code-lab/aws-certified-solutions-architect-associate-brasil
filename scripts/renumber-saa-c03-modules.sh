#!/usr/bin/env bash
set -euo pipefail

# Historical migration utility: legacy Portuguese identifiers intentionally remain
# as input names. Targets use the English 01..31 curriculum. Existing English
# directories are left in place. Run from the repository root or pass its path.
BASE_DIR="${1:-.}"
cd -- "$BASE_DIR"

declare -a MAP=(
  "01-Introducao-SAA-C03|01-Introduction-SAA-C03"
  "02-IAM-e-Seguranca|02-IAM-and-Security"
  "09-IAM-e-Seguranca|03-IAM-and-Security-Labs"
  "03-Computacao-EC2|04-EC2-Compute"
  "04-Alta-Disponibilidade-e-Escalabilidade|05-High-Availability-and-Scalability"
  "05-Amazon-S3-e-Armazenamento|06-Amazon-S3-and-Storage"
  "08-S3-Avancado|07-Advanced-S3-Labs"
  "07-VPC-e-Redes|08-VPC-and-Networking"
  "05-VPC-e-Redes|09-VPC-and-Networking-Labs"
  "06-Banco-de-Dados|10-Databases"
  "06-RDS-e-Bancos-Relacionais|11-RDS-and-Relational-Databases-Labs"
  "07-DynamoDB|12-DynamoDB"
  "08-DNS-Route53-e-CloudFront|13-DNS-Route53-and-CloudFront"
  "09-Desacoplamento-SQS-SNS-EventBridge|14-Decoupling-SQS-SNS-EventBridge"
  "10-SQS-SNS-Mensageria|15-SQS-SNS-Messaging-Labs"
  "10-Containers-ECS-EKS-Fargate|16-Containers-ECS-EKS-Fargate"
  "11-Serverless-Lambda-API-Gateway|17-Serverless-Lambda-API-Gateway"
  "12-Dados-e-Analytics|18-Data-and-Analytics"
  "13-Machine-Learning-e-IA|19-Machine-Learning-and-AI"
  "14-Monitoramento-CloudWatch-CloudTrail|20-Monitoring-CloudWatch-CloudTrail"
  "15-Migracao-e-Transferencia|21-Migration-and-Transfer"
  "16-Well-Architected-Framework|26-Well-Architected-Framework"
  "17-Casos-de-Uso-Reais|27-Real-World-Use-Cases"
  "18-Labs-Praticos|28-Hands-on-Labs"
  "19-Simulados-e-Questoes|29-Practice-Exams-and-Questions"
  "20-Glossario|30-Glossary"
  "21-Recursos-e-Links|31-Resources-and-Links"
  "03-IAM-e-Seguranca-Labs|03-IAM-and-Security-Labs"
  "04-Computacao-EC2|04-EC2-Compute"
  "05-Alta-Disponibilidade-e-Escalabilidade|05-High-Availability-and-Scalability"
  "06-Amazon-S3-e-Armazenamento|06-Amazon-S3-and-Storage"
  "07-S3-Avancado-Labs|07-Advanced-S3-Labs"
  "08-VPC-e-Redes|08-VPC-and-Networking"
  "09-VPC-e-Redes-Labs|09-VPC-and-Networking-Labs"
  "10-Banco-de-Dados|10-Databases"
  "11-RDS-e-Bancos-Relacionais-Labs|11-RDS-and-Relational-Databases-Labs"
  "13-DNS-Route53-e-CloudFront|13-DNS-Route53-and-CloudFront"
  "14-Desacoplamento-SQS-SNS-EventBridge|14-Decoupling-SQS-SNS-EventBridge"
  "15-SQS-SNS-Mensageria-Labs|15-SQS-SNS-Messaging-Labs"
  "18-Dados-e-Analytics|18-Data-and-Analytics"
  "19-Machine-Learning-e-IA|19-Machine-Learning-and-AI"
  "20-Monitoramento-CloudWatch-CloudTrail|20-Monitoring-CloudWatch-CloudTrail"
  "21-Migracao-e-Transferencia|21-Migration-and-Transfer"
  "22-Recuperacao-de-Desastres-e-Continuidade|22-Disaster-Recovery-and-Business-Continuity"
  "23-AWS-Organizations-Governanca-e-Custos|23-AWS-Organizations-Governance-and-Costs"
  "24-Redes-Avancadas-e-Conectividade-Hibrida|24-Advanced-Networking-and-Hybrid-Connectivity"
  "25-Criptografia-KMS-e-Gestao-de-Segredos|25-Encryption-KMS-and-Secrets-Management"
  "27-Casos-de-Uso-Reais|27-Real-World-Use-Cases"
  "28-Labs-Praticos|28-Hands-on-Labs"
  "29-Simulados-e-Questoes|29-Practice-Exams-and-Questions"
  "30-Glossario|30-Glossary"
  "31-Recursos-e-Links|31-Resources-and-Links"
)
declare -a SOURCES=() TARGETS=() TEMPORARIES=()
declare -A SEEN_TARGETS=()

fail() { printf 'Error: %s\n' "$1" >&2; exit 1; }

preflight() {
  local pair src dst tmp
  for pair in "${MAP[@]}"; do
    src="${pair%%|*}"
    dst="${pair##*|}"
    [[ -d "$src" ]] || continue
    tmp="__tmp__${dst}"
    [[ ! -e "$dst" ]] || fail "Destination already exists: $dst"
    [[ ! -e "$tmp" ]] || fail "Temporary path already exists: $tmp"
    [[ -z "${SEEN_TARGETS[$dst]:-}" ]] || fail "Multiple sources map to: $dst"
    SEEN_TARGETS[$dst]=1
    SOURCES+=("$src")
    TARGETS+=("$dst")
    TEMPORARIES+=("$tmp")
  done
}

preflight
printf '[1/2] Moving %s source directories to temporary names...\n' "${#SOURCES[@]}"
for i in "${!SOURCES[@]}"; do
  mv -- "${SOURCES[$i]}" "${TEMPORARIES[$i]}"
  printf '  %s -> %s\n' "${SOURCES[$i]}" "${TEMPORARIES[$i]}"
done

printf '[2/2] Applying final English directory names...\n'
for i in "${!TARGETS[@]}"; do
  mv -- "${TEMPORARIES[$i]}" "${TARGETS[$i]}"
  printf '  %s -> %s\n' "${TEMPORARIES[$i]}" "${TARGETS[$i]}"
done
printf 'Done. Existing destination directories were never overwritten.\n'
