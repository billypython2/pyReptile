from pyReptile.storage import *


class MovieComment(DataStorage):
    # Define table metadata
    def field(self):
        self.movieId = Column(String(50), comment='电影ID')
        self.user = Column(String(50), comment='用户名')
        self.comment = Column(String(3000), comment='评论内容')


class MovieInfo(DataStorage):
    # Define table metadata
    def field(self):
        self.movieId = Column(String(50), comment='电影ID')
        self.name = Column(String(50), comment='电影名称')
        self.summary = Column(String(3000), comment='剧情简介')
