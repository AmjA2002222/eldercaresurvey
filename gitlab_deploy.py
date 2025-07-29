#!/usr/bin/env python3
"""
GitLab Deployment Helper for ElderCare Survey
"""

import os
import subprocess
import webbrowser

def create_gitlab_files():
    """Create necessary files for GitLab deployment"""
    print("📦 Creating GitLab deployment files...")
    
    # Create a proper .gitlab-ci.yml for Flask deployment
    gitlab_ci_content = """# GitLab CI/CD for ElderCare Survey
# Deploys to GitLab Pages with Flask

stages:
  - test
  - build
  - deploy

variables:
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.pip-cache"

cache:
  paths:
    - .pip-cache/

before_script:
  - python --version
  - pip install -r requirements.txt

test:
  stage: test
  script:
    - python -c "import flask; print('Flask version:', flask.__version__)"
    - python -c "import app; print('App imported successfully')"
  only:
    - main
    - master

build:
  stage: build
  image: python:3.9
  before_script:
    - pip install -r requirements.txt
    - pip install gunicorn
  script:
    - echo "Building Flask app..."
    - mkdir -p public
    - cp -r templates public/
    - cp app.py public/
    - cp requirements.txt public/
    - echo "from app import app" > public/wsgi.py
    - echo "Build completed!"
  artifacts:
    paths:
      - public/
    expire_in: 1 week
  only:
    - main
    - master

pages:
  stage: deploy
  image: python:3.9
  before_script:
    - pip install -r requirements.txt
    - pip install gunicorn
  script:
    - echo "Deploying to GitLab Pages..."
    - mkdir -p public
    - cp -r templates public/
    - cp app.py public/
    - cp requirements.txt public/
    - echo "from app import app" > public/wsgi.py
    - echo "Deployment completed!"
  artifacts:
    paths:
      - public/
    expire_in: 1 week
  only:
    - main
    - master
"""
    
    with open('.gitlab-ci.yml', 'w') as f:
        f.write(gitlab_ci_content)
    print("✅ Created .gitlab-ci.yml")
    
    # Create a simple deployment guide
    guide_content = """GITLAB DEPLOYMENT GUIDE FOR ELDERCARE SURVEY
========================================================

STEP 1: Push to GitLab
1. Create a new project on GitLab.com
2. Copy the repository URL
3. Run: git remote add origin YOUR_GITLAB_URL
4. Run: git push -u origin main

STEP 2: Enable GitLab Pages
1. Go to your GitLab project
2. Navigate to Settings > Pages
3. Enable Pages if not already enabled

STEP 3: Configure CI/CD
1. The .gitlab-ci.yml file is already created
2. GitLab will automatically run the pipeline
3. Check the CI/CD tab to monitor deployment

STEP 4: Access Your Survey
1. Once deployed, your survey will be available at:
   https://YOUR_USERNAME.gitlab.io/YOUR_PROJECT_NAME
2. No passcode required!
3. Accessible from anywhere in the world!

ALTERNATIVE: Use GitLab with Render
1. Push your code to GitLab
2. Go to https://render.com
3. Connect your GitLab repository
4. Deploy as a Web Service
5. Get a custom URL like: https://your-app.onrender.com

✅ NO PASSCODE REQUIRED!
✅ FREE HOSTING!
✅ AUTOMATIC DEPLOYMENT!
"""
    
    with open('GITLAB_DEPLOYMENT_GUIDE.txt', 'w') as f:
        f.write(guide_content)
    print("✅ Created deployment guide")
    
    # Create a simple HTML redirect for GitLab Pages
    html_content = """<!DOCTYPE html>
<html>
<head>
    <title>ElderCare Survey</title>
    <meta http-equiv="refresh" content="0; url=https://render.com">
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
        .container { max-width: 600px; margin: 0 auto; }
        .button { background: #3498db; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; display: inline-block; margin: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 ElderCare Survey</h1>
        <p>This survey is being deployed to a cloud platform.</p>
        <p>For the best experience, please deploy to Render or PythonAnywhere.</p>
        <a href="https://render.com" class="button">Deploy to Render (Recommended)</a>
        <a href="https://www.pythonanywhere.com" class="button">Deploy to PythonAnywhere</a>
    </div>
</body>
</html>
"""
    
    with open('public/index.html', 'w') as f:
        f.write(html_content)
    print("✅ Created public/index.html")

