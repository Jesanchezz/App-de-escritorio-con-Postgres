from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from Modelsdb import Answer, Question, Test 
from credentialsdb import credentials
if __name__ == "__main__":
    engine = create_engine(f"postgresql://{credentials['user']}:{credentials['password']}@{credentials['host']}:{credentials['port']}/{credentials['db']}")
    Session = sessionmaker(bind = engine)
    session = Session()

    questions = [
        
        Question(
            question_text = '¿Cómo se define una lista?',
            answers = [
                Answer(
                    answer_text = 'lista = [1,2,3]',
                    is_correct = True
                ),
                Answer(
                    answer_text = 'lista = (1,2,3)',
                    is_correct = False
                ),
                Answer(
                    answer_text = 'iter(1,2,3)',
                    is_correct = False
                )
            ]
        ),

        Question(
            question_text = '¿Qué excepción lanza un iterador?',
            answers = [
                Answer(
                    answer_text = 'StopIteration',
                    is_correct = True
                ),
                Answer(
                    answer_text = 'ZeroDivision',
                    is_correct = False
                ),
                Answer(
                    answer_text = 'SyntaxError',
                    is_correct = False
                )
            ]
        ),

        Question(
            question_text = '¿Puede modificar un elemento de una tupla?',
            answers = [
                Answer(
                    answer_text = 'Si',
                    is_correct = False
                ),
                Answer(
                    answer_text = 'Jamás',
                    is_correct = True
                ),
                Answer(
                    answer_text = 'Un poquito',
                    is_correct = False
                )
            ]
        ),
    ]

    test = Test(test_name ='Python', questions=questions)
    session.add(test)
    session.commit()