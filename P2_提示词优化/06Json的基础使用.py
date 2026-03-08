import json

d = {
    "name": "张三",
    "age": 18,
    "sex": "男"
}
s = json.dumps(d, ensure_ascii=False)
print(s)

a = [
    {
        "name": "张三",
        "age": 18
    },
    {
        "name": "张三",
        "age": 18
    }
]

b = json.dumps(a, ensure_ascii=False)
print(b)

json_str = '{"name": "张三", "age": 18}'
json_array_str = '[{"name": "张三", "age": 18}, {"name": "张三", "age": 18}]'

res_dict = json.loads(json_str)
print(res_dict,type(res_dict))
res_list = json.loads(json_array_str)
print(res_list,type(res_list))