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



from twilio.rest import Client 
def twilio_announce(account_sid, 
                    auth_token, 
                    from_phone, 
                    to_phone, 
                    filename="ファイル"): 
    ''' 
    SMSで完了をお知らせ 
     
    account_sid=Your Account SID from twilio.com/console 
    auth_token=Your Auth Token from twilio.com/console 
    ''' 
    client = Client(account_sid, auth_token) 
    message = client.messages.create( 
        to=to_phone,  
        from_=from_phone, 
        body="スクレピング完了しました。"+filename+"を確認ください。") 
    return print(message.sid)
    
#twilio_announce 
#SMSで完了をお知らせ 
#twilio_announce 
#SMSで完了をお知らせ 
twilio_account_sid= "AC57a7######6d5d9911c8e4caf2" 
twilio_auth_token= "91823e#####e3e62d45cfc72b74" 
twiilio_to="+8170#####4753" 
twiilio_from="+16#####121" 
twilio_announce(twilio_account_sid, 
                twilio_auth_token, 
                twiilio_from, 
                twiilio_to)
