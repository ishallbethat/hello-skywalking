import os
from skywalking import agent, config
from flask import Flask
from service import some_method, some_other_method, async_func, async_func2

# 参考文档 https://github.com/apache/skywalking-python/tree/master/docs/en/setup
os.environ["SW_AGENT_NAME"] = "gabriel"
os.environ["SW_AGENT_INSTANCE"] = "gabriel"
os.environ["SW_AGENT_COLLECTOR_BACKEND_SERVICES"] = "127.0.0.1:11800"
config.log_reporter_level="INFO"
config.log_reporter_active=True # 启动日志上报
config.log_reporter_layout="%(asctime)s [%(threadName)s] %(levelname)s %(name)s - %(message)s"
config.flask_collect_http_params = True # 将 flask 参数上报
agent.start()
##导入结束
# import logging
# from framework import app
# if __name__ != '__main__': #gunicorn 启动
#     gunicorn_logger = logging.getLogger('gunicorn.error')
#     app.logger.handlers = gunicorn_logger.handlers
#     app.logger.setLevel(gunicorn_logger.level)

# if __name__ == '__main__':#flask 启动
#     app.run(host=app.config["HOST"], port=app.config["PORT"], debug=app.config["DEBUG_MODEL_SWITCH"])

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/abc')
def abc():
    some_method()
    return 'Hello, World!'

@app.route('/async')
def haha():
    async_func2()
    return 'Hello, World!'

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8881)