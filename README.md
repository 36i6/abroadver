# abroadver
TG bot for verify from abroad

Simple telegram bot for verifying services via abroad sms
Project was created as an experiment aka diploma work

Project needs for adding FSMContent, SQLite encryption, minor string manipulations for working well as real service.
Otherwise, it can be at this time.
Service is on beta-testing. Link only eye-by-eye;)

_______
Installing on Debian/GNU:

1. Install nginx + letsencrypt

2. Bot working on webhook (polling existing and commented in app.py, but undesirable)
    Port: 7771

3. python -m pip install -r requirements.txt

4. nano /lib/systemd/system/%name%.service
---
[Unit]
Description=%%
After=network.target

[Service]
Type=Simple
Restart=always
WorkingDirectory=/path/to/bot/directory/
VIRTUAL_ENV=/path/to/bot/directory/venv
Environment=PATH=$VIRTUAL_ENV/bin:$PATH
ExecStart=/path/to/bot/venv/bin/python app.py
Restart=on-failure/always

[Install]
WantedBy=multi-user.target
---
sudo systemctl daemon-reload
sudo systemctl enable %name%
sudo systemctl restart %name%
sudo systemctl status %name%
