from maa.agent.agent_server import AgentServer
from maa.custom_action import CustomAction
from maa.context import Context

counter=0
counterMax=5

@AgentServer.custom_action("news_counter")
class MyCustomAction(CustomAction):

    def run(
        self,
        context: Context,
        argv: CustomAction.RunArg,
    ) -> bool:
        global counter
        global counterMax
        counter+=1
        print(f"新闻资讯任务已执行{counter}轮")
        if counter>=counterMax:
            print(f"新闻资讯已完成")
            context.override_pipeline({argv.node_name:{"next":"新闻资讯_stop"}})
        return CustomAction.RunResult(success=True)
    
@AgentServer.custom_action("init_counter")
class MyCustomAction(CustomAction):

    def run(
        self,
        context: Context,
        argv: CustomAction.RunArg,
    ) -> bool:
        global counterMax
        param_str = argv.custom_action_param.strip('"\'')
        counterMax=int(param_str)
        print(f"新闻资讯任务次数设定为{counterMax}次")
        return CustomAction.RunResult(success=True)