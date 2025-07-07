from dotenv import load_dotenv
from agents import Agent,Runner,set_tracing_disabled,RunContextWrapper
from pydantic import BaseModel
import rich
# -----------------------------------------------
load_dotenv()
set_tracing_disabled(disabled=True)  # Disable tracing for this run
# ------------- pydentic model ---------------------
class UserInfo(BaseModel):
    name: str
    age: int
    adress: str
    # ------------------------------------------- instance of user info
UserInfo_information = UserInfo(name="Yumna", age=21, adress="123 Main St, Springfield")    
# ------------------------- local context -----------------------------
def dynamic_instr(wrapper: RunContextWrapper[UserInfo], agent : Agent) :
    wrapper.context.name = "Ali"    
    return f"User Name is : {wrapper.context.name}, User Age is : {wrapper.context.age} and User Adress is : {wrapper.context.adress}"
# --------------------------------context -------------------------------------
agent= Agent[UserInfo](
    model="gpt-4.1-nano" ,
    name= "my_agent",
    instructions= dynamic_instr,
   
)
res = Runner.run_sync(agent, "what is the name of the user", context=UserInfo_information)
rich.print(res.final_output)