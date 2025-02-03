import subprocess
import time

"""Apart from MongoDB, the other databases worked successfully. I have tried to create database with db.create_collection
query but it still gave an error."""

create_database_query = """
CREATE DATABASE IF NOT EXISTS wordpress;
"""

create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);
"""

insert_data_query = """
INSERT INTO users (id, name) 
VALUES (1, 'SQLUser');
"""

def run_command(command):
    
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if process.returncode == 0:
        return process.stdout.strip()
    else:
        print(f"Error running command: {command}\n{process.stderr}")
        return None
    
print("Starting Wordpress environment...")
run_command("docker-compose -f ../Wordpress/docker-compose.yml up -d")

print("Starting SQL environment...")
run_command("docker-compose -f ../SQL/docker-compose.yml up -d")

time.sleep(10)

wordpress_db_container = run_command("docker ps --filter name=wordpress-db-1 --format '{{.ID}}'")
sql_container = run_command("docker ps --filter name=my_postgres --format '{{.ID}}'")
nosql_container = run_command("docker ps --filter name=my_mongo --format '{{.ID}}'")
inmemory_container = run_command("docker ps --filter name=my_redis --format '{{.ID}}'")

print(f"WordPress container ID: {wordpress_db_container[1:-1]}")
print(f"SQL container ID: {sql_container[1:-1]}")
print(f"NoSQL container ID: {nosql_container[1:-1]}")
print(f"In-memory container ID: {inmemory_container[1:-1]}")

time.sleep(10)

if wordpress_db_container:
    mysql_create__database_command = f"docker exec {wordpress_db_container[1:-1]} mysql -u root -pwordpress -e \"{create_database_query}\""
    run_command(mysql_create__database_command)
    mysql_insert_command = f"docker exec {wordpress_db_container[1:-1]} mysql -u root -pwordpress -D wordpress -e \"{insert_data_query}\""
    print("Inserting data into Wordpress database...")
    run_command(mysql_insert_command)
    
if sql_container:
    sql_create_command = f"docker exec {sql_container[1:-1]} psql -U user -d mydatabase -c \"{create_table_query}\""
    run_command(sql_create_command)
    sql_insert_command = f"docker exec {sql_container[1:-1]} psql -U user -d mydatabase -c \"{insert_data_query}\""
    print("Inserting data into SQL database...")
    run_command(sql_insert_command)
    
if nosql_container:
    mongo_insert_command = f"docker exec {nosql_container[1:-1]} mongo:7 mongo mydatabase -u root -p password --eval \"db.users.insertOne({{id: 1, name: 'NoSQLUser'}});\""
    print("Inserting data into NoSQL database...")
    run_command(mongo_insert_command)
    
if inmemory_container:
    redis_insert_command = f"docker exec {inmemory_container[1:-1]} redis-cli SET user:1 'InMemoryUser'"
    print("Inserting data into In-Memory database...")
    run_command(redis_insert_command)

print("All tasks completed.")