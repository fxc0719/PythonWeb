import smtplib # 负责发送邮件
from email.mime.text import MIMEText # 负责构造邮件


# 通过smtp发送
# 输入Email地址和口令
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址
to_addr = input('To: ')
# 输入SMTP服务器地址
smtp_server = input('SMTP server: ')

# 输入正文
email_msg = input('Bodies: ')
# 参数
# 正文，MIME的subtype，文本编码格式
msg = MIMEText(email_msg, 'plain', 'utf-8')

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()