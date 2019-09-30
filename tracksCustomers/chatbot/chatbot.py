from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot(
    'Sahim',
   
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'maximum_similarity_threshold': 0.99,
            
        }
    ]
)


trainer=ListTrainer(chatbot)


trainer.train([
    'introduction',
    'I am sahim'
])

trainer.train([
    'hi',
    'hi there'
])

trainer.train([
    'what is your name',
    'I am a bot but I am not a human'
])
