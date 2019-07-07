from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from git import Repo
import os
import subprocess
# import json
import simplejson as json


@csrf_exempt 
# Create your views here.

# def console(cmd):
#     p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
#     out, err = p.communicate()
#     return (p.returncode, out, err)

def index(request):
    json_object = json.loads(request.body)
    data  = json_object['data']['code']
    f = open("javascriptTest.js", "w");
    f.write(data);
    f.close()
 
    shell_output_security =  subprocess.Popen('nodejsscan -f javascriptTest.js -o output.json', shell=True, stdout=subprocess.PIPE);
    shell_output_security.wait();
    shell_output_lint =  subprocess.Popen('jshint javascriptTest.js', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE);
    shell_output_lint.wait();
    f = open('output.json', "r")
    v = json.loads(f.read());
    # print(os.system('nodejsscan -f javascript.js'));
    # print('shell_output_lint--', shell_output_lint.communicate())
    output, err = shell_output_lint.communicate()
    rc = shell_output_lint.returncode
    print('--output---', output);
    responseData = {
        'message': v,
        'lint': output,
    }
    return HttpResponse(json.dumps(responseData), content_type='application/json');
    # return HttpResponse(shell_output);
@csrf_exempt 
def github_webhook(request):
    print('hit');
    print('Request: ');
    event_type = request.headers["X-GitHub-Event"]
    payload    = json.loads(request.body);
    # repo = Repo(repo_path)
    print('hit payload', 'event_type', event_type);
    print(payload);

    return HttpResponse(json.dumps(payload), content_type='application/json');