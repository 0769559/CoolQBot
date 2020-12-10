import nonebot
from nonebot import export
from nonebot.log import logger
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base

driver = nonebot.get_driver()

engine = create_async_engine(driver.config.database, echo=True)
Base = declarative_base()

# 导出
export().Base = Base
export().engine = engine


@driver.on_startup
async def _():
    logger.info('启动数据库')
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
