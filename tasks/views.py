from django.shortcuts import render
import logging


logger = logging.getLogger(__name__)

def my_view(request):
    logger.info("This is an info message")
    logger.error("Something went wrong")