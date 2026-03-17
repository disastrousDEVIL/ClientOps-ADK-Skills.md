import pathlib
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.skills import load_skill_from_dir
from google.adk.tools import skill_toolset

load_dotenv()

brief_generator_skill = load_skill_from_dir(pathlib.Path("skills/brief-generator"))
company_policy_skill = load_skill_from_dir(pathlib.Path("skills/company-policy"))
meeting_summary_skill = load_skill_from_dir(pathlib.Path("skills/meeting-summary"))
email_writer_skill = load_skill_from_dir(pathlib.Path("skills/email-writer"))

skills_main = skill_toolset.SkillToolset(
    skills=[
        brief_generator_skill,
        company_policy_skill,
        meeting_summary_skill,
        email_writer_skill,
    ]
)

root_agent = Agent(
    name="root_agent",
    description="Helps with briefs, policies, meeting summaries, and emails.",
    model=LiteLlm(model="gpt-5.4"),
    tools=[skills_main],
    instruction="You are a helpful assistant that can help with a variety of tasks.",
)