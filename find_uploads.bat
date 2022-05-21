@echo This is where you need to store all the CSV files before next steps: (It's an upload path to MySql)
mysqlsh -u root -p --sql -e "SHOW VARIABLES LIKE 'secure_file_priv'"
