from flask import Flask
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

'''
{
    "question_id": 1,
    "question: "What is a cat?",
    "correct_answer": 1,
    "answer_1": "Cat",
    "answer_2": "Dog",
    "answer_3": "Bird",
    "answer_4": "Snake",
    "answer_5": "Chicken",
    "explanation_1": "What ever",
    "explanation_2": "What ever",
    "explanation_3": "What ever",
    "explanation_4": "What ever",
    "explanation_5": "What ever",
}
'''
@app.route("/questions/<question_id>", methods=['GET'])
def question(question_id):
    response = {
        "question_id": question_id,
        "question": "What is a cat?",
        "answers" : 
        [
            {
            "answer":"Cat",
            "explanation": "Because it is a cat",
            "correct" : True
            },
            {
            "answer":"Dog",
            "explanation": "Because it is not a Dog",
            "correct" : False
            },
            {
            "answer":"Bird",
            "explanation": "Because it is not a Bird",
            "correct" : False
            },
            {
            "answer":"Snake",
            "explanation": "Because it is not a Snake",
            "correct" : False
            }
        ]
    }
    return json.dumps(response, indent = 0)

@app.route("/sections", methods=['GET'])
def sections():
    response = [
        {"section_id":1, "section_name":"Stomatologia zachowawcza"},
        {"section_id":2, "section_name":"Stomatologia dziecięca"},
        {"section_id":3, "section_name":"Endodendo"}
    ]
    return json.dumps(response, indent = 0)

@app.route("/exams", methods=['GET'])
def exams():
    response = [
        {"exam_id":1, "exam_name":"LDEK-J-2005"},
        {"exam_id":2, "exam_name":"LDEK-J-2006"},
        {"exam_id":3, "exam_name":"LDEK-J-2007"},
        {"exam_id":4, "exam_name":"LDEK-J-2008"},
        {"exam_id":5, "exam_name":"LDEK-J-2009"},
        {"exam_id":6, "exam_name":"LDEK-J-2010"},
        {"exam_id":7, "exam_name":"LDEK-J-2011"}
    ]
    return json.dumps(response, indent = 0)
