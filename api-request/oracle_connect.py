import oracledb

# Dados da conexão
username = "SISFOSSA_ESR_SERVICE"
password = "HR50$Mko1#"
dsn = "10.9.9.181:1521/mat1prd"

# Conectar
try:
    print("Conectando ao banco de dados Oracle...")
    connection = oracledb.connect(user=username, password=password, dsn=dsn)
    print(connection)
except oracledb.DatabaseError as e:
    print(f"Erro ao conectar ao banco de dados Oracle: {e}")
    raise

# Criar cursor
#cursor = connection.cursor()

# Executar query
#cursor.execute("SELECT * FROM employees")

# Exibir resultados
#for row in cursor:
#    print(row)

# Fechar
#cursor.close()
#connection.close()
