---
title: "Static Code Analysis"
permalink: /security/appsec/staticanalysis
---

**[~](../../../README.md)**

**[~/Security](../../security.md)**

**[~/Security/Appsec](0application-security.md)**

---

* TOC
{:toc}

---

# Static Code Analysis

Static Code Analysis (also known as Source Code Analysis) is usually performed as part of a Code Review (also known as white-box testing) and is carried out at the Implementation phase of a Security Development Lifecycle (SDL)

Scales Well (Can be run on lots of software, and can be repeatedly (like in nightly builds))

For things that such tools can automatically find with high confidence, such as buffer overflows, SQL Injection Flaws, etc. they are great.

# Main Advantages

- analyzes source code without executing it, it always terminates
- finishes execution faster than dynamic analysis
- automate-
  - maintaining code quality
  - finding bugs early
  - find security vulnerabilities early
- easy to incoporate into projects

# Types of static analysis

- codestyle
- security linting
- error detection
- UML creation
- code duplication detection
- complexity analysis
- secrets detection
- comment style analysis
- dead coe detectio
- framework best practices

# Static Analysis with Python

**covered [here](secure_coding_python.md)**

# Automate Static Analysis

## Incorporate it into your project

Most popular static analysis tools have plug-ins for popular IDEs, and run against open files, project files, or workspace files

![](img/prospector.png)
_pass in your prospector args in Visual Studio Code_

## Incorporate it into CI/CD

Use something like Github Actions to perform static analysis before code goes live. Here you can configure automated actions for:

- [Security Issues](https://github.com/marketplace?category=security&type=actions)
- [Code Quality](https://github.com/marketplace?category=code-quality&type=actions)
- [Code Review](https://github.com/marketplace?category=code-review&type=actions)
- [Software Composition Analysis/Dependency Scanning](https://github.com/marketplace?category=dependency-management&type=actions)
- [Testing](https://github.com/marketplace?category=testing&type=actions)

_fin_
