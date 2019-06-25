from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
import subprocess
import json


@csrf_exempt 
# Create your views here.

def index(request):
    # json_object = json.loads(request.body)
    # data  = json_object['data']['code']
    # f = open("javascript.js", "w")
    # f.write(data);
    # f.close()
 
    shell_output =  subprocess.Popen('nodejsscan -f javascript.js', shell=True, stdout=subprocess.PIPE).stdout
    shell_output =  shell_output.read();
    print(os.system('nodejsscan -f javascript.js'));
    print(os.system('jshint javascript.js'))
    # responseData = {
    #     'message': shell_output.decode(),
    # }
    # return HttpResponse(json.dumps(responseData), content_type='application/json');
    return HttpResponse(shell_output);