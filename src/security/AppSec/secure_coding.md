---
title: "Secure Coding Manifesto"
permalink: /security/appsec/securedev
---

# [~](../../../README.md)

# [~/Security](../../security.md)

# [~/Security/Appsec](../appsec.md)

---

_Resources-_

[OWASP](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/migrated_content)

[UC Berkeley](https://security.berkeley.edu/secure-coding-practice-guidelines)

---

1. Keep all secrets out of repos.

   Set up a .gitignore file. If secrets have been pushed to a git repository, assume they have been grabbed. It is very difficult to cover it up, and your best course of action is to invalidate these secrets and request new ones

2. Leave password handling to audited and trusted frameworks and libraries. Follow standards and guidelines for that specific library or encryption type.

3. Try to break your own software.

   Static code analysis, done in a code-review context, is the first and most essential step in developing and maintaining good software. Can also be analyzing code against a ruleset or coding standards. These address vulnerabilities, and code smell.

   Use automated testing to check integrations, interfaces, performance, the operation of specific modules and security. Unit tests, regression tests, API and integration tests, smoke tests, UI and I/O tests, security and vulnerability tests, stress tests, and acceptance tests.

   [Analysis Tools](https://analysis-tools.dev/)

   [Dynamic Analysis Tools](https://github.com/analysis-tools-dev/dynamic-analysis)

   **Static Application Security testing** to test code quality and scan for security issues.

   **Dynamic Application Security testing** performs a black-box test, reporting vulnerabilities by actually performing attacks

   Check for known vulnerablities in dependencies. GitHub offers functions to check and notify you of known vulnerabilities in dependencies in your projects.

   Automate **vulnerability scanning**

   A subset of this is to try to break your own security.

4. Be open to security audits. [Security through obscurity is not an answer](https://www.pearsonitcertification.com/articles/article.aspx?p=2218577&seqNum=7#:~:text=Security%20through%20obscurity%20means%20that,trusted%20people%20from%20seeing%20it.)

   [Related](https://danielmiessler.com/study/security-by-obscurity/#goodbad)

5. Any thing the user touches is assumed to be evil by default. Uploaded files, any user input, requests

   Do not give attackers namespaces to explore.

6. Make sure you are not open to SQL injections. Database data exposure==org going under, as fines get larger. It is far too easy to check for injectable areas and SQLi vulnerabilities now that it isn't an excuse.

7. Never trust your supply chain or third party vendors. Have a no trust policy with their products and services.

   [Supply Chain Vulnerability](https://www.techtarget.com/searcherp/definition/supply-chain-security)

   [NIST-Best Practices in Cyber Supply Chain Risk Management](https://csrc.nist.gov/CSRC/media/Projects/Supply-Chain-Risk-Management/documents/briefings/Workshop-Brief-on-Cyber-Supply-Chain-Best-Practices.pdf)

8. Minimize exposure in the first place, and follow [hardening](https://elvindesouza.github.io/hardening/) practices. Keep as few services exposed to the internet or networks as possible. If you must have them, use strong authentication, and detective(logging)+preventive(DoS prevention, proxy,etc.) measures.

9. Follow the principle of [Least Privilege](https://elvindesouza.github.io/hardening/#least-privilege)

---
