from botbuilder.core import TurnContext, MessageFactory

class Acrobot():
    def __init__(self):
        pass

    # To handle incoming messages
    async def handle_message(self, turn_context: TurnContext):
        # To echo the same message sent by sender
        return await turn_context.send_activity(
            MessageFactory.text(f"Echo: {turn_context.activity.text}")
        )
    
    async def get_users(self, graph_client):
        users = await graph_client.users.get()
        if users and users.value:
            for user in users.value:
                print(user.id, user.display_name, user.mail)
    