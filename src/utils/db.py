from gino import Gino
from nonebot import get_driver, logger

db = Gino()

on_startup = get_driver().on_startup


@on_startup
async def _():
    logger.info('数据库初始化')
    await db.set_bind(get_driver().config.database)
    await db.gino.create_all()
