#!/usr/bin/env python3
"""
PythonAnywhere Direct Deployment - No GitHub, No Account Setup Required
"""

import os
import webbrowser
import zipfile
import tempfile
import shutil

def create_deployment_files():
    """Create all necessary files for PythonAnywhere deployment"""
    print("📦 Preparing files for PythonAnywhere deployment...")
    
    # Create a deployment directory
    deploy_dir = "pythonanywhere_deploy"
    if os.path.exists(deploy_dir):
        shutil.rmtree(deploy_dir)
    os.makedirs(deploy_dir)
    
    # Copy necessary files
    files_to_copy = [
        'app.py',
        'requirements.txt',
        'templates/survey.html',
        'templates/waiting_list.html',
        'README.md'
    ]
    
    for file_path in files_to_copy:
        if os.path.exists(file_path):
            # Create directories if needed
            dest_path = os.path.join(deploy_dir, file_path)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy2(file_path, dest_path)
            print(f"✅ Copied {file_path}")
    
    # Create PythonAnywhere specific files
    wsgi_file = os.path.join(deploy_dir, "passenger_wsgi.py")
    with open(wsgi_file, 'w') as f:
        f.write("""import sys
import os

# Add the project directory to Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)

# Import the Flask app
from app import app as application

# For debugging
if __name__ == '__main__':
    application.run()
""")
    print("✅ Created passenger_wsgi.py")
    
    # Create a simple deployment guide
    guide_file = os.path.join(deploy_dir, "DEPLOYMENT_GUIDE.txt")
    with open(guide_file, 'w') as f:
        f.write("""ELDERCARE SURVEY - PYTHONANYWHERE DEPLOYMENT GUIDE
===============================================================

STEP 1: Create PythonAnywhere Account
1. Go to https://www.pythonanywhere.com/
2. Click "Create a Beginner account" (FREE)
3. Choose a username and password
4. Verify your email

STEP 2: Upload Files
1. Log into PythonAnywhere
2. Go to "Files" tab
3. Navigate to your home directory
4. Upload all files from this folder

STEP 3: Set Up Web App
1. Go to "Web" tab
2. Click "Add a new web app"
3. Choose "Flask"
4. Select Python 3.9
5. Set source code to: /home/YOUR_USERNAME/mysite
6. Set working directory to: /home/YOUR_USERNAME/mysite

STEP 4: Configure WSGI File
1. Click on the WSGI configuration file
2. Replace contents with the passenger_wsgi.py file
3. Save the file

STEP 5: Install Dependencies
1. Go to "Consoles" tab
2. Open a Bash console
3. Run: pip install -r requirements.txt

STEP 6: Reload Web App
1. Go back to "Web" tab
2. Click "Reload" button
3. Your survey will be live at: YOUR_USERNAME.pythonanywhere.com

✅ NO GITHUB REQUIRED!
✅ COMPLETELY FREE!
✅ NO PASSCODE NEEDED!
""")
    print("✅ Created deployment guide")
    
    # Create zip file
    zip_path = "eldercare_survey_pythonanywhere.zip"
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, dirs, files in os.walk(deploy_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, deploy_dir)
                zipf.write(file_path, arcname)
    
    print(f"📦 Deployment package created: {zip_path}")
    return zip_path

def main():
    print("🚀 ElderCare Survey - PythonAnywhere Deployment")
    print("=" * 55)
    print("✅ No GitHub required!")
    print("✅ Completely free!")
    print("✅ No passcode needed!")
    print("✅ Direct deployment!")
    print("=" * 55)
    
    # Create deployment package
    zip_path = create_deployment_files()
    
    print("\n🎯 Deploying to PythonAnywhere...")
    print("PythonAnywhere is perfect for Flask apps!")
    print("It's free, reliable, and doesn't require GitHub.")
    
    # Open PythonAnywhere
    print("\n🌐 Opening PythonAnywhere...")
    webbrowser.open("https://www.pythonanywhere.com/")
    
    print("\n📋 Quick Deployment Steps:")
    print("1. Create a FREE account at PythonAnywhere")
    print("2. Go to 'Files' tab and upload the zip file")
    print("3. Extract the files to your home directory")
    print("4. Go to 'Web' tab and create a new Flask web app")
    print("5. Configure the WSGI file with our passenger_wsgi.py")
    print("6. Install dependencies: pip install -r requirements.txt")
    print("7. Reload the web app")
    print("8. Your survey will be live at: YOUR_USERNAME.pythonanywhere.com")
    
    print(f"\n📦 Your deployment package: {zip_path}")
    print("Upload this file to PythonAnywhere!")
    
    # Alternative: Also show Render option
    print("\n🌐 Alternative: Render (also free, no GitHub CLI needed)")
    print("1. Go to https://render.com")
    print("2. Sign up for free account")
    print("3. Click 'New +' → 'Web Service'")
    print("4. Choose 'Build and deploy from a Git repository'")
    print("5. We'll create a simple GitHub repo for you")
    
    # Open Render as alternative
    print("\n🌐 Opening Render as alternative...")
    webbrowser.open("https://render.com")
    
    # Wait for user
    input("\nPress Enter when you've completed the deployment...")
    
    print("\n🎉 Your ElderCare survey should now be live!")
    print("Share the URL with anyone - no passcode required!")
    print("The survey will be accessible 24/7 from anywhere in the world!")

if __name__ == "__main__":
    main() 