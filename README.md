Static Flow Analysis using Semgrep (CI/CD)
Overview

This project demonstrates static code analysis and static flow (taint) analysis using Semgrep, integrated into a GitHub Actions CI/CD pipeline.

The goal is to automatically detect insecure coding practices such as:

Use of eval()

SQL injection vulnerabilities caused by unsafe user input

All checks run automatically whenever code is pushed or a pull request is opened.

What this project does

Uses custom Semgrep rules written in YAML

Scans Python source code (app.py)

Runs Semgrep automatically using GitHub Actions

Fails the CI pipeline if a security issue is found

Prevents insecure code from being merged (when using pull requests)

Project structure
static-flow-analysis/
│
├── app.py
│   └── Sample Python code used to trigger Semgrep rules
│
├── semgrep-rules/
│   ├── eval_rules.yaml
│   │   └── Detects usage of eval()
│   └── sql_injection.yaml
│       └── Detects SQL injection using taint analysis
│
└── .github/workflows/
    └── semgrep.yml
        └── GitHub Actions workflow to run Semgrep

Semgrep rules used
1. Eval detection (pattern-based)

Detects any use of eval(...)

Marked as ERROR

Causes the CI pipeline to fail

2. SQL Injection detection (taint-based)

Source: input(...)

Sink: execute(...)

Tracks unsafe data flow from user input into SQL execution

Flags SQL injection vulnerabilities

How CI/CD works in this project

Code is pushed to GitHub or a pull request is opened

GitHub Actions triggers the Semgrep workflow

Semgrep scans all tracked files

If a rule with severity: ERROR matches:

❌ Workflow fails

❌ Pull request merge is blocked

If no issues are found:

✅ Workflow passes

✅ Code can be merged

Example vulnerable code (for testing)
user_id = input("Enter user id: ")
query = "SELECT * FROM users WHERE id = " + user_id
cursor.execute(query)


This code triggers the SQL injection taint rule.

How to fix issues

Remove eval() usage

Use parameterized SQL queries, for example:

cursor.execute(
    "SELECT * FROM users WHERE id = ?",
    (user_id,)
)


After fixing the code and pushing again, the CI pipeline will pass.

Why this project is useful

Demonstrates real-world CI/CD security enforcement

Shows how static analysis can prevent vulnerabilities early

Works without running Semgrep locally (useful for Windows users)

Uses industry-standard tools and workflows

Tools used

Python

Semgrep

GitHub Actions

GitHub (Pull Requests & CI)

Summary

This project shows how static flow analysis can be automated using Semgrep and enforced through CI/CD, ensuring insecure code never reaches the main branch.
