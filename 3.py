# -*- coding: utf-8 -*-
"""
Created on Thu May 23 20:40:09 2024

@author: FX-tec
"""

import csv

def ask_questions(questions):
    score = 0
    total_questions = len(questions)
    for i, (question, answer) in enumerate(questions, 1):
        print(f"Question {i}: {question}")
        user_answer = input("Your answer: ").strip()
        if user_answer.lower() == answer.lower():
            score += 1
    return score, total_questions

def save_result(user_name, score, total_questions, file_name):
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user_name, score, total_questions])

def main():
    user_name = input("Enter your name: ")
    questions = [
        ("What is the largest country", "russia"),
        ("what color is the sea ?", "blue"),
     
    ]
    score, total_questions = ask_questions(questions)
    print(f"Your score: {score}/{total_questions}")
    save_result(user_name, score, total_questions, 'results.csv')

if __name__ == "__main__":
    main()