def main():
    print("🚀 ElderCare Survey - GitLab Deployment")
    print("=" * 50)
    print("✅ GitLab integration ready!")
    print("✅ Free hosting available!")
    print("✅ No passcode required!")
    print("=" * 50)
    
    # Create GitLab files
    create_gitlab_files()
    
    print("\n🎯 GitLab Deployment Options:")
    print("1. GitLab Pages (Static hosting)")
    print("2. GitLab + Render (Recommended)")
    print("3. GitLab + PythonAnywhere")
    
    print("\n📋 Recommended: GitLab + Render")
    print("This gives you the best of both worlds:")
    print("- GitLab for code management")
    print("- Render for Flask hosting")
    print("- No passcode required")
    print("- Professional URL")
    
    # Open GitLab
    print("\n🌐 Opening GitLab...")
    webbrowser.open("https://gitlab.com")
    
    print("\n📋 Steps to deploy:")
    print("1. Create a new project on GitLab")
    print("2. Copy the repository URL")
    print("3. Run: git remote add origin YOUR_GITLAB_URL")
    print("4. Run: git push -u origin main")
    print("5. Go to https://render.com")
    print("6. Connect your GitLab repository")
    print("7. Deploy as Web Service")
    
    # Get GitLab URL from user
    print("\n🔗 Enter your GitLab repository URL:")
    gitlab_url = input("GitLab URL (e.g., https://gitlab.com/username/eldercare-survey.git): ").strip()
    
    if gitlab_url:
        print(f"\n🔄 Adding GitLab remote: {gitlab_url}")
        try:
            # Remove existing origin if any
            subprocess.run("git remote remove origin", shell=True, capture_output=True)
            
            # Add new origin
            result = subprocess.run(f"git remote add origin {gitlab_url}", shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ GitLab remote added successfully!")
                
                # Push to GitLab
                print("🔄 Pushing to GitLab...")
                push_result = subprocess.run("git push -u origin main", shell=True, capture_output=True, text=True)
                if push_result.returncode == 0:
                    print("✅ Code pushed to GitLab successfully!")
                    print("🎉 Your repository is now on GitLab!")
                    
                    # Open Render for deployment
                    print("\n🌐 Opening Render for deployment...")
                    webbrowser.open("https://render.com")
                    
                    print("\n📋 Next steps:")
                    print("1. Go to Render.com")
                    print("2. Sign up for free account")
                    print("3. Click 'New +' → 'Web Service'")
                    print("4. Connect your GitLab account")
                    print("5. Select your eldercare-survey repository")
                    print("6. Configure:")
                    print("   - Build Command: pip install -r requirements.txt")
                    print("   - Start Command: python app.py")
                    print("   - Plan: Free")
                    print("7. Click 'Create Web Service'")
                    print("8. Your survey will be live at: https://your-app-name.onrender.com")
                    
                else:
                    print(f"❌ Error pushing to GitLab: {push_result.stderr}")
            else:
                print(f"❌ Error adding GitLab remote: {result.stderr}")
        except Exception as e:
            print(f"❌ Error: {e}")
    else:
        print("❌ No GitLab URL provided.")
    
    print("\n🎯 Alternative: Direct deployment without GitLab")
    print("If you prefer not to use GitLab, you can:")
    print("1. Use PythonAnywhere (upload zip file)")
    print("2. Use Render (direct upload)")
    print("3. Use Railway (direct upload)")
    
    input("\nPress Enter when you've completed the deployment...")
    
    print("\n🎉 Your ElderCare survey should now be live!")
    print("Share the URL with anyone - no passcode required!")

if __name__ == "__main__":
    main() 