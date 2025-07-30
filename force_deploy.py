#!/usr/bin/env python3
"""
Force Deploy Script for ElderCare Survey
"""

import subprocess
import webbrowser
import time

def main():
    print("🚀 Force Deploy ElderCare Survey")
    print("=" * 40)
    
    # Make a small change to force deployment
    with open('deploy_trigger.txt', 'w') as f:
        f.write(f"Last updated: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    print("✅ Created deployment trigger file")
    
    # Add and commit the trigger
    subprocess.run("git add deploy_trigger.txt", shell=True)
    subprocess.run('git commit -m "Force redeploy with new questions"', shell=True)
    subprocess.run("git push", shell=True)
    
    print("✅ Pushed to GitHub")
    
    # Open Render dashboard
    print("🌐 Opening Render Dashboard...")
    webbrowser.open("https://dashboard.render.com")
    
    print("\n📋 Manual Deploy Steps:")
    print("1. Go to your eldercare-survey service")
    print("2. Click 'Manual Deploy' button")
    print("3. Wait for deployment to complete")
    print("4. Check your survey at: https://eldercare-survey-1.onrender.com")
    
    print("\n🔗 Your Survey Links:")
    print("- Survey: https://eldercare-survey-1.onrender.com")
    print("- Database: https://eldercare-survey-1.onrender.com/waiting-list")
    print("- Local: http://localhost:5001")
    
    print("\n✅ New questions should now appear:")
    print("- Question 11: How often do you see your friends and family?")
    print("- Question 12: How often do you feel lonely?")

if __name__ == "__main__":
    main() 