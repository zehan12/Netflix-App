import os
import sys

filename = sys.argv[1]
with open(filename, 'r') as f:
    lines = f.readlines()

# The format of rebase -i is:
# pick 8fbabda Update README.md
# pick bd20db7 edge runtime
# pick 298f4b8 error.tsx update
# pick 9b5a79f Update README.md
# pick 02e358e Fix: dropdown menu closes when clicked + loading.tsx change
# pick 7160ff6 bug fix for email signup
# pick 9b9cc1a Update README.md
# pick e35adbd bun ci
# pick a7b3fe5 chore: update app details and footer
# pick 62f0b41 feat: add footer credit link to the GitHub repository

# We want to move 'a7b3fe5' to the 5th position (index 4)
new_lines = []
target_line = None
for line in lines:
    if line.startswith('pick ') and 'a7b3fe5' in line:
        target_line = line
    else:
        new_lines.append(line)

if target_line:
    new_lines.insert(4, target_line)

with open(filename, 'w') as f:
    f.writelines(new_lines)
