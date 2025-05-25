from dotenv import load_dotenv
from agents import Agent, Runner,function_tool,RunContextWrapper
import rich
load_dotenv()  # Yeh .env file ko load karega
from dataclasses import dataclass
# --------------------------------context -------------------------------------
# ----------------- class user info
@dataclass
class UserInfo():
    name: str
    age: int
    adress: str

# ---------------------- instance of user info
user_information = UserInfo( "Yumna", 21,"123 Main St, Springfield")

# -----------------------------function tool----------------------------------------
@function_tool 
                    # ------------function tool ka decorator hai is mai function ko pass karna hai
async def fetch_user_info(wrapper: RunContextWrapper[UserInfo]) -> str:
    # --------------------------- is mai body hoti hai  agent ki context ko use karte hain
     return f"User Name is : {wrapper.context.name}, User Age is : {wrapper.context.age} and User Adress is : {wrapper.context.adress}"

# -----------------------------Agent code----------------------------------------
agent= Agent[UserInfo](
    model="gpt-4.1-nano" ,
    name= "my_agent",
    instructions= "You are a helpful assistant.",
    tools=[fetch_user_info],  # ----------------- function tool ko pass karte hain
)
# -------------------------------------------------------------
                                # ----------------- run the agent with user information context
                 # -------------------------ab user information ko context ke tor par pass karte hain
                #  ------------------------------ is mai instance araha hai user info ka
res = Runner.run_sync(agent, "what is the name of the user and the age of the user and the adress of the user?", context=user_information)
rich.print(res.final_output)
# rich.print(res)
    


  











