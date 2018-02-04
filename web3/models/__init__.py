import json


def save(data, path):
    # json.dump把数据序列化，data, indent缩进，
    json_data = json.dumps(data, indent=2, ensure_ascii=False)
    #  open(path, 'w+', )
    with open(path, 'w+', encoding='utf-8') as f:
        f.write(json_data)


def load(path):
    with open(path, 'r',encoding='utf-8') as f:
        content =  f.read()
        return json.loads(content)


class Model(object):
    def __init__(self):
        self.name = 'dudu'
        self.age = 20


    @classmethod
    def db_path(cls):
        classname = cls.__name__
        path =  '{}.txt'.format(classname)
        return path

    @classmethod
    def all(cls):
        path = cls.db_path()
        raw_data = load(path)
        m_list = [cls.new(form) for form in raw_data]
        return m_list

    def save (self):
        # m_list是实例组成的list
        m_list = self.all()
        # self 本身也是实例呀
        m_list.append(self)
        l = [m.__dict__ for m in m_list]
        path = self.db_path()
        save(l, path)


    @classmethod
    def new(cls, form):
        m =  cls(form)
        return m

    def __repr__(self):
        classname = self.__class__.__name__
        properties = ['{}:({})'.format(k, v) for k,v in self.__dict__.items()]
        s = '\n'.join(properties)
        return '<{}\n{}>'.format(classname,s)



