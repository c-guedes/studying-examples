import telepot, time
import datetime as dt


bot = telepot.Bot('578012223:AAFjXoFrzYwfE4vCNUM-hcOFKrgLOn0dnE4')



def handle(msg):
    global ids
    content_type, chat_type, chat_id = telepot.glance(msg)
    username = msg['from']['username']
    userid = msg['from']['id']
    rpli = msg['message_id']
    user = msg['from']['username']
    id = msg['from']['id']
    #print(msg)
    print(msg)

    if msg['text'] == 'nom':
        #bot.sendMessage(-1001329390640, "*BOM DIA SEU ARROMBADO!*", parse_mode='Markdown')
        bot.sendMessage(-1001302996167, "*BOM DIA SEU ARROMBADO!*", parse_mode='Markdown')



bot.message_loop(handle)
print ('Rodando ...')

# Keep the program running.
while 1:
    if dt.datetime.now().hour == 13 and dt.datetime.now().minute == 31 and dt.datetime.now().second == 10:
        #if dt.datetime.now().minute == 26:
            #if dt.datetime.now().second == 20:
        bot.sendMessage(-1001329390640, "*BOA TARDE SEUS ARROMBADO!*", parse_mode='Markdown')
                #time.sleep(2)
    time.sleep(3)

''''#enviar tarde
    if dt.datetime.now().hour == 8: 
        if dt.datetime.now().minute == 00:
            if dt.datetime.now().second == 40:
                bot.sendMessage(-1001302996167, "*BOA TARDE SEUS ARROMBADOS!*", parse_mode='Markdown')
                bot.sendSticker(-1001329390640, sticker=open('vin.webp', 'rb'))
                time.sleep(2)

    if dt.datetime.now().hour == 19:
        #enviar noite
        if dt.datetime.now().minute == 00:
            if dt.datetime.now().second == 40:
                bot.sendMessage(-1001302996167, "*BOA NOITE SEUS ARROMBADOS!*", parse_mode='Markdown')
                bot.sendSticker(-1001329390640, sticker=open('vin.webp', 'rb'))'''
