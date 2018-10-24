import imapclient
import pyzmail

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('my_email_address@gmail.com', 'MY_SECRET_PASSWORD')
imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['SINCE 05-Jul-2014'])
rawMessages = imapObj.fetch([40041], ['BODY[]', 'FLAGS'])
message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
message.get_subject()

message.get_addresses('from')
message.get_addresses('to')
message.get_addresses('cc')

message.get_addresses('bcc')

message.text_part != None
message.text_part.get_payload().decode(message.text_part.charset)
message.html_part != None
message.html_part.get_payload().decode(message.html_part.charset)
imapObj.logout()