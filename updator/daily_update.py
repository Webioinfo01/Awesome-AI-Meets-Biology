from aweagent.agent import PaperAgent
from datetime import datetime, timedelta
import os
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base
import json, ast
# 通用 Database 类
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Database:
    def __init__(self, db_url, Base):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = None
        self.Base = Base

    def get_session(self):
        if self.session is None:
            self.session = self.Session()
        return self.session

    def close(self):
        if self.session:
            self.session.close()
            self.session = None

    def insert_many(self, orm_class, data_list):
        session = self.get_session()
        objects = [orm_class(**data) for data in data_list]
        session.add_all(objects)
        session.commit()

    def query_all(self, orm_class):
        session = self.get_session()
        return session.query(orm_class).all()

    def query_filter(self, orm_class, **kwargs):
        session = self.get_session()
        return session.query(orm_class).filter_by(**kwargs).all()

    def __del__(self):
        self.close()

# 环境变量
os.environ["DATABASE_URL"] = "sqlite:///updator/SemanticScholar_papers.db"
os.environ["DATABASE_FILTER_URL"] = (
    "sqlite:///updator/SemanticScholar_papers_filter.db"
)

today = datetime.now().strftime("%Y-%m-%d")
last7d = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
pa = PaperAgent()
rep = pa.run(
    msg=f"""
    查询论文：
     query: AI agent|large language model|foundation model
     publication_date: {last7d} 到 {today}
     limit: 100
     fields: "paperId",  "externalIds", "url", "title", "abstract", "venue", "publicationVenue", "publicationTypes", "publicationDate", "journal", "authors", "citations"
     fields_of_study: "Medicine",  "Biology"
    
    pre-defined category: ["ai-agents", "ai-tools", "foundation-models", "databases", "benchmarks", "reviews"]

    """
)

from aweagent.db import Paper, Base as PaperBase

# 目标数据库 ORM
Base = declarative_base()

class AwePaper(Base):
    __tablename__ = 'AI_papers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    year = Column(Integer)
    title = Column(String(200))
    team = Column(String(100))
    teamWebsite = Column(String(100))
    affiliation = Column(String(100))
    domain = Column(String(100))
    venue = Column(String(100))
    paperUrl = Column(String(100))
    codeUrl = Column(String(50))
    githubStars = Column(Integer)
    doi = Column(String(50))
    category = Column(String(50))

# 数据库初始化
src_db = Database("sqlite:///updator/SemanticScholar_papers_filter.db", PaperBase)
dst_db = Database("sqlite:///updator/ai_papers.db", AwePaper)

# 读取所有论文
papers = src_db.query_all(Paper)

# 构建插入数据
insert_data = []
for paper in papers:
    print(paper.title)
    doi = paper.doi
    # 先查目标表是否已存在该doi
    if doi:
        exists = dst_db.query_filter(AwePaper, doi=doi)
        if exists:
            continue  # 已存在，跳过
    print(paper.authors)
    authors = ast.literal_eval(paper.authors)
    entry_data = {
        "category": paper.category,
        "year": paper.year,
        "title": paper.title,
        "team":authors['name'],
        "teamWebsite": None,
        "affiliation": ",".join(authors['affiliations']),
        "domain": paper.domain,
        "venue": paper.venue,
        "paperUrl": paper.url,
        "codeUrl": None,
        "githubStars": None,
        "doi": paper.doi,
    }
    insert_data.append(entry_data)

dst_db.insert_many(AwePaper, insert_data)
src_db.close()

print("已从原数据库迁移数据到 awe_papers 表。")


import ast
papers = dst_db.query_all(AwePaper)

# 分组
data = {}
for paper in papers:
    cat = paper.category or "other"
    print(paper.team)
    # 字段名映射，和 data.json 保持一致
    paper_dict = {
        "year": str(paper.year) if paper.year else "",
        "title": paper.title,
        "team": paper.team,
        "team website": paper.teamWebsite,
        "affiliation": paper.affiliation,
        "domain": paper.domain,
        "venue": paper.venue,
        "paperUrl": paper.paperUrl,
        "codeUrl": paper.codeUrl,
        "githubStars": str(paper.githubStars) if paper.githubStars else "",
        "doi": paper.doi,
    }
    if cat not in data:
        data[cat] = []
    data[cat].append(paper_dict)

# 写出 json
with open("docs/data1.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("已导出为 data.json")

dst_db.close()