from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatbot = ChatBot(
    'TracksBot',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    logic_adapters=[
        {
            # 'import_path': 'chatterbot.logic.BestMatch',
            'import_path': 'chatbot/askQuestionLogicAdapter.MyLogicAdapter',
            # 'maximum_similarity_threshold': 0.99,
            
        }
    ]
)

# chatbot.storage.drop()

trainer=ListTrainer(chatbot)


trainer.train([
    'introduction',
    '<p>Tracks uses artificial intelligence to predict and manage  one of the biggest uncertainties of the road freight  industry the fuel consumption of trucks </p>  <p>Our predictive fuel analytics enable truck fleet operators to save fuel, reduce CO2 emissions, and improve their bottom line.</p>',
    'what is the fleet number?'
])

# trainer.train([
#     'hi',
#     'hi there'
# ])

# trainer.train([
#     'what is your name',
#     'I am a bot but I am not a human'
# ])
