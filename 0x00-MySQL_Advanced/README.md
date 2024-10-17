# 0x00. MySQL advanced

### Comments for your SQL file:
```sh

$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;

```

### How to import a SQL dump
```sh

$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller

```

## Tasks
0. We are all unique! 
Write a SQL script that creates a table `users` following these requirements:

- With these attributes:
    - `id`, integer, never null, auto increment and primary key
    - `email`, string (255 characters), never null and unique
    - `name`, string (255 characters)
- If the table already exists, your script should not fail
- Your script can be executed on any database

Context: Make an attribute unique directly in the table schema will enforced your business rules and avoid bugs in your application
```sh

stevecmd@stevecmd-HP-ENVY-15-Notebook-PC:/media/stevecmd/48444E06444DF6EA/ALX/Specialization/Backend/alx-backend-storage$ service mysql start
stevecmd@stevecmd-HP-ENVY-15-Notebook-PC:/media/stevecmd/48444E06444DF6EA/ALX/Specialization/Backend/alx-backend-storage$ service mysql status
● mysql.service - MySQL Community Server
     Loaded: loaded (/lib/systemd/system/mysql.service; enabled; vendor preset: enabled)
     Active: active (running) since Thu 2024-10-17 07:08:39 EAT; 7h ago
   Main PID: 1967 (mysqld)
     Status: "Server is operational"
      Tasks: 37 (limit: 9345)
     Memory: 390.9M
        CPU: 4min 1.633s
     CGroup: /system.slice/mysql.service
             └─1967 /usr/sbin/mysqld

Okt 17 07:07:30 stevecmd-HP-ENVY-15-Notebook-PC systemd[1]: Starting MySQL Community Server...
Okt 17 07:08:39 stevecmd-HP-ENVY-15-Notebook-PC systemd[1]: Started MySQL Community Server.
stevecmd@stevecmd-HP-ENVY-15-Notebook-PC:/media/stevecmd/48444E06444DF6EA/ALX/Specialization/Backend/alx-backend-storage$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
stevecmd@stevecmd-HP-ENVY-15-Notebook-PC:/media/stevecmd/48444E06444DF6EA/ALX/Specialization/Backend/alx-backend-storage$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
stevecmd@stevecmd-HP-ENVY-15-Notebook-PC:/media/stevecmd/48444E06444DF6EA/ALX/Specialization/Backend/alx-backend-storage$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id      name
1       Drama
2       Mystery
3       Adventure
4       Fantasy
5       Comedy
6       Crime
7       Suspense
8       Thriller

stevecmd@stevecmd-HP-ENVY-15-Notebook-PC:/media/stevecmd/48444E06444DF6EA/ALX/Specialization/Backend/alx-backend-storage/0x00-MySQL_Advanced$ echo "CREATE DATABASE holberton;" | mysql -uroot -p
Enter password: 
stevecmd@stevecmd-HP-ENVY-15-Notebook-PC:/media/stevecmd/48444E06444DF6EA/ALX/Specialization/Backend/alx-backend-storage/0x00-MySQL_Advanced$ cat 0-uniq_users.sql | mysql -uroot -p holberton
Enter password: 
stevecmd@stevecmd-HP-ENVY-15-Notebook-PC:/media/stevecmd/48444E06444DF6EA/ALX/Specialization/Backend/alx-backend-storage/0x00-MySQL_Advanced$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");' | mysql -uroot -p holberton
Enter password: 
stevecmd@stevecmd-HP-ENVY-15-Notebook-PC:/media/stevecmd/48444E06444DF6EA/ALX/Specialization/Backend/alx-backend-storage/0x00-MySQL_Advanced$ echo 'INSERT INTO users (email, name) VALUES ("sylvie@dylan.com", "Sylvie");' | mysql -uroot -p holberton
Enter password: 
stevecmd@stevecmd-HP-ENVY-15-Notebook-PC:/media/stevecmd/48444E06444DF6EA/ALX/Specialization/Backend/alx-backend-storage/0x00-MySQL_Advanced$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Jean");' | mysql -uroot -p holberton
Enter password: 
ERROR 1062 (23000) at line 1: Duplicate entry 'bob@dylan.com' for key 'users.email'
stevecmd@stevecmd-HP-ENVY-15-Notebook-PC:/media/stevecmd/48444E06444DF6EA/ALX/Specialization/Backend/alx-backend-storage/0x00-MySQL_Advanced$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
id      email   name
1       bob@dylan.com   Bob
2       sylvie@dylan.com        Sylvie

```

