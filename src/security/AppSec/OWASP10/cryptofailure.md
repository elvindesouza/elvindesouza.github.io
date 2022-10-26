---
title: "Cryptographic Failures"
permalink: /security/appsec/owasp10/cryptographic_failures
---

**[~](../../../../README.md)**

**[~/Security](../../../security.md)**

**[~/Security/Appsec](../0application-security.md)**

**[~/Security/Appsec/OWASP10](../OWASP10.md)**

---

* TOC
{:toc}

---

Cryptography isn't used as it's intended to. Use modern cryptographic algorithms.

NVD-(US) National Vulnerability Database-statistics in chart form too! Perform a search for cryptographic Vulnerabilities. 

Not all data must be encrypted. A choice needs to be made-data classification policy. Categorize regulated data.

*GRC*
- GDPR
- HIPAA
- CCPA

For each category, list the data applicable, and the requirements.

## Key Management
Don't store keys with the data(most convenient, least secure). Encryption key management. Access control & logging for keys. Rotate keys.
Hash functions are vulnerable to brute-force attacks. Make use of salting.
