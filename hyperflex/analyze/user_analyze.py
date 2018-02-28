# -*-coding: utf-8 -*-


import pandas as pd
import hyperflex_recommend.enpity.DataBase as db

MEAL_TYPE = [1, 2, 3]


def analyze_single_user_info(result):
    """

    :param result:
    :return:
        examp: {user_id: 1, meal_info: {breakfast:{food_name:菜名，times:次数}}, {early_dinner:{...}}, {supper:{...}}}
    """
    result = pd.DataFrame(result, columns=['user_id', 'user_name', 'food_code', 'food_name', 'meal_type', 'eat_time'])
    user_id = set(result['user_id'])
    user_dict = {}
    for i in user_id:
        user_info = result[result['user_id'] == i]
        breakfast_info = user_info[user_info['meal_type'] == MEAL_TYPE[0]]
        early_dinner_info = user_info[user_info['meal_type'] == MEAL_TYPE[1]]
        dinner_info = user_info[user_info['meal_type'] == MEAL_TYPE[0]]

        def analyze_meal_info(meal_info):
            """

            :param meal_info:
            :return:
            """
            food_name = set(meal_info['food_name'])
            result_set = []
            for name in food_name:
                tmp = {'food_name': name, 'times': len(meal_info[meal_info['food_name'] == name])}
                result_set.append(tmp)
            return result_set

        meal_type = {'breakfast': analyze_meal_info(breakfast_info),
                     'early_dinner': analyze_meal_info(early_dinner_info),
                     'supper': analyze_meal_info(dinner_info)}
        user_dict = {'user_id': i, 'meal_info': meal_type}

    return user_dict


def analyze_all_user_info(result):
    """

    :param result:
    :return:
    """
    pass


def load_data():
    query = 'select ' \
            'm.user_id, user_name, m.food_code, food_name, meal_type, eat_time ' \
            'from ' \
            'User u ' \
            'right join ' \
            'Meal m on u.user_id = m.user_id ' \
            'left join ' \
            'Food f on m.food_code=f.food_code;'
    cur, connect = db.DataBaes().connect_db()
    cur.execute(query)
    data = cur.fetchall()
    return data


if __name__ == '__main__':
    result = load_data()
    analyze_single_user_info(result=result)
