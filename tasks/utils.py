from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View

class WelcomeView():
    def init(self):
        self.template = 'tasks/welcome.html'
        self.context = {}