python3.11 -m venv virt.env
source virt.env/bin/activate

pip freeze requirements.txt

brew services start mysql@8.0
sudo mysql

# CREATE DATABASE my_database;
# CREATE USER my_user@localhost IDENTIFIED BY 'password';
# GRANT ALL PRIVILEGES ON my_database.* TO my_user@localhost;
# GRANT ALL PRIVILEGES ON chatbot_project.* TO ninjavr2@localhost;

