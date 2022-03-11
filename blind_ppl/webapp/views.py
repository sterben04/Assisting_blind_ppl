from django.shortcuts import render
from django.http import HttpResponse
import shutil
import os
from django.views.decorators.csrf import csrf_exempt

import numpy as np
from PIL import Image
import base64
import re
from binascii import a2b_base64
import pickle
from webapp.model.model_predict import gen_caption

# Create your views here.
def index(request):
    return render(request, 'index.html')



@csrf_exempt
def get_image(request):
    if request.method == 'POST':

        image_b64 = request.POST.get('imgBase64', None)
    
        binary_data = a2b_base64(image_b64)

        fd = open('/home/aravind/volume/final_project/Assisting_blind_ppl/blind_ppl/webapp/static/images/image.jpg', 'wb')
        fd.write(binary_data)
        fd.close()

        print('Genrating Caption......')
        caption = gen_caption
        print(caption)
    return ''



    # pass