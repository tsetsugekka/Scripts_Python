#メール自動送付（添付付き）
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

stmp_server = "smtp.gmail.com"
stmp_port = 587
stmp_user = "■■■■■■■■■■■■■■"
stmp_password = "■■■■■■■■■■■■■■"

to_address = "■■■■■■■■■■■■■■"
cc_address = "■■■■■■■■■■■■■■,■■■■■■■■■■■■■■" #複数人の場合はカンマで区切り
from_address = stmp_user
subject = "■■■■■■■■■■■■■■"
body = """
<html>
    <body>
        <h1>■■■■■■■■■■■■■■の自動送付です。</h1>
        <p>添付にてお送りいたします。</p>
        <p>よろしくお願いいたします。</p>
    </body>
</html>"""

filepath = r"■■■■■■■■■■■■■■.csv"
filename = os.path.basename(filepath)

msg = MIMEMultipart()
msg["Subject"] = subject
msg["From"] = from_address
msg["To"] = to_address
msg["Cc"] = cc_address
msg.attach(MIMEText(body, "html"))

with open(filepath, "rb") as f:
    mb = MIMEApplication(f.read())

mb.add_header("Content-Disposition", "attachment", filename=filename)
msg.attach(mb)

s = smtplib.SMTP(stmp_server, stmp_port)
s.ehlo()
s.starttls()
s.ehlo()
s.login(stmp_user, stmp_password)
s.sendmail(from_address, [to_address,cc_address], msg.as_string())　#ccやbccがいるときは[]を使用
s.quit()

print("Eメールを送信しました。")
