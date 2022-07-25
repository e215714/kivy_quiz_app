import json
import random


with open("./quiz.json", encoding="utf-8") as f:
    quiz_data = json.load(f)["quiz"]

r = random.sample(quiz_data, k=2)

print(r)