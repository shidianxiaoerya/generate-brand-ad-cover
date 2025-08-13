# -*- coding: utf-8 -*-  
"""
MCP广告封面生成器服务器启动脚本
"""
import sys
import os

# 将当前目录添加到Python路径中，以便能够导入src.mcp_plus
sys.path.insert(0, os.path.abspath('.'))

# 导入我们自己的模块
from src.mcp_plus import main

if __name__ == "__main__":
    main()