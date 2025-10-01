from maa.agent.agent_server import AgentServer
from maa.custom_action import CustomAction
from maa.context import Context

counter=0

@AgentServer.custom_action("news_counter")
class MyCustomAction(CustomAction):

    def run(
        self,
        context: Context,
        argv: CustomAction.RunArg,
    ) -> bool:
        global counter
        counter+=1
        print(f"新闻资讯任务已完成{counter}次")
        if counter>=5:
            print(f"听广播")
            context.override_pipeline({argv.node_name:{"next":"enter_MyPage"}})
        return CustomAction.RunResult(success=True)