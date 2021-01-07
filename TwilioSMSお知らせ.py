from twilio.rest import Client

filename="#######"

#SMSで完了をお知らせ 
# Your Account SID from twilio.com/console 
account_sid = "################" 
# Your Auth Token from twilio.com/console 
auth_token  = "###############" 
 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
    to="+81#######3",  
    from_="+16#######1", 
    body="スクレピング完了しました。"+filename+"を確認ください。") 
 
print(message.sid) 
