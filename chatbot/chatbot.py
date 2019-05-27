from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Create a new chat bot named Charlie
chatbot = ChatBot('Charlie')
# Create a new Trainer
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.korean"
)

# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input()

        bot_response = chatbot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break