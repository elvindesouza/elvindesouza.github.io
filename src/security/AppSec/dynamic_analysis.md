---
title: "Dynamic Code Analysis"
permalink: /security/appsec/dynamicanalysis
---

**[~](../../../README.md)**

**[~/Security](../../security.md)**

**[~/Security/Appsec](../appsec.md)**

---

* TOC
{:toc}

---

# Dynamic Code Analysis

Dynamic code analysis involves running code and examining the outcome, which also entails testing possible execution paths of the code.

# Main Advantages

- providing visibility of issues before code hits production
- actually runs the code, so can provide time-for-execution, resource usage, log errors occuring during testing, and report vulnerabilities that may have been found during the testing process

# Main Disadvantages

- if the code doesn't run, it isn't tested. Checking for dead code can be done with various [Static Analysis](static_analysis.md) tools
- poor rules lead to poor results. analysis is only as good as the rules, and often the "automation" is taken for granted, making it completely pointless

# Software Testing


# Automate Dynamic Analysis

## Incorporate it into your project

Use automated testing to check integrations, interfaces, performance, the operation of specific modules and security. Unit tests, regression tests, API and integration tests, smoke tests, UI and I/O tests, security and vulnerability tests, stress tests, and acceptance tests.

## Incorporate it into CI/CD

Use something like Github Actions to perform dynamic analysis before code goes live. Here you can configure automated actions for:

- [Security Issues](https://github.com/marketplace?category=security&type=actions)
- [Code Quality](https://github.com/marketplace?category=code-quality&type=actions)
- [Code Review](https://github.com/marketplace?category=code-review&type=actions)
- [Software Composition Analysis/Dependency Scanning](https://github.com/marketplace?category=dependency-management&type=actions)
- [Testing](https://github.com/marketplace?category=testing&type=actions)

_wip_
