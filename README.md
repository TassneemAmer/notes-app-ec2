# Notes App on AWS EC2

A simple note-taking web application deployed on AWS EC2 using Python (Flask) and MariaDB with EBS backup.

## Tech Stack
- Python (Flask)
- MariaDB
- AWS EC2 (RHEL 10)
- EBS Volume mounted on /backup

## Features
- Write and save notes via browser
- Notes stored with timestamps
- Latest notes appear first

## How to Run
```bash
ssh -i key.pem ec2-user@<EC2_PUBLIC_DNS>
sudo -i
cd /root/notes-app
python3 app.py
