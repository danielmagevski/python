import boto3
import sys
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def check_open_ports_for_cidr(ports, cidr="0.0.0.0/0"):
    try:
        # Obtém a região e a ID da conta
        session = boto3.session.Session()
        region = session.region_name
        sts_client = boto3.client('sts')
        account_id = sts_client.get_caller_identity()['Account']

        print(f"Região: {region}")
        print(f"Conta: {account_id}")
        print("-" * 50)

        # Cria um cliente EC2
        ec2_client = boto3.client('ec2')

        # Lista os Security Groups
        response = ec2_client.describe_security_groups()

        # Verifica se ha Security Groups
        security_groups = response.get('SecurityGroups', [])

        if not security_groups:
            print("Nenhum Security Group encontrado.")
            return

        # Verifica cada porta
        for port in ports:
            port_found = False
            for sg in security_groups:
                for rule in sg.get('IpPermissions', []):
                    port_from = rule.get('FromPort', None)
                    port_to = rule.get('ToPort', None)
                    ip_ranges = rule.get('IpRanges', [])

                    # Verifica se a porta e o CIDR estão na regra
                    if port_from is not None and port_to is not None and port_from <= port <= port_to:
                        for ip_range in ip_ranges:
                            if ip_range.get('CidrIp') == cidr:
                                port_found = True
                                print(f"A porta {port} está aberta para entrada no CIDR {cidr}.")
                                print(f"Security Group ID: {sg['GroupId']}")
                                print(f"Nome do Security Group: {sg.get('GroupName', 'N/A')}")
                                print("-" * 50)
                                break
                    if port_found:
                        break
                if port_found:
                    break

            # Resultado para a porta caso nenhuma regra seja encontrada
            if not port_found:
                print(f"Nenhuma regra de entrada encontrada para a porta {port} no CIDR {cidr}.")

    except NoCredentialsError:
        print("Erro: Credenciais da AWS não encontradas.")
    except PartialCredentialsError:
        print("Erro: Credenciais da AWS incompletas.")
    except Exception as e:
        print(f"Erro ao verificar portas abertas: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python script.py <porta1> <porta2> ...")
        sys.exit(1)
    
    # Obtém as portas passadas como argumentos
    ports = list(map(int, sys.argv[1:]))
    check_open_ports_for_cidr(ports)
