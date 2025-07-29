#!/usr/bin/env python3
"""
ElderCare Survey Auto-Deployment Script
This script helps automate the deployment process to Render
"""

import os
import subprocess
import webbrowser
import time

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} completed successfully")
            return result.stdout.strip()
        else:
            print(f"❌ {description} failed: {result.stderr}")
            return None
    except Exception as e:
        print(f"❌ Error during {description}: {e}")
        return None

def main():
    print("🚀 ElderCare Survey Auto-Deployment")
    print("=" * 50)
    
    # Step 1: Check if we're in the right directory
    if not os.path.exists('app.py'):
        print("❌ Error: app.py not found. Please run this script from the ElderCare directory.")
        return
    
    # Step 2: Check Git status
    print("\n📋 Checking Git status...")
    git_status = run_command("git status --porcelain", "Checking Git status")
    
    if git_status:
        print("📝 Changes detected. Committing...")
        run_command("git add .", "Adding files to Git")
        run_command('git commit -m "Auto-deploy: Update ElderCare survey"', "Committing changes")
    
    # Step 3: Check if remote repository exists
    print("\n🌐 Checking for GitHub remote...")
    remote_url = run_command("git remote get-url origin", "Getting remote URL")
    
    if not remote_url:
        print("\n📝 No GitHub repository found. Let's create one!")
        print("Please follow these steps:")
        print("1. Go to https://github.com/new")
        print("2. Create a new repository named 'eldercare-survey'")
        print("3. Don't initialize with README (we already have files)")
        print("4. Copy the repository URL")
        
        repo_url = input("\nEnter your GitHub repository URL (e.g., https://github.com/username/eldercare-survey.git): ").strip()
        
        if repo_url:
            run_command(f"git remote add origin {repo_url}", "Adding GitHub remote")
            run_command("git branch -M main", "Setting main branch")
            run_command("git push -u origin main", "Pushing to GitHub")
        else:
            print("❌ No repository URL provided. Please create a GitHub repository first.")
            return
    else:
        print(f"✅ GitHub repository found: {remote_url}")
        run_command("git push", "Pushing latest changes")
    
    # Step 4: Deploy to Render
    print("\n🎯 Deploying to Render...")
    print("Please follow these steps:")
    print("1. Go to https://render.com")
    print("2. Sign up or log in")
    print("3. Click 'New +' → 'Web Service'")
    print("4. Connect your GitHub account")
    print("5. Select your 'eldercare-survey' repository")
    print("6. Configure the service:")
    print("   - Name: eldercare-survey")
    print("   - Build Command: pip install -r requirements.txt")
    print("   - Start Command: python app.py")
    print("   - Plan: Free")
    print("7. Click 'Create Web Service'")
    
    # Open Render in browser
    print("\n🌐 Opening Render in your browser...")
    webbrowser.open("https://render.com")
    
    print("\n⏳ Waiting for deployment...")
    print("Once deployed, your survey will be available at:")
    print("https://eldercare-survey.onrender.com")
    print("\n✅ No passcode required - anyone can access it!")
    
    # Wait for user confirmation
    input("\nPress Enter when you've completed the Render setup...")
    
    print("\n🎉 Deployment completed!")
    print("Your ElderCare survey is now live and accessible worldwide!")
    print("Share this URL with anyone: https://eldercare-survey.onrender.com")

if __name__ == "__main__":
    main() 