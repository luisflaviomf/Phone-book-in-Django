# Phone book in Django

# **About this project**

This was my first project in Django (A rapid web development framework written in Python). 

It's a simple contact management with easy configs, Bootstrap interface, WhatsApp integration, and easy contact deletion.

## **Libraries**
```py
from django.contrib import admin  # Admin interface for managing models via the web.
from django.apps import AppConfig  # Configurations for Django applications.
from django.forms import ModelForm  # Simplifies form creation based on models.
from django.db import models  # Defines database table structures.
from django.test import TestCase  # Base class for creating Django test cases.
from django.urls import path, include  # Defines URL patterns and includes other configurations.
from django.shortcuts import render, redirect, get_object_or_404  # Shortcuts for rendering, redirecting, and getting objects or 404 errors.
```
## **How does it work?**

When executing this program, the user only needs to go to 'create new contact' and enter the desired contact's name and number.

## **Examples**

### **Simple interface made with bootstrap.**
&nbsp;

![alt text](https://i.ibb.co/F5RjXDJ/site1.png)
&nbsp;

### **Simple creation of new contacts.**
&nbsp;

![alt text](https://i.ibb.co/31c59X4/site2.png)
&nbsp;

### **Automatic integration with whatsapp.**
&nbsp;

![alt text](https://media.giphy.com/media/gh684r9Mjftrf6QbBB/giphy.gif)
&nbsp;

### **Easy to delete a contact.**
&nbsp;

![alt text](https://media.giphy.com/media/ZbCFNQyFBfj2VBCI2P/giphy.gif)
