from config import AppConfig, BotConfig
from bot.acrobot import Acrobot

from azure.identity import ClientSecretCredential
from msgraph import GraphServiceClient
from msgraph.generated.users.item.online_meetings.online_meetings_request_builder import OnlineMeetingsRequestBuilder
from kiota_abstractions.api_error import APIError
from botbuilder.core import TurnContext
from botbuilder.integration.aiohttp import CloudAdapter, ConfigurationBotFrameworkAuthentication
from botbuilder.core.integration import aiohttp_error_middleware
from botbuilder.schema import Activity
import sys
import traceback
import asyncio
from http import HTTPStatus
from aiohttp import web
from aiohttp.web import Request, Response, json_response

appConfig = AppConfig()
botConfig = BotConfig()

# Authorization of app and bot to access Graph API and MS Teams respectively
credential = ClientSecretCredential(
    tenant_id=appConfig.TENANT_ID,
    client_id=appConfig.CLIENT_ID,
    client_secret=appConfig.CLIENT_SECRET
)

scopes = ['https://graph.microsoft.com/.default']

graph_client = GraphServiceClient(credential, scopes)
# print(graph_client.teams.)
adapter = CloudAdapter(ConfigurationBotFrameworkAuthentication(botConfig))

bot = Acrobot()


# Checking for errors
async def on_error(context: TurnContext, error: Exception):
    print(f"\n [on_turn_error] unhandled error: {error}", file=sys.stderr)
    traceback.print_exc()

    await context.send_activity("The bot encountered an error or bug.")
    await context.send_activity("To continue to run this bot, please fix the bot source code.")


# Listen for incoming requests on /api/messages
async def messages(req: Request) -> Response:
    if "application/json" in req.headers["content-type"]:
      body = await req.json()
    else:
      return Response(status = HTTPStatus.UNSUPPORTED_MEDIA_TYPE)

    activity = Activity().deserialize(body)

    auth_header = req.headers["Authorization"] if "Authorization" in req.headers else ""
    response = await adapter.process_activity(auth_header, activity, bot.handle_message)

    if response:
        return json_response(data = response.body, status = response.status)
    return Response(status = HTTPStatus.OK)

# async def get_id():
#         try:
#             query_params = OnlineMeetingsRequestBuilder.by_online_meeting_id(
#                 self = "",
#                 online_meeting_id = '482236079896')
#             result = await graph_client.users.get(request_configuration = query_params)
            
#             print(result)
#             # return result
#         except APIError as err:
#             print(err)

async def join_meeting():
    try:
        meeting_id = "123"
        join_url = f"https://teams.microsoft.com/l/meeting/{meeting_id}"
        join_endpoint = f"/me/onlineMeetings/{meeting_id}/join"

        # response = graph_client.online
        invoke("POST", join_endpoint)
    except APIError as err:
        print(err)

# asyncio.run(bot.get_users(graph_client))
# asyncio.run(bot.display_transcript(graph_client))
asyncio.run(get_id())

app = web.Application(middlewares = [aiohttp_error_middleware])
app.router.add_post("/api/messages", messages)
# adapter.on_turn_error = on_error


if __name__ == '__main__':
    try:
        web.run_app(app, host = AppConfig.ENDPOINT, port = BotConfig.PORT)
    except Exception as err:
       raise err