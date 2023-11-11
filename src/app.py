import json

from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.question import Question
from models.section import Section
app = Flask(__name__)
CORS(app)

engine = create_engine('sqlite:///development.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()


@app.route("/questions/<question_id>", methods=['GET'])
def get_question(question_id):
    try:
        question = session.query(Question).filter(Question.id == question_id).first()

        if question:
            question_data = {
                'id': question.id,
                'section_id': question.section_id,
                'question_text': question.question_text,
                'ans_1': question.ans_1,
                'ans_2': question.ans_2,
                'ans_3': question.ans_3,
                'ans_4': question.ans_4,
                'ans_5': question.ans_5,
                'hint_1': question.hint_1,
                'hint_2': question.hint_2,
                'hint_3': question.hint_3,
                'hint_4': question.hint_4,
                'hint_5': question.hint_5,
                'right_answer_index': question.right_answer_index,
            }

            return jsonify(question_data)
        else:
            return jsonify({'error': 'Question not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route("/sections", methods=['GET'])
def get_sections():
    try:
        sections = session.query(Section).all()
        sections_list = []

        for section in sections:
            section_data = {
                'id': section.id,
                'name': section.name,
            }
            sections_list.append(section_data)

        return jsonify(sections_list)

    except Exception as e:
        return jsonify({'error': str(e)})


@app.route("/exams", methods=['GET'])
def exams():
    response = [
        {"exam_id": 1, "exam_name": "LDEK-J-2005"},
        {"exam_id": 2, "exam_name": "LDEK-J-2006"},
        {"exam_id": 3, "exam_name": "LDEK-J-2007"},
        {"exam_id": 4, "exam_name": "LDEK-J-2008"},
        {"exam_id": 5, "exam_name": "LDEK-J-2009"},
        {"exam_id": 6, "exam_name": "LDEK-J-2010"},
        {"exam_id": 7, "exam_name": "LDEK-J-2011"}
    ]
    return json.dumps(response, indent=0)
