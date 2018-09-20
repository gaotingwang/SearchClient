# _*_ coding: utf-8 _*_

from elasticsearch_dsl import Document, Date, Integer, Keyword, Text, connections, Completion, analyzer

# 使用参考地址 https://github.com/elastic/elasticsearch-dsl-py

# 定义与es服务器连接，连接地址允许有多个
connections.create_connection(hosts=["localhost"])

my_analyzer = analyzer('ik_max_word')


class ArticleType(Document):
    """ 伯乐在线文章类型 """

    # 使用搜索建议，必须添加suggest属性，type为completion
    suggest = Completion(analyzer=my_analyzer) # 此处需要指定自己定义analyzer
    # 伯乐在线文章类型
    title = Text(analyzer="ik_max_word")
    create_date = Date()
    url = Keyword()
    url_object_id = Keyword()
    front_image_url = Keyword()
    front_image_path = Keyword()
    praise_nums = Integer()
    comment_nums = Integer()
    fav_nums = Integer()
    tags = Text(analyzer="ik_max_word")
    content = Text(analyzer="ik_smart")
    crawl_time = Date()

    # 定义了es中对应的index
    class Index:
        name = 'jobbole' # index
        doc_type = "article"
        # settings = {
        #     "number_of_shards": 2,
        # }

    class Meta:
        doc_type = "article"


class LagouType(Document):
    """ 拉勾网工作职位 """

    suggest = Completion(analyzer=my_analyzer)
    title = Text(analyzer="ik_max_word")
    url = Keyword()
    url_object_id = Keyword()
    salary_min = Integer()
    salary_max = Integer()
    job_city = Keyword()
    work_years_min = Integer()
    work_years_max = Integer()
    degree_need = Text(analyzer="ik_max_word")
    job_type = Keyword()
    publish_time = Date()
    job_advantage = Text(analyzer="ik_max_word")
    job_desc = Text(analyzer="ik_max_word")
    job_addr = Text(analyzer="ik_max_word")
    company_name = Keyword()
    company_url = Keyword()
    tags = Text(analyzer="ik_max_word")
    crawl_time = Date()

    # 定义了es中对应的index
    class Index:
        name = 'lagou'
        doc_type = "job"

    class Meta:
        doc_type = "job"


class ZhiHuQuestionType(Document):
    """ 知乎问题 """

    suggest = Completion(analyzer=my_analyzer)
    # 知乎的问题 item
    zhihu_id = Keyword()
    topics = Text(analyzer="ik_max_word")
    url = Keyword()
    title = Text(analyzer="ik_max_word")
    content = Text(analyzer="ik_max_word")
    answer_num = Integer()
    comments_num = Integer()
    watch_user_num = Integer()
    click_num = Integer()
    crawl_time = Date()

    # 定义了es中对应的index
    class Index:
        name = 'zhihu'
        doc_type = "question"

    class Meta:
        doc_type = "question"


class ZhiHuAnswerType(Document):
    """ 知乎回答 """

    suggest = Completion(analyzer=my_analyzer)
    # 知乎的问题 item
    zhihu_id = Keyword()
    url = Keyword()
    question_id = Keyword()
    author_id = Keyword()
    content = Text(analyzer="ik_max_word")
    praise_num = Integer()
    comments_num = Integer()
    create_time = Date()
    update_time = Date()
    crawl_time = Date()
    author_name = Keyword()

    # 定义了es中对应的index
    class Index:
        name = 'zhihu'
        doc_type = "answer"

    class Meta:
        doc_type = "answer"
