import subprocess
import time

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
    sql_query = "INSERT INTO test_table (id, name) VALUES (1, 'TestUser');"
    mysql_command = f"docker exec {wordpress_db_container[1:-1]} mysql -u root -pwordpress -D wordpress -e \"{sql_query}\""
    print("Inserting data into Wordpress database...")
    run_command(mysql_command)
    
if sql_container:
    sql_insert_command = f"docker exec {sql_container[1:-1]} psql -U user -d mydatabase -c \"INSERT INTO users (id, name) VALUES (1, 'SQLUser');\""
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