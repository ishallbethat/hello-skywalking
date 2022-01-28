from time import sleep

from skywalking import Component
from skywalking.decorators import trace, runnable
from skywalking.trace.context import SpanContext, get_context
import logging

@trace()  # the operation name is the method name('some_other_method') by default
def some_other_method():
    logging.info("this is log from some_other_method")
    sleep(1)


@trace(op='awesome')  # customize the operation name to 'awesome'
def some_method():
    logging.info("this is log from some_method")
    some_other_method()


@trace(op='async_functions_are_also_supported')
async def async_func():
    logging.info("this is log from async_func")
    return 'asynchronous'


@trace()
async def async_func2():
    return await async_func()

