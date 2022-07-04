---
title: "Android"
permalink: /pages/android
---

<!-- security focused settings,tweaks -->

## F-droid

[Website](https://f-droid.org/)

> F-Droid is an installable catalogue of FOSS (Free and Open Source Software) applications for the Android platform. The client makes it easy to browse, install, and keep track of updates on your device

navigate to the downloads page, and download and install the .apk

## Security Tools

[Oversec](https://www.oversec.io/)-privacy for all apps

[Tessercube-Secure Messaging](https://tessercube.com/)

[OpenPGP for Android](https://tesserpg.com/)

[DroidFS](https://f-droid.org/en/packages/sushi.hardcore.droidfs/)-access your encrypted filesystems on Android

[KeePassXC](https://keepassxc.org/docs/) cross-platform password manager, also available for Android on the F-droid store

[Syncthing](https://syncthing.net/) cross-platform folder synchronization application

[OpenKeychain](https://www.openkeychain.org/)- OpenPGP on Android. Encrypt-decrypt files, sign messages and verify signatures

## De-Google and De-Bloat

you may write a script to remove all unnecessary apps(especially those which have no respect for your privacy) from your phone

[example](../resources/debloat_xiaomi.py)

## Termux- setting up SSH/SFTP or FTP

1. install the `openssh` package, and the public/private ed25529 keypair will be created automatically

2. run the SSH daemon with `sshd`

3. run `passwd` to set a new password

4. run `whoami` to get your username

5. connect to the server from a client

   > Default SSH port in Termux is 8022

You may also [setup storage](https://wiki.termux.com/wiki/Internal_and_external_storage), and then can access it through SFTP

Add to your `.bash_profile`-

```
sshd
```

from the wiki,

> Termux is not FHS compliant.

alternatively set up an FTP server and add

```
sv up ftpd
```

to your `.bash_profile`
