---
title: "Training: Git Basics for New Team Members"
description: "Hands-on training module covering Git fundamentals and branch workflow"
author: "Infrastructure Team"
created: 2026-03-26
updated: 2026-03-26
status: approved
tags: [training, git, onboarding]
---

# Training: Git Basics for New Team Members

| Field                   | Value                                        |
| ----------------------- | -------------------------------------------- |
| **Audience**            | Junior developers — beginner level           |
| **Duration**            | 2 hours                                      |
| **Prerequisites**       | Computer with internet, GitHub account       |
| **Learning Objectives** | Clone repos, commit changes, create PRs      |

---

## Lesson 1: Git Fundamentals

### Concepts

- **Repository (repo):** A folder tracked by Git. Contains your code + full history.
- **Commit:** A snapshot of changes. Each commit has a unique hash (e.g., `a1b2c3d`).
- **Remote:** The server copy of your repo (e.g., GitHub). Local is your machine.

### Hands-on Lab

**Step 1: Clone a repository**

```bash
git clone https://github.com/your-org/sample-project.git
cd sample-project
```

Expected result: Directory `sample-project/` created with `.git/` folder inside.

**Step 2: Make a change and commit**

```bash
echo "Hello from $(whoami)" >> contributors.md
git add contributors.md
git commit -m "Add my name to contributors"
```

Expected result:

```text
[main abc1234] Add my name to contributors
 1 file changed, 1 insertion(+)
```

**Step 3: Push to remote**

```bash
git push origin main
```

Expected result: Changes visible on GitHub.

### Knowledge Check

- [ ] Learner can explain the difference between local and remote
- [ ] Learner completed clone + commit + push successfully

---

## Lesson 2: Branch Workflow

### Concepts

- **Branch:** A parallel version of the code. `main` is the default branch.
- **Merge:** Combining changes from one branch into another.
- **Pull Request (PR):** A request to merge your branch. Reviewed by teammates.

### Hands-on Lab

**Step 1: Create a feature branch**

```bash
git checkout -b feature/add-readme-section
```

Expected result:

```text
Switched to a new branch 'feature/add-readme-section'
```

**Step 2: Make changes and push branch**

```bash
echo "## New Section" >> README.md
git add README.md
git commit -m "Add new section to README"
git push -u origin feature/add-readme-section
```

Expected result: Branch appears on GitHub with "Compare & pull request" button.

**Step 3: Create a Pull Request**

1. Go to GitHub repository page
2. Click "Compare & pull request"
3. Add title: "Add new section to README"
4. Add description explaining the change
5. Click "Create pull request"

Expected result: PR created with green "Open" status.

### Knowledge Check

- [ ] Learner can create a branch and switch to it
- [ ] Learner can push a branch and create a PR
- [ ] Learner understands why PRs are used (code review)

---

## Assessment

| Criteria        | Pass Condition                    |
| --------------- | --------------------------------- |
| Lab completion  | 100% steps completed successfully |
| Knowledge check | Can explain branch workflow        |
| Practical demo  | Create PR independently           |

---

## Troubleshooting

### Error: "Permission denied (publickey)"

**Cause:** SSH key not configured for GitHub.

**Fix:**

```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
cat ~/.ssh/id_ed25519.pub
# Copy output → GitHub Settings → SSH Keys → New SSH Key
```

### Error: "Updates were rejected"

**Cause:** Remote has changes you don't have locally.

**Fix:**

```bash
git pull --rebase origin main
git push origin main
```

---

## Next Steps

- Git Advanced: Rebasing and Cherry-pick — *coming soon*
- [Google Workspace New User Guide](../guides/how-to/google-workspace-new-user.md)
