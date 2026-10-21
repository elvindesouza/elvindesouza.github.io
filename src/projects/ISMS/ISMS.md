---
title: "ISMS (WIP)"
permalink: /security/isms
---

* TOC
{:toc}

---

# ISMS (WIP)


Idea: invent a 60-person company.

## Phase 1

Complete **Information Security Management System** implementation

- scope and context of the organization
- information security policy
- Statement of Applicability covering all 93 controls: Write a full SoA justifying why specific Annex A controls were selected or excluded.
- Risk Assessment Methodology
- Risk Assessment Matrix: evaluating risks based on Asset, Threat, and Vulnerability (Likelihood vs. Impact scoring); risk register with risk treatment plans
- Few core procedures: (Information Security Policy, Access Control Policy, Acceptable Use Policy, and Incident Response Plan mapped directly to ISO 27001:2022 Annex A controls)
- A small internal audit and a management review summary


## Phase 2

At the end, I can do a BSI IT-Grundschutz check- A basis Absicherung

https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/it-grundschutz_node.html

https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/WIBA/Weg_in_die_Basis_Absicherung_WiBA_node.html

## Phase 3

Map ISO 27001 controls to Grundschutz Bausteine. List which of my documents cover each item.

## Phase 4

This fictional company creates an application.

Create a **GDPR** compliance package:
- Data Protection Impact Assessment (Art. 35)
- Record of Processing Activities (ROPA / Verzeichnis von Verarbeitungstätigkeiten)(Art. 30)
- Technical and organizational measures/Privacy-by-Design Technical Implementation (Art. 32)
- data subject request procedure (access, deletion)- explicit consent management, automated user data export (Data Portability - Art. 20), and an automated "Right to be Forgotten" (Erasure - Art. 17)

## Phase 5

**Compliance as code**

Run an automated hardening scan (Lynis or OpenSCAP) on a Linux lab VM, map each finding to ISO 27001 controls and Grundschutz requirements, and show a before-and-after report. 

Configure a GitHub Actions or GitLab CI/CD pipeline using policy engine tools (e.g., Open Policy Agent, Trivy, or Checkov) to scan IaC (Terraform/Ansible) and containers for security misconfigurations.
