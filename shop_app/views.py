from django.shortcuts import render
from . import models
from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse('Welcome to my SHOP!')


def about(request):
    logger.debug('About page accessed')
    return HttpResponse('This is the ABOUT page.')


def contact(request):
    logger.debug('Contact page accessed')
    return HttpResponse('This is the CONTACT page.')

