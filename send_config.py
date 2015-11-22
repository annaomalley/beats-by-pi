import subprocess
import yaml

def send_email(user, pwd, recipient, subject, body):
    import smtplib
    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body
    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.googlemail.com")
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except smtplib.SMTPException, error:
        print str(error)
        print "failed to send mail"

if __name__ == '__main__':
    subprocess.Popen('ifconfig > ifconfig.txt', shell=True)
    with open('config.yml', 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
    with open('ifconfig.txt','r') as iffile:
        ifc = iffile.read()
    send_email(cfg['from_email_user'], cfg['from_email_pass'], cfg['to_email_users'], "[Raspberry] Server Config Info", ifc)
