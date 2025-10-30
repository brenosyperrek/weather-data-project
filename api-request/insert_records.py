import psycopg2
from api_request import mock_fetch_weather_data

def connect_to_db():
    print ("Conectando ao banco de dados PostgreSQL...")
    try:
        conn = psycopg2.connect(
            host='localhost',
            port='5000',  
            dbname='weather_db',
            user='db_user',
            password='db_password'
        )
        return conn
    except psycopg2.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        raise
    
def create_table(conn):
    print("Criando tabela de clima se não existir...")
    create_table_query = '''
    CREATE SCHEMA IF NOT EXISTS weather_schema;
    CREATE TABLE IF NOT EXISTS weather_schema.weather_data (
        id SERIAL PRIMARY KEY,
        city TEXT,
        temperature FLOAT,
        weather_descriptions TEXT,
        wind_speed FLOAT,
        time TIMESTAMP,
        inserted_at TIMESTAMP DEFAULT NOW(),
        utc_offset TEXT
    );
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        conn.commit()
        print("Tabela criada ou já existente.")
    except psycopg2.Error as e:
        print(f"Erro ao criar a tabela: {e}")
        raise
    
conn = connect_to_db()
create_table(conn)