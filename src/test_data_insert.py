from db_setup import Session
from models.question import Question
from models.section import Section

session = Session()

category1 = Section(name='Science')
category2 = Section(name='History')
category3 = Section(name='Geography')

session.add_all([category1, category2, category3])
session.commit()

question1 = Question(
    section=category1,
    question_text='Who developed the theory of relativity?',
    ans_1='Isaac Newton',
    ans_2='Galileo Galilei',
    ans_3='Albert Einstein',
    ans_4='Niels Bohr',
    ans_5='Marie Curie',
    hint_1='Hint 1: He is known for his equation E=mc^2.',
    hint_2='Hint 2: He won the Nobel Prize in Physics in 1921.',
    hint_3='Hint 3: His famous work includes the photoelectric effect.',
    hint_4='Hint 4: He was born in Germany in 1879.',
    hint_5='Hint 5: His first name starts with "A".',
    right_answer_index=3
)

question2 = Question(
    section=category2,
    question_text='In which year did World War II end?',
    ans_1='1939',
    ans_2='1942',
    ans_3='1945',
    ans_4='1950',
    ans_5='1960',
    hint_1='Hint 1: The war lasted for six years.',
    hint_2='Hint 2: D-Day, a significant event in the war, occurred in 1944.',
    hint_3='Hint 3: The war ended with the surrender of Germany and Japan.',
    hint_4='Hint 4: The United Nations was established after the war.',
    hint_5='Hint 5: The year starts with "19".',
    right_answer_index=3
)

question3 = Question(
    section=category3,
    question_text='What is the capital of Australia?',
    ans_1='Sydney',
    ans_2='Melbourne',
    ans_3='Canberra',
    ans_4='Brisbane',
    ans_5='Perth',
    hint_1='Hint 1: It is not Sydney or Melbourne.',
    hint_2='Hint 2: The city was purpose-built to be the capital.',
    hint_3='Hint 3: The Australian Parliament House is located here.',
    hint_4='Hint 4: It is inland, not on the coast.',
    hint_5='Hint 5: The name starts with "C".',
    right_answer_index=3
)

question4 = Question(
    section=category1,
    question_text='What is the chemical symbol for gold?',
    ans_1='Au',
    ans_2='Ag',
    ans_3='Fe',
    ans_4='Cu',
    ans_5='Pt',
    hint_1='Hint 1: It is a two-letter symbol.',
    hint_2='Hint 2: It comes from the Latin word "aurum".',
    hint_3='Hint 3: It is a precious metal.',
    hint_4='Hint 4: It is often used in jewelry.',
    hint_5='Hint 5: It is often represented as a yellow metal.',
    right_answer_index=1
)

question5 = Question(
    section=category2,
    question_text='Who was the first President of the United States?',
    ans_1='John Adams',
    ans_2='Thomas Jefferson',
    ans_3='George Washington',
    ans_4='James Madison',
    ans_5='Benjamin Franklin',
    hint_1='Hint 1: He is often referred to as the "Father of His Country".',
    hint_2='Hint 2: He led the Continental Army during the American Revolution.',
    hint_3='Hint 3: He presided over the Constitutional Convention of 1787.',
    hint_4='Hint 4: His face is on the one-dollar bill.',
    hint_5='Hint 5: His last name starts with "W".',
    right_answer_index=3
)

# Dodajemy pytania do sesji
session.add_all([question1, question2, question3, question4, question5])
session.commit()
