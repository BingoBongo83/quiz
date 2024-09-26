MusicQuiz Python app!


The app is written in python3.12 and uses flask, sqlalchemy, gunicorn and nginx.

I use this app for my musicquiz with friends, where I play the showmaster and they play the quiz.
4 people play against each other in 3 rounds (preround, semifinal, final).
You (showmaster) control wrong or right answers in python app via CLI and scoreboard is served via gunicorn/nginx to localhost.

All songs are stored in SQL database, you only need to create spotify (or any other streaming service) playlists similar to the database list.

I additionally use 3d printed quizbuzzers (will be published as other project).

![ScreenShot](https://github.com/BingoBongo83/musikquiz/blob/master/screenshots/musikquiz_screen1.png)
![ScreenShot](https://github.com/BingoBongo83/musikquiz/blob/master/screenshots/musikquiz_screen2.png)
![ScreenShot](https://github.com/BingoBongo83/musikquiz/blob/master/screenshots/musikquiz_screen3.png)
![ScreenShot](https://github.com/BingoBongo83/musikquiz/blob/master/screenshots/buzzer1.jpg)
![ScreenShot](https://github.com/BingoBongo83/musikquiz/blob/master/screenshots/buzzer2.jpg)

RULES:

correct answer: 2 points

wrong answer: 2 points for all other players and blocked for next song

(this is why in this case player is marked red)

best 2 players will get to the next round

thats it :)

SETUP:

create database and user on local mariadb server.

copy example.database.ini to database.ini and fill in credentials.

change to git clone directory.

create virtual environment and install requirements.txt:

  ```
  Python3.12 -m venv env
  source env/bin/activate
  pip install -r requirements.txt
  ```

install gunicorn:

  ```
  pip install gunicorn
  ```


all folders must bechanged to where you cloned git repo!

create systemd service:

  ```
  sudo cp gunicornmusikquiz.service /etc/systemd/system/gunicornmusikquiz.service
  sudo systemctl daemon-reload
  sudo systemctl start gunicornmusikquiz
  sudo systemctl enable gunicornmusikquiz
  ```

create nginx config:

  ```
  sudo cp gunicornmusikquiz /etc/nginx/sites-available/localhost
  sudo ln -s /etc/nginx/sites-available/gunicornmusikquiz /etc/nginx/sites-enabled
  sudo systemctl restart nginx
  ```
  nginx config:
  ```
  upstream webservice_musikquiz{
  server 127.0.0.1:5555;
  }

  server {
	server_name 127.0.0.1 localhost;
	access_log /var/log/nginx/access.log;
	error_log /var/log/nginx/error.log;

  location / {

	proxy_pass http://webservice_musikquiz/;
	proxy_redirect off;
  }
  }
  ```

call 127.0.0.1 in webbrowser to show scoreboard

start app with:

  ```. env/bin/activate
  Python3.12 ./main.py
  ```
