
# 拼接get请求参数
def path_with_query(path, query):
    temp = []
    for key in query:
        temp.append('{}={}'.format(key, query[key]))

    result = '&'.join(temp)
    result = str(path) + '?' + result
    return result


def test_path_with_query():
    path = '/student'
    query = {
        'name':'dudu',
        'age':12
    }
    #  字段的遍历没有顺序
    expected = [
        '/student?name=dudu&age=12',
        '/student?age=12&name=dudu'
    ]
    # 判断数组中的一项是否在数组中的操作符是 In
    assert path_with_query(path,query) in expected


