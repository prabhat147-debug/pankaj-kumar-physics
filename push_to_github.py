#!/usr/bin/env python3
"""
Er. Pankaj Kumar - GitHub Push & Deployment Helper
Publishes the website to GitHub and sets up GitHub Pages.
"""

import os
import sys
import subprocess
import shutil

# Locate Git executable (check portable MinGit first, then system path)
MINGIT_PATH = r"C:\Users\HP\.gemini\antigravity\bin\mingit\cmd\git.exe"
GIT_BIN = MINGIT_PATH if os.path.exists(MINGIT_PATH) else shutil.which("git") or "git"

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

def run_git(args):
    cmd = [GIT_BIN] + args
    result = subprocess.run(cmd, cwd=PROJECT_DIR, capture_output=True, text=True)
    return result

def main():
    print("=" * 65)
    print("   Er. Pankaj Kumar Physics Mentorship - GitHub Deployment Tool")
    print("=" * 65)
    print(f"Project Directory: {PROJECT_DIR}")
    print(f"Using Git binary:  {GIT_BIN}\n")

    # 1. Initialize Git if not already done
    if not os.path.exists(os.path.join(PROJECT_DIR, ".git")):
        print("[1/4] Initializing Git repository...")
        res = run_git(["init", "-b", "main"])
        if res.returncode != 0:
            run_git(["init"])
            run_git(["branch", "-M", "main"])
    else:
        print("[1/4] Git repository already initialized.")

    # 2. Configure user name & email locally if needed
    run_git(["config", "user.name", "Er. Pankaj Kumar"])
    run_git(["config", "user.email", "pankaj.physics.iitk@gmail.com"])

    # 3. Stage and commit files
    print("[2/4] Staging files and creating commit...")
    run_git(["add", "."])
    commit_res = run_git(["commit", "-m", "Initial commit: Er. Pankaj Kumar Physics Mentorship website"])
    if "nothing to commit" in commit_res.stdout:
        print("      Everything up-to-date in local git.")
    else:
        print("      Files committed successfully.")

    # 4. Check remote
    remotes_res = run_git(["remote", "-v"])
    current_remote = remotes_res.stdout.strip()

    print("\n[3/4] GitHub Remote Configuration")
    if current_remote:
        print(f"Current remote configured:\n{current_remote}\n")
    
    repo_url = None
    if len(sys.argv) > 1:
        repo_url = sys.argv[1]
    else:
        print("Please enter your GitHub repository URL.")
        print("Example: https://github.com/your-username/pankaj-kumar-physics.git")
        print("(Press Enter if you have already configured the remote, or paste URL):")
        try:
            user_input = input("GitHub Repo URL: ").strip()
            if user_input:
                repo_url = user_input
        except EOFError:
            pass

    if repo_url:
        run_git(["remote", "remove", "origin"])
        add_res = run_git(["remote", "add", "origin", repo_url])
        if add_res.returncode == 0:
            print(f"      Remote 'origin' set to: {repo_url}")
        else:
            print(f"      Error setting remote: {add_res.stderr}")

    # 5. Push to GitHub
    print("\n[4/4] Pushing to GitHub (branch: main)...")
    push_res = run_git(["push", "-u", "origin", "main"])
    if push_res.returncode == 0:
        print("\n" + "=" * 65)
        print(" SUCCESS! Your website has been uploaded to GitHub.")
        print("=" * 65)
        print("\nTo activate your free live website via GitHub Pages:")
        print("1. Go to your repository on GitHub.com")
        print("2. Click 'Settings' -> 'Pages' (in left sidebar)")
        print("3. Under 'Build and deployment' -> 'Branch', select 'main' / 'root'")
        print("4. Click 'Save'. Your website will be live in 60 seconds!")
    else:
        print("\nNote: Push output / status:")
        if push_res.stderr:
            print(push_res.stderr)
        if push_res.stdout:
            print(push_res.stdout)
        print("\nIf authentication was required, you can sign in to GitHub using:")
        print(f"cd \"{PROJECT_DIR}\"")
        print(f"\"{GIT_BIN}\" push -u origin main")

if __name__ == "__main__":
    main()
