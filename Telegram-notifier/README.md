## Telegram Notifier Script

First of all it's better to copy your public ssh-key into servers:
   ```
   ssh-copy-id -p SSH_PORT SSH_USER@IP
   ```
## Run Script 

1. First install requirements 
   
   ```
   pip install -r requirements.txt
   ```
2. Run script like as below:
   
   ```
   python3 Telegram-notifier.py
   ```

If You need to Automate to send , do it with cronjob. 
