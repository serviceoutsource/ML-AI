# ML-AI

# URL 适用

1. url(r'^hyperflex/recipe_recommended/$', fun.recipe_recommended, name='recipe_recommended')，获取推荐结果，后台返回user_id（access token即可）以及对应的三餐类型；examp: hyperflex/recipe_recommended/?user_id=&meal_type=

2. url(r'^hyperflex/single_user_analysis$', fun.single_user_analysis, name='single_user_analysis')，直接调用该http API获取单个用户数据分析；examp: {user_id: 1, meal_info: {breakfast:{food_name:菜名，times:次数}}, {early_dinner:{...}}, {supper:{...}}}

3. url(r'^hyperflex/all_user_analysis$', fun.all_user_analysis, name='all_user_analysis')，直接调用获取全体用户数据分析结果；examp: {breakfast: {food_name, times}, early_dinner: {...}, supper: {...}}