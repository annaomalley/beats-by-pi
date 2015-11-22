# beats-by-pi

SMS controlled music player

Requirements
------------
* Linux
* Python 2.7.6
* Flask 0.10.1
* PyYaml 3.11
* [Google Data Python Library](https://developers.google.com/gdata/articles/python_client_lib#linux)
* [youtube-dl](https://rg3.github.io/youtube-dl/)
* VLC player
* Twilio account and SMS enabled number

Installation
------------

1. Clone the repository
  ```
   git clone https://github.com/annaomalley/beats-by-pi.git
  ```
  
2. Edit the config.yml file
   ```yaml
    youtube_api_key: 'XXXXXXXXXX' 
    from_email_user: 'sender@gmail.com' # sends ip info from this address*
    from_email_pass: 'senderpass'
    to_email_users: ['receiver@email.com'] # sends ip info to this address
   ```
  *currently configured to send from gmail accounts

3. Change your Request URL in the Twilio Messaging dashboard to your server's IP and set to HTTP POST

Running
------------
1. Start the server

   ```python
    python run.py
   ```
2. Send texts to your Twilio SMS number
3. ???
4. Music

Helpful Resources
------------
* http://martin-thoma.com/configuration-files-in-python/
