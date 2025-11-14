import oracledb

host = "oracle1.casan.com.br"          # DNS ou IP
port = 1521                # ou a porta real
service_name = "mat1prd"  # ex.: orclpdb1, meu_db.empresa.local

# dsn = f"{host}:{port}/{service_name}"  # TCP
# Para TCPS (TLS):
dsn = f"tcps://{host}:{port}/?service_name={service_name}&ssl_server_dn_match=yes"

connection = oracledb.connect(
    user="SISFOSSA_ESR_SERVICE",
    password="HR50$Mko1#",
    dsn=dsn
)