REM @echo This is where you need to store all the CSV files before next steps: (It's an upload path to MySql)
REM mysqlsh -u root -p --sql -e "SHOW VARIABLES LIKE 'secure_file_priv'"

mysqlsh -u root -p --sql -e "DROP DATABASE gloat;"

mysqlsh -u root -p --sql -e "CREATE DATABASE gloat;"

python manage.py makemigrations
python manage.py migrate

mysqlsh -u root -p --sql -f "init_db.sql"