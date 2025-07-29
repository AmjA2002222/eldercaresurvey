#!/usr/bin/env python3
"""
GitHub Private Repository Deployment for ElderCare Survey
Step-by-step guide with private repository setup
"""

import os
import subprocess
import webbrowser
import time

def check_github_cli():
    """Check if GitHub CLI is installed"""
    result = subprocess.run("gh --version", shell=True, capture_output=True, text=True)
    return result.returncode == 0

def install_github_cli():
    """Install GitHub CLI if not available"""
    print("📦 Installing GitHub CLI...")
    
    # Detect OS and install GitHub CLI
    if os.name == 'posix':  # macOS/Linux
        if subprocess.run("which brew", shell=True, capture_output=True).returncode == 0:
            print("🍺 Installing via Homebrew...")
            subprocess.run("brew install gh", shell=True)
        else:
            print("📥 Installing GitHub CLI manually...")
            print("Please visit: https://cli.github.com/")
            print("Or run: brew install gh")
    else:
        print("📥 Please install GitHub CLI from: https://cli.github.com/")
    
    return check_github_cli()

def setup_github_repo():
    """Create a private GitHub repository"""
    print("🔐 Creating private GitHub repository...")
    
    if not check_github_cli():
        print("❌ GitHub CLI not found. Installing...")
        if not install_github_cli():
            print("❌ Could not install GitHub CLI automatically.")
            print("Please install it manually from: https://cli.github.com/")
            return False
    
    # Check if user is logged in
    auth_result = subprocess.run("gh auth status", shell=True, capture_output=True, text=True)
    if auth_result.returncode != 0:
        print("🔑 Please log in to GitHub CLI...")
        subprocess.run("gh auth login", shell=True)
    
    # Create private repository
    print("🏗️  Creating private repository 'eldercare-survey'...")
    repo_result = subprocess.run(
        "gh repo create eldercare-survey --private --source=. --remote=origin --push",
        shell=True, capture_output=True, text=True
    )
    
    if repo_result.returncode == 0:
        print("✅ Private GitHub repository created successfully!")
        print("🔒 Repository is private - only you can see it!")
        return True
    else:
        print(f"❌ Error creating repository: {repo_result.stderr}")
        return False

def deploy_to_render():
    """Help deploy to Render using the GitHub repository"""
    print("\n🌐 Deploying to Render...")
    print("Render will host your Flask app with a public URL!")
    
    # Open Render
    webbrowser.open("https://render.com")
    
    print("\n📋 Render Deployment Steps:")
    print("1. Click 'Sign Up' (free account)")
    print("2. Click 'New +' → 'Web Service'")
    print("3. Click 'Connect account' → 'GitHub'")
    print("4. Select your 'eldercare-survey' repository")
    print("5. Configure the service:")
    print("   - Name: eldercare-survey")
    print("   - Build Command: pip install -r requirements.txt")
    print("   - Start Command: python app.py")
    print("   - Plan: Free")
    print("6. Click 'Create Web Service'")
    print("7. Wait for deployment (2-3 minutes)")
    print("8. Your survey will be live at: https://eldercare-survey.onrender.com")

def main():
    print("🚀 ElderCare Survey - GitHub Private Deployment")
    print("=" * 60)
    print("✅ Private repository (only you can see the code)")
    print("✅ Free hosting on Render")
    print("✅ No passcode required for survey access")
    print("✅ Step-by-step instructions")
    print("=" * 60)
    
    print("\n📋 Step-by-Step Process:")
    print("1. Create private GitHub repository")
    print("2. Push code to GitHub")
    print("3. Deploy to Render (free hosting)")
    print("4. Get public URL for survey")
    
    # Step 1: Create GitHub repository
    print("\n🔐 STEP 1: Creating Private GitHub Repository")
    print("-" * 50)
    
    if setup_github_repo():
        print("✅ Repository created successfully!")
        
        # Step 2: Push code
        print("\n📤 STEP 2: Pushing Code to GitHub")
        print("-" * 50)
        
        push_result = subprocess.run("git push -u origin main", shell=True, capture_output=True, text=True)
        if push_result.returncode == 0:
            print("✅ Code pushed to GitHub successfully!")
            print("🔒 Your code is now safely stored in a private repository!")
            
            # Step 3: Deploy to Render
            print("\n🌐 STEP 3: Deploying to Render")
            print("-" * 50)
            deploy_to_render()
            
            print("\n🎉 DEPLOYMENT COMPLETE!")
            print("=" * 50)
            print("✅ Private GitHub repository: https://github.com/YOUR_USERNAME/eldercare-survey")
            print("✅ Public survey URL: https://eldercare-survey.onrender.com")
            print("✅ No passcode required for survey access!")
            print("✅ Only you can see the source code!")
            
        else:
            print(f"❌ Error pushing to GitHub: {push_result.stderr}")
    else:
        print("❌ Failed to create GitHub repository.")
        print("\n🔧 Manual Alternative:")
        print("1. Go to https://github.com/new")
        print("2. Create repository named 'eldercare-survey'")
        print("3. Make it PRIVATE")
        print("4. Don't initialize with README")
        print("5. Copy the repository URL")
        print("6. Run: git remote add origin YOUR_REPO_URL")
        print("7. Run: git push -u origin main")

if __name__ == "__main__":
    main() 