# coding: utf-8

# In[46]:


import jieba

text = '''新乡SEO 昊天 seo 168seo.cn 免费分享最新的SEO技术,本站的目的是与同行交流SEO知识,并提供企业网站优化、企业网站诊断等服务,白帽SEO从我做起,专注用户体验研究''
'''
seg_list = jieba.cut_for_search(text)  # 搜索引擎模式
# 对于要处理的文本进行搜索引擎分词处理
data = list(seg_list)
# 分词后 转化成list
stopwords = [line.rstrip() for line in open('stopwords.txt', 'r', encoding="gbk").readlines()]
# 读取停止词,生成list
data = [d for d in data if d not in stopwords]
# 剔除 停止词

c = dict.fromkeys(data, 0)

# 构造构造字典,并且默认值为0

for x in data:
    c[x] += 1
# 统计频次

newc = sorted(c.items(), key=lambda x: x[1], reverse=True)
# 进行高频词排序

print(newc)


# In[ ]:
