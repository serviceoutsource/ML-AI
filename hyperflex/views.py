# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
import hyperflex.analyze.user_analyze as analyze
import json


DATA = analyze.load_data()


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


def single_user_analysis(request):
    """
    全体用户数据单体分析
    :param request:
    :return:
    """
    result_set = analyze.analyze_single_user_info(DATA)
    return json.dumps(result_set)


def all_user_analysis(request):
    """
    全体用户综合数据分析
    :param request:
    :return:
    """
    result_set = analyze.analyze_all_user_info(DATA)
    return json.dumps(result_set)
