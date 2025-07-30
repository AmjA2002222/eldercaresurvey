#!/usr/bin/env python3
"""
Force Render Redeployment Script
"""

import subprocess
import webbrowser
import time

def main():
    print("🚀 Force Render Redeployment")
    print("=" * 40)
    
    # Create a timestamp file to force deployment
    timestamp = time.strftime('%Y%m%d_%H%M%S')
    with open('render_deploy_trigger.txt', 'w') as f:
        f.write(f"Deploy trigger: {timestamp}")
    
    print("✅ Created deployment trigger")
    
    # Add and commit
    subprocess.run("git add render_deploy_trigger.txt", shell=True)
    subprocess.run(f'git commit -m "Force Render redeploy - {timestamp}"', shell=True)
    subprocess.run("git push", shell=True)
    
    print("✅ Pushed to GitHub")
    print("⏳ Render will automatically redeploy in 1-2 minutes")
    
    # Open the survey
    print("\n🔗 Opening your survey...")
    webbrowser.open("https://eldercare-survey-1.onrender.com")
    
    print("\n📋 What to expect:")
    print("1. Render will detect the new commit")
    print("2. Automatic deployment will start")
    print("3. Wait 2-3 minutes for completion")
    print("4. New questions will appear:")
    print("   - Question 11: Social connections")
    print("   - Question 12: Loneliness")
    
    print(f"\n⏰ Deployment started at: {time.strftime('%H:%M:%S')}")
    print("Check Render dashboard for status: https://dashboard.render.com")

if __name__ == "__main__":
    main() 