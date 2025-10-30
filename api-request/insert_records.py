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
    
def insert_records(conn, data):
    print("Inserindo dados de clima na tabela...")
    try:
        weather = data['current']
        location = data['location']
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO weather_schema.weather_data (
                city,
                temperature,
                weather_descriptions,
                wind_speed,
                time,
                inserted_at,
                utc_offset
            ) VALUES (%s, %s, %s, %s, %s, NOW(), %s)
        ''', (
            location['name'],
            weather['temperature'],
            weather['weather_descriptions'][0],
            weather['wind_speed'],
            location['localtime'],
            location['utc_offset']
        ))
        conn.commit()
        print("Dados inseridos com sucesso.")
    except psycopg2.Error as e:
        print(f"Erro ao inserir os dados: {e}")
        raise
                
def main():
    try:
        data = mock_fetch_weather_data()
        conn = connect_to_db()
        create_table(conn)
        insert_records(conn, data)
    except Exception as e:
        print(f"Erro no processo principal: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
            print("Conexão com o banco de dados fechada.")