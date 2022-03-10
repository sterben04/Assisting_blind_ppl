from django.shortcuts import render
from django.http import HttpResponse
import shutil
import os
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, 'index.html')

import numpy as np
from PIL import Image
import base64
import re
from binascii import a2b_base64


from io import StringIO 

@csrf_exempt
def get_image(request):
    if request.method == 'POST':

        image_b64 = request.POST.get('imgBase64', None)
    
        binary_data = a2b_base64(image_b64)

        fd = open('/home/aravind/volume/final_project/Assisting_blind_ppl/blind_ppl/webapp/static/images/image.png', 'wb')
        fd.write(binary_data)
        fd.close()

        print('No problem...continue')
    return ''