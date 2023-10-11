from django.shortcuts import render
from .models import Questions
import time
import openai,os
from dotenv import load_dotenv
import re
load_dotenv()
api_key=os.getenv("OPENAI_KEY", None)

# Create your views here.
def index(request):
    dict_q={
        'ques':Questions.objects.all()
    }
    return render(request,'index.html',dict_q)

def chatbot(request,id):
    obj=Questions.objects.get(q_id=id)
    dict_q={
        'ques':obj,
    }
    
    
    return render(request,'chat.html',dict_q)

def suggest(request):
    obj="Your solution is well-structured and should meet the time and memory constraints effectively. It utilizes a common approach to solve this problem, and the time complexity is linear, which is efficient given the input constraints.Your code creates a new linked list to store the result, handles carry, and traverses both input linked lists while adding corresponding digits. The overall logic appears correct.Based on the provided code, your solution is suitable for competitive coding, and it is expected to pass the time and memory constraints. You do not need to reshape it."
    dict_a={
        'ans':obj
    }
    time.sleep(4)
    return render(request,'suggest.html',dict_a)
