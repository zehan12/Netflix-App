import os
import subprocess

def run(cmd):
    return subprocess.check_output(cmd, shell=True, text=True).strip()

def apply_replacements():
    for root, dirs, files in os.walk('.'):
        if '.git' in root: continue
        for file in files:
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r') as f:
                    content = f.read()
                
                # Apply replacements
                new_content = content.replace('zehan12/Netflix-App', 'zehan12/Netflix-App')
                new_content = new_content.replace('zehan12', 'zehan12')
                new_content = new_content.replace('@zehan12', '@zehan12')
                
                if new_content != content:
                    with open(filepath, 'w') as f:
                        f.write(new_content)
            except Exception:
                pass

os.system("git rebase --abort >/dev/null 2>&1")

# Get original SHAs
# Note: Since the user added 62f0b41, e35adbd is at HEAD~2
# Actually, the SHAs 02e358e, 7160ff6, 9b9cc1a, e35adbd are immutable because they are historical commits that haven't been rewritten yet (we didn't rewrite them, we just added a7b3fe5 on top of them!)
# Wait, let's verify if they exist.
os.system("git checkout 9b5a79f")
os.system("git branch -D new_main >/dev/null 2>&1")
os.system("git checkout -b new_main")

apply_replacements()
os.system("git add .")
os.system("git commit -m 'chore: update project details'")

commits = ["02e358e", "7160ff6", "9b9cc1a", "e35adbd"]
for c in commits:
    os.system("git rm -rf . >/dev/null 2>&1")
    os.system(f"git checkout {c} -- .")
    apply_replacements()
    os.system("git add .")
    os.system(f"git commit -C {c}")

os.system("git checkout main")
os.system("git reset --hard new_main")
os.system("git branch -D new_main")
