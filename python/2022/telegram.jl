using Telegram

bot_token = "5084995372:AAHEvFHWjrTTEhi9gJifK_PFPeg8hL94fXw"

chat_id = "484229211"
tg = TelegramClient(bot_token, chat_id=chat_id)

#Telegram.sendMessage(tg, text="Ciao Matteo, buon Natale")
#run_bot() do msg
#    println(msg)
#end

# send an image
Telegram.sendPhoto(tg, photo = open("/Users/sani/Downloads/141203854_3818262274860573_5386218796734864436_o.jpg", "r"))

# send an file
#Telegram.sendDocument(tg, document = open("path/to/document.txt", "r"))

#open("path/to/picture.jpg", "r") do io
#    sendPhoto(tg, photo = io)
#end

#io = IOBuffer()
#print(io, "Hello world!")
#Telegram.sendDocument(document = "hello.txt" => io)
