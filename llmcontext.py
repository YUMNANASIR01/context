# ------------------- llm context -------------------
from dotenv import load_dotenv
from agents import Agent,Runner,set_tracing_disabled,RunContextWrapper,function_tool
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
    return f"User Name is : {wrapper.context.name}, User Age is : {wrapper.context.age} "
# --------------------------------llm context mai function tool ka decorator jata hai -------------------------------------
@function_tool
async def yumna_user_info(wrapper: RunContextWrapper[UserInfo]) :
    """ This function returns the user address from the context. """
    return f" User Adress is : {wrapper.context.adress}"
# -----------------------------------------------------------------------
agent= Agent[UserInfo](
    model="gpt-4.1-nano" ,
    name= "my_agent",
    instructions= dynamic_instr,
    tools=[yumna_user_info]  # ----------------- function tool ko pass karte hain
)
res = Runner.run_sync(agent, "what is the name of the user and what is his address", context=UserInfo_information)
rich.print(res.final_output)