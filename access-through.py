import dotenv
dotenv.load_dotenv()  # May skip if you have exported environment variables.
from google.adk.runners import InMemoryRunner
from google.genai.types import Part, UserContent
from fact_checker.agent import root_agent

user_input = "Double check this: Earth is further away from the Sun than Mars."

runner = InMemoryRunner(agent=root_agent)
session = runner.session_service.create_session(
    app_name=runner.app_name, user_id="test_user"
)
content = UserContent(parts=[Part(text=user_input)])
for event in runner.run(
    user_id=session.user_id, session_id=session.id, new_message=content
):
    for part in event.content.parts:
        print(part.text)