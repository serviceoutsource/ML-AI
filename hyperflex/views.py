# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
import hyperflex.analyze.user_analyze as analyze
import hyperflex.algorithm.svd_recommend as svd
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
    user_id = request.GET['user_id']; meal_type = request.GET['meal_type']
    recommended_set = svd.recommend(svd.load_data_from_db(meal_type=meal_type), user_id)
    return HttpResponse(json.dumps(recommended_set))


def single_user_analysis(request):
    """
    全体用户数据单体分析
    :param request:
    :return:
    """
    result_set = analyze.analyze_single_user_info(DATA)
    return HttpResponse(json.dumps(result_set))


def all_user_analysis(request):
    """
    全体用户综合数据分析
    :param request:
    :return:
    """
    result_set = analyze.analyze_all_user_info(DATA)
    return HttpResponse(json.dumps(result_set))
