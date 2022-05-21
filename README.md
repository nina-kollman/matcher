# Gloat Matcher

This repo implement two different end points in django using the MySql db.

<ol>
  <li>job/ - Search candidates according to perfect job title match with max skill match.</li>
  <li>partial/ - Search candidates according to partial job title match.</li>
</ol>

## How to install the project

- First download the project from the repo.

- Open the gloat_matcher/settings.py and modify the DATABASES section to you relevant database to use.
- Run the find_uploads.bat file in order to find the MySql uploads directory path. Move all the csv files to the presented directory.
  The csv files are located in the data directory.
- Change the init.bat file as follows:
  ```bash
  $ mysqlsh -u <db_user_name> -p --sql -e "DROP DATABASE <DB_name>;"
  $ mysqlsh -u <db_user_name> -p --sql -e "CREATE DATABASE <DB_name>;"
  ```
- Run the init.bat file. This will make migrations and load the csv data to the database.
- Now the project is ready to go! Run the command:
  ```bash
  $ python manage.py runserver
  ```
- open the given server url with the desired endpoint and start playing!
  ```bash
    http://127.0.0.1:8000/job/
    http://127.0.0.1:8000/partial/
  ```

## Let's Play

<img src='docs/hello_matcher.jpg' style="width:300px" />

### Search 'Software developer' by title in 'job/' endpoint:

<img src='docs/software_developer.jpg' style="width:300px" />

<img src='docs/software_developer2.jpg' style="width:300px" />

### Search 'Software developer' with partial matching in 'partial/' endpoint:

<img src='docs/partial.jpg' style="width:300px" />
