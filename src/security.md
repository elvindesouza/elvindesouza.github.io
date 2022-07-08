---
title: "~/Security"
permalink: /security/
---

# [~](../README.md)

---

# Security

## [Appliation Security Section](security/appsec.md)

> Application security (short AppSec) includes all tasks that introduce a secure software development life cycle to development teams. Its final goal is to improve security practices and, through that, to find, fix and preferably prevent security issues within applications.

Exploring Web application security, OWASP, and tooling(SAST, DAST, static and dynamic analyzers, codestyle and standards)

Also leaning into DevSecOps, which is the seamless integration of security testing and protection throughout the software development and deployment lifecycle

## [Network Security Section](security/networking.md)

Networking basics-Routers(and setup), switches, identifying devices on a local network, troubleshooting, ICMP, IP addressing, MAC addressing, DNS, nslookup, DNSSEC and OCSP, etc.

Discussing common diagnostic and security tools like `ping`, `netstat`, `ss`, `hping`, `traceroute`, `arp`

Also delving into how the Web works, the HTTP Request/Response Cycle, HTTP headers, and session keys, cookies

## [GnuPG-The free implementation of the OpenPGP standard and using GPG-GUI](security/gnupg.md)

The [free](https://www.gnu.org/philosophy/free-sw.en.html) implementation of the OpenPGP standard. File and message encryption with GnuPG. Different types of encryption-symmetric and asymmetric, along with [GPG-GUI](https://elvindesouza.github.io/GPG-GUI/), a front-end to GnuPG written in Python

Also exploring creating and verifying signatures on files or messages

## [Microsoft Windows Operating System Security](security/MSWindowsSecurity/windows.md)

Microsoft Windows Operating System administration, maintenance, architecture, and security fundamentals

## [GNU/Linux Operating System Security](security/LinuxSecurity/linux.md)

Administration and maintenance of the GNU/Linux operating system, common security tools and security aspects

## [The kexec system call and scope of a physical attack](projects/kexec.md)

Using the kexec Linux system call to load a kernel of choice, and perform an attack with scripting in a more familiar environment

## [SSH setup and secure configuration](security/ssh.md)

> operate securely over an unsecured network
> remote shell login, but any network service can be secured with SSH

Covers key generation, public key authentication, intrusion prevention, X11 forwarding, etc.

## [Android Security](security/android.md)

Security related apps and tools available for Android

Android hardening and de-bloating, setting up Termux for SSH/SFTP and FTP access

## [Using the Nessus vulnerability scanner](https://elvindesouza.github.io/NetworkPenetrationTesting/#nessus)

Using the Nessus vulnerability scanner, creating reports, and addressing vulnerabilities

## [Secure Coding Practices and Introduction to Application Security](security/AppSec/secure_coding.md)

A set of practices that applies security considerations to how software will be coded and encrypted to best defend against a cyber attack or vulnerabilities.

## [Secure Python Development](security/AppSec/secure_coding_python.md)

Tools and guidelines to follow when developing projects in Python, to make them less vulnerable and insecure

Covers codestyle, module structure guidelines, security tools to check python code, tests with Python, formatters and standardization, and type hinting along with type checking to scan for issues.

## [Static Code Analysis](security/AppSec/static_analysis.md)

Static Code Analysis (also known as Source Code Analysis) is usually performed as part of a Code Review (also known as white-box testing) and is carried out at the Implementation phase of a Security Development Lifecycle (SDL)

## [Networking Basics](security/networking/networking_basix.md)

Routers(and setup), switches, identifying devices on a local network, troubleshooting, ICMP, using the `ping` utility

The OSI and TCP/IP Models, packet capture with Wireshark

## [IP addressing](security/networking/ip_addressing.md)

IP addresses-public and private, LAN, subnetting, DHCP servers

MAC addresses, ARP and ARP spoofing

## [DNS, nslookup, DNSSEC and OCSP](security/networking/dns.md)

Exploring the Domain Name System, using `nslookup`, DNS cache poisoning, DNSSEC and OCSP stapling

<!-- dnsenum -->

## [How the Web Works, HTTP Request/Response Cycle](security/networking/web.md)

HTTP/HTTPS-methods, status codes, URLs, tracking a GET request and the response

Also talking briefly about HTTP headers, and session keys, cookies

## [netstat](security/networking/netstat_linux.html)

Exploring netstat, and how we could use this as a diagnostic tool when troubleshooting or monitoring networks

## [hping3](security/networking/hping3.html)

Setting up a DoS attack on a system or network, and experimenting with additional modes with hping

## [traceroute](security/networking/traceroute.html)

Using the traceroute utility to inspect the route of a packet sent across networks. Additionally, covers how we could use this as a diagnostic tool

<!-- ## [DevTools](devtools.md) -->
<!--
## Enumerating Network Services
## Exploiting Network Services
## [Wireshark](wireshark.md)
## Active Directory
## GNU/Linux Operating System Security -->

<!-- virtualization,setup, security (virtualization.md)  -->
<!-- # Threat & Vulnerability management -->

<!-- ## MITRE, MITRE ATT&CK
## Yara
## ISAC
## OpenVAS
## MISP
# SO & Monitoring
---
-->
