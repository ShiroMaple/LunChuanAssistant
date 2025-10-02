import sys
import os

AGENT_DIR= os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(AGENT_DIR)
LIBS_DIR = os.path.join(BASE_DIR, 'libs')

sys.path.insert(0, AGENT_DIR) 
sys.path.insert(0, BASE_DIR)

# 添加 libs 目录到路径（跳过 .dist-info 目录）
if os.path.exists(LIBS_DIR):
    for item in os.listdir(LIBS_DIR):
        item_path = os.path.join(LIBS_DIR, item)
        if os.path.isdir(item_path) and not item.endswith('.dist-info'):
            sys.path.insert(0, item_path)
    sys.path.insert(0, LIBS_DIR)

# 导入依赖
try:
    import numpy
    import maa
    import MaaAgentBinary
    import strenum
    print("所有依赖加载成功")
except ImportError as e:
    print(f"依赖加载失败: {e}")
    sys.exit(1)

from maa.agent.agent_server import AgentServer
from maa.toolkit import Toolkit

import my_action
import my_reco


def main():
    Toolkit.init_option("./")

    socket_id = sys.argv[-1]

    AgentServer.start_up(socket_id)
    AgentServer.join()
    AgentServer.shut_down()


if __name__ == "__main__":
    main()
