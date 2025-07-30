# PythonAnywhere Deployment Guide

## Step 1: Sign up at PythonAnywhere
1. Go to [pythonanywhere.com](https://pythonanywhere.com)
2. Create a free account
3. Verify your email

## Step 2: Upload your files
1. Go to "Files" tab
2. Create a new directory: `eldercaresurvey`
3. Upload all your files to this directory

## Step 3: Create a web app
1. Go to "Web" tab
2. Click "Add a new web app"
3. Choose "Flask" and "Python 3.9"
4. Set the path to: `/home/yourusername/eldercaresurvey`
5. Set the WSGI file to: `/home/yourusername/eldercaresurvey/wsgi.py`

## Step 4: Install dependencies
1. Go to "Consoles" tab
2. Start a new Bash console
3. Run: `pip install -r requirements.txt`

## Step 5: Configure the app
1. Edit the WSGI file to match your username
2. Reload the web app
3. Your survey will be live at: `https://yourusername.pythonanywhere.com`

## Benefits of PythonAnywhere:
✅ Free forever (no time limits)
✅ No sleep after inactivity
✅ Reliable and stable
✅ Easy to manage
✅ Good for Flask apps
