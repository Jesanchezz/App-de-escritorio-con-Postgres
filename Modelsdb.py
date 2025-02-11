from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Boolean
from credentialsdb import credentials

Base = declarative_base()


class Answer(Base):
    __tablename__ = 'answer'
    answer_id = Column(Integer, primary_key = True)
    answer_text = Column(String(200))
    is_correct = Column(Boolean, nullable = True)
    question_id = Column(Integer, ForeignKey('question.question_id', ondelete = 'CASCADE'))


    def __repr__(self) ->str:
        return f'Answer object: Answer id: {self.answer_id}. Answer text: {self.answer_text}'

class Question(Base):
    __tablename__ = 'question'
    question_id = Column(Integer, primary_key = True)
    question_text = Column(String(200))
    answers = relationship('Answer', cascade = 'all,delete', backref = backref('question'))
    test_id = Column(Integer, ForeignKey('test.test_id', ondelete = 'CASCADE'))


    def __repr__(self) ->str:
        return f'Question object: Question id: {self.question_id}. Question text: {self.question_text}'

class Test(Base):
    __tablename__ = 'test'
    test_id = Column(Integer, primary_key=True)
    test_name = Column(String(100))
    questions = relationship('Question', cascade = 'all , delete', backref = backref('test'))

    
    def __repr__(self) ->str:
        return f'Test object: Test id: {self.test_id}. Test text: {self.test_text}'
    

#Creamos base de datos
db_url = f"postgresql:{credentials['user']}//:{credentials['password']}@{credentials['host']}:{credentials['port']}/{credentials['db']}"
if __name__ == '__main__':
    engine = create_engine(db_url, echo = True)
    Base.metadata.create_all(engine)
