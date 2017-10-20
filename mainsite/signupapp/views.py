from django.shortcuts import render
from django.contrib.auth import authenticate
from django import forms
from django.template.context_processors import csrf


def index(request):
    return "Yeah"