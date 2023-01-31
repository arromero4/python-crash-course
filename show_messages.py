
def show_messages(message):
    for msg in message:
        print(f"Los mensajes que se enviarán son: {msg}" )

def show_sent_messages(message):
    for msg in message:
        print(f"Los mensajes enviados fueron: {msg}" )

def sent_messages(listMsg, sentMessages):
    """
    prints each text message and moves each
    message to a new list called sent_messages
    """
    while listMsg:
        current_message = listMsg.pop()
        #print(f"The current message is: {current_message}")
        sentMessages.append(current_message)



listMsg = ['Hello World!', 'Race Start!', 'Magnifico!']
sentMessages = []


sent_messages(listMsg[:], sentMessages)
show_messages(listMsg)
show_sent_messages(sentMessages)
print(listMsg)
print(sentMessages)