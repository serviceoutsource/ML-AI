# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse


def get_tianmao_voice_answer(request):
    """
    从后台webhook获取用户与天猫精灵交互语音识别结果
    :param request:
    :return:
    """
    pass


def recipe_recommended(request):
    """
    向后台webhook返回菜谱推荐结果
    :param request:
    :return:
    """
    pass


def user_analysis(request):
    """
    用户分析数据反馈至前段进行数据可视化展示
    :param request:
    :return:
    """
    pass
