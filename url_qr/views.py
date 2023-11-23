from django.shortcuts import redirect, render
from django.urls import reverse
import django.views.generic
import random

from django.views import View
from django.views.generic import TemplateView
from .utility import url_random
from django.http import HttpResponseRedirect
from .models import Url_QR

from .serializers import UrlQrSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions


class CreateUrlApiView(APIView):
    queryset = Url_QR.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = UrlQrSerializer
    
    def post(self, request,  *args, **kwargs):
        serializer = self.serializer_class(data = self.request.data)
        serializer.is_valid(raise_exception = True)
        generate = serializer.validated_data.get('generate')
        url_long = serializer.validated_data.get('url_long')
        url_shorted = serializer.validated_data.get('url_short')
        select_1 = serializer.validated_data.get('select_1')
        select_2 = serializer.validated_data.get('select_2')
    
        if generate:
            random_url = url_random()
            new_url = Url_QR(url_long=url_long, url_short=random_url)
            new_url.save()
            qr_code_image = Url_QR.objects.all().get(url_short=random_url)
            counter = len(Url_QR.objects.all())
            return Response(
                {
                    'success': True,
                    'url_short': random_url,
                    'qr_code': qr_code_image.qr_code.url,
                    'counter': counter,
                    'message': 'Successfully created short URL.',
                    'status': 200,
                }, status = 200
            )
            
        else:
            all_url = Url_QR.objects.all()
            random_num = random.randint(0, 9)
            url_short = f"{url_shorted}_{select_1}{select_2}"
            db_url = all_url.filter(url_short = url_short).first()
            counter = len(Url_QR.objects.all())
            if db_url:
                return Response(
                {
                    'success': False,
                    'url_short': url_short,
                    'qr_code': None,
                    'counter': counter,
                    'message': 'Please enter another URL. This short URL is in our database.',
                    'status': 202,
                }, status = 200
                )
            else:
                new_url = Url_QR(url_long=url_long, url_short=url_short)
                new_url.save()
                qr_code_image = Url_QR.objects.all().get(url_short=url_short)
                counter = len(Url_QR.objects.all())
                return Response(
                {
                    'success': True,
                    'url_short': url_short,
                    'qr_code': qr_code_image.qr_code.url,
                    'counter': counter,
                    'message': 'Successfully created short URL.',
                    'status': 200,
                }, status = 200
                )
                
                
                
                
class InfoApiView(APIView):
    queryset = Url_QR.objects.all()
    permission_classes = (permissions.AllowAny, )
    def get(self, request,  *args, **kwargs):
        counter = self.queryset.count()
        return Response(
                {
                    'success': True,
                    'counter': counter,
                    'message': 'Successfully send Info.',
                }, status = 200
            )
    



class SendToLongUrl(View):
    def get(self, request, url_short):
        long_url = Url_QR.objects.all().filter(url_short=url_short).first()
        if long_url:
            return HttpResponseRedirect(long_url.url_long)
        return HttpResponseRedirect('Page not found')
        
      
      
      
      
class HomeView(TemplateView):
    template_name = 'index.html'
    
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return response

            