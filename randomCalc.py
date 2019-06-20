#!/usr/bin/python
# good ideas from https://stackoverflow.com/questions/26260950/how-can-i-randomly-choose-a-maths-operator-and-ask-recurring-maths-questions-wit

import random
import operator
import pprint
import json

def randomCalc():
  ops = {'+':operator.add,
         '-':operator.sub,
         '*':operator.mul,
         '/':operator.truediv}
  number1 = random.randint(1,10)
  number2 = random.randint(1,10) #avoid divide by zero
  op = random.choice(list(ops.keys()))
  answer = ops.get(op)(number1,number2)
  print('What is {} {} {}?\n'.format(number1, op, number2))
  return answer

def selectCalc(selected_op):
  ops = {'+':operator.add,
         '-':operator.sub,
         '*':operator.mul,
         '/':operator.truediv}
  number1 = random.randint(1,10)
  number2 = random.randint(1,10) #avoid divide by zero
  op = selected_op
  question = '{} {} {}'.format(number1, op, number2)
  answer = ops.get(op)(number1,number2)
# print('What is {} {} {}?\n'.format(number1, op, number2))
  print json.dumps({"Question": question, "Answer": answer})
  return answer

def askQuestion():
  answer = randomCalc()
  guess = float(input())
  return guess == answer

def quiz():
  print('Welcome. This is a 10 question math quiz\n')
  score = 0
  for i in range(10):
    correct = askQuestion()
    if correct:
      score += 1
      print('Correct!\n')
    else:
      print('Incorrect!\n')
  return 'Your score was {}/10'.format(score)

#print(quiz())
#askQuestion()

#print('Welcome, this is a generated item\n')
#print('Question:\n')
#answer = randomCalc()

# Return 1 question and answer as a json object
answer = selectCalc('+')

#print('Answer: {}'.format(answer))
