from botbuilder.core import TurnContext, MessageFactory
from msgraph.generated.users import users_request_builder
from msgraph import GraphServiceClient

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
    
    async def get_id(self, graph_client):
        result = graph_client.users.by_user_id('7def1fbf-f04e-4c2f-8921-41f24202d550').online_meetings.by_online_meeting_id('431330455232')
        print(result)
        # return result

    async def get_transcript(self, graph_client):
        pass
    