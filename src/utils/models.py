""" 公用的一些模型

是否启用
"""
from .db import db


class PluginSetting(db.Model):
    """ 插件的设置

    可以针对不同插件，不同群，不同机器人保存不同配置
    如果 bot_id 为 null 则是适用于所有 bot 的设置，group_id 同理
    """
    __tablename__ = 'plugin_setting'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String)
    group_id = db.Column(db.Integer())
    bot_id = db.Column(db.Integer())
    key = db.Column(db.String)
    value = db.Column(db.String)
