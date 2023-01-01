---
title: "Threat Modeling"
permalink: /security/appsec/threat-modeling
---

**[~](../../../README.md)**

**[~/Security](../../security.md)**

**[~/Security/Appsec](0application-security.md)**

---

* TOC
{:toc}

---

# Threat Modeling

Written while completing the **Threat Modeling Skills course by Adam Shostack**, on LinkedIn Learning

[Certificate of Completion](https://www.linkedin.com/learning/certificates/9c11efd851ef6cf49e2dc2383d738e781f43f6844504c929ba024cd148ae10a5?u=126888530)

## Four-Question Framework

1. What are we working on?(Assess Scope)
2. What can go wrong?(Identify what can go wrong)
3. What are we going to do about it?(Identify countermeasures/perform risk management)
4. Did we do a good job?(Assess Work)

## Steps

### Decompose the Application

- how the application will be used and how it will react with external components
- (data) entry points
- (data) exit points
- assets
- trust levels

### Determining and Ranking Threats using STRIDE

>threat categorization

>help identify threats from the attacker and

- spoofing(authentication)
- tampering(integrity)
- repudiation(non-repudiation)
- information disclosure(confidentiality)
- denial of service(availability)
- elevation of privilege(authorization)

```
risk=P(threat)*cost
```

Create a threat tree diagram

### Risk Management

once the possible impact is identified, the associated risks can be-

- accept
- eliminate
- mitigate
