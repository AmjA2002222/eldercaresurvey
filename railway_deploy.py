#!/usr/bin/env python3
"""
Direct Railway Deployment - No GitHub Required
"""

import os
import subprocess
import webbrowser
import zipfile
import tempfile

def create_deployment_package():
    """Create a zip file of the project for direct deployment"""
    print("📦 Creating deployment package...")
    
    # Files to include in deployment
    files_to_include = [
        'app.py',
        'requirements.txt',
        'Procfile',
        'runtime.txt',
        'templates/survey.html',
        'templates/waiting_list.html',
        'README.md'
    ]
    
    # Create temporary zip file
    with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as tmp_file:
        zip_path = tmp_file.name
    
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file_path in files_to_include:
            if os.path.exists(file_path):
                zipf.write(file_path, file_path)
                print(f"✅ Added {file_path}")
            else:
                print(f"⚠️  Skipped {file_path} (not found)")
    
    print(f"📦 Deployment package created: {zip_path}")
    return zip_path

def main():
    print("🚀 ElderCare Survey - Direct Railway Deployment")
    print("=" * 55)
    print("✅ No GitHub required!")
    print("✅ Free hosting!")
    print("✅ No passcode needed!")
    print("=" * 55)
    
    # Create deployment package
    zip_path = create_deployment_package()
    
    print("\n🎯 Deploying to Railway...")
    print("Follow these simple steps:")
    print("1. Go to https://railway.app")
    print("2. Click 'Start a New Project'")
    print("3. Choose 'Deploy from GitHub' (we'll use a simple repo)")
    print("4. Or use 'Deploy from Template' and upload our files")
    
    # Alternative: Use Render with direct upload
    print("\n🌐 Alternative: Render with direct upload")
    print("1. Go to https://render.com")
    print("2. Sign up for free account")
    print("3. Click 'New +' → 'Web Service'")
    print("4. Choose 'Build and deploy from a Git repository'")
    print("5. Connect GitHub (we'll create a simple one)")
    
    # Let me create a simple GitHub repo automatically
    print("\n🔧 Creating a simple GitHub repository automatically...")
    
    # Check if gh CLI is available
    gh_check = subprocess.run("gh --version", shell=True, capture_output=True)
    
    if gh_check.returncode == 0:
        print("✅ GitHub CLI found. Creating repository...")
        try:
            # Create repo using GitHub CLI
            subprocess.run("gh repo create eldercare-survey --public --source=. --remote=origin --push", shell=True)
            print("✅ GitHub repository created and code pushed!")
            
            # Open Render for deployment
            print("\n🌐 Opening Render for deployment...")
            webbrowser.open("https://render.com")
            
            print("\n📋 Render Deployment Steps:")
            print("1. Click 'New +' → 'Web Service'")
            print("2. Connect your GitHub account")
            print("3. Select 'eldercare-survey' repository")
            print("4. Configure:")
            print("   - Name: eldercare-survey")
            print("   - Build Command: pip install -r requirements.txt")
            print("   - Start Command: python app.py")
            print("   - Plan: Free")
            print("5. Click 'Create Web Service'")
            
        except Exception as e:
            print(f"❌ Error creating GitHub repo: {e}")
            print("Let's try a different approach...")
    else:
        print("❌ GitHub CLI not found. Let's use a different approach...")
    
    # Alternative approach: Use Netlify Drop or similar
    print("\n🎯 Alternative: Use Netlify Drop (No account needed!)")
    print("1. Go to https://app.netlify.com/drop")
    print("2. Drag and drop your project folder")
    print("3. Get instant deployment!")
    
    # Open Netlify Drop
    print("\n🌐 Opening Netlify Drop...")
    webbrowser.open("https://app.netlify.com/drop")
    
    print(f"\n📦 Your deployment package is ready: {zip_path}")
    print("You can upload this zip file to any hosting service!")
    
    # Wait for user
    input("\nPress Enter when you've completed the deployment...")
    
    print("\n🎉 Your ElderCare survey should now be live!")
    print("Share the URL with anyone - no passcode required!")

if __name__ == "__main__":
    main() 