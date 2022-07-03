---
title: "Android"
permalink: /pages/android
---

<!-- debloat/degoogle xiaomi/android -->
<!-- termux, vnc, applications -->
<!-- ssh, ftp -->
<!-- encryption, privacy&security(separate .md under ~/security) -->

## Termux

1. install the `openssh` package, and the public/private ed25529 keypair will be created automatically

2. run the SSH daemon with `sshd`

3. run `passwd` to set a new password

4. run `whoami` to get your username

5. connect to the server from a client

   > Default SSH port in Termux is 8022

You may also [setup storage](https://wiki.termux.com/wiki/Internal_and_external_storage), and then can access it through SFTP

from the wiki,

> Termux is not FHS compliant.
