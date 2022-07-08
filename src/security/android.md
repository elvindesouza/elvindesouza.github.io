---
title: "Android"
permalink: /security/android
---

**[~](../../README.md)**

**[~/Security](../security.md)**

---

* TOC
{:toc}

---

<!-- security focused settings,tweaks -->

Android Security and Privacy Controls

# Alternative App Stores

## F-droid

[Website](https://f-droid.org/)

> F-Droid is an installable catalogue of FOSS (Free and Open Source Software) applications for the Android platform. The client makes it easy to browse, install, and keep track of updates on your device

> F-Droid respects your privacy. They don’t track you, or your device.

navigate to the downloads page, and download and install the .apk

## Aurora Store

[Download](https://f-droid.org/packages/com.aurora.store/)

- alternate to Google's Play Store, with an elegant design,
- download apps, update existing apps, search for apps,
- get details about in-app trackers, spoof your location and much more.

# Security Tools

## [Oversec](https://www.oversec.io/)

privacy for all apps

> Eye-to-Eye encryption: Messages are decrypted on-the-fly and only while shown on screen - decrypted text is never stored

> ...features a unique way of encoding encrypted messages. It stores the encrypted text in invisible (zero-width) characters and let's you add decoy text at the end. That way, a message will just show e.g. "The sun is shining today!" with no visible sign of any encryption, whereas in reality it contains a hidden encrypted message.

> encrypt and send photos through Oversec

## [KeePassDX](https://www.keepassdx.com/)

keepass\*-compatible password manager, also available for Android on the F-droid store

> Edit encrypted keys and digital identities in a single KeePass file and fill out forms securely.

## [Syncthing](https://syncthing.net/)

**cross-platform** folder synchronization application

You can also [encrypt shares](https://docs.syncthing.net/users/untrusted.html) with a password.

Encryption is XChaCha20-Poly1305 and AES-SIV with a key derived from the password and folder ID using scrypt.

## [OpenKeychain](https://www.openkeychain.org/)- OpenPGP on Android.

Encrypt-decrypt files, sign messages and verify signatures

importing your OpenPGP private key is incredibly easy, and it can remember your passphrases until you decide to clear them

## [K-9 Mail](https://f-droid.org/en/packages/com.fsck.k9/)

_mail client that_

- supports multiple accounts
- Unified Inbox
- privacy-friendly (no tracking whatsoever, only connects to your email provider)
- automatic background synchronization or push notifications
- local and server-side search
- OpenPGP email encryption (PGP/MIME)

## [Sentry](https://f-droid.org/en/packages/me.lucky.sentry/)

Enforce security policies of your device

_Features_

- limit the maximum number of failed password attempts
- disable USB data connections (Android 12, USB HAL 1.3, Device Owner)

## [AnySoftKeyboard](https://anysoftkeyboard.github.io/)

Free as in speech and Free as in beer.

_Features_

- Supports lots of languages via external packages
- Physical keyboards are supported as well
- Themes (skin) support
- Incognito Mode - will not track your typing
- Word suggestions, and Next-Word suggestions
- Automatic correction can be customized, or turned off entirely. External packages include word lists that can be freely mixed. You can use a French layout and get suggestions for German and Russian!
- Gesture typing
- Dark mode, automatic (based on system) and manual
- Power saving mode, disables various features to save battery
- Per-app tint, the keyboard changes color depending on the app
- Voice input
- Compact modes: Split and Compact to left/right
- Special keyboard for text fields which require only numbers, dates, email or URI addresses.
- Plenty of emojis

and many more

## [Tessercube-Secure Messaging](https://tessercube.com/)

Secure Messaging with end-to-end encryption

## [TesserPG](https://tesserpg.com/)

OpenPGP for Android

## [DroidFS](https://f-droid.org/en/packages/sushi.hardcore.droidfs/)

access your encrypted filesystems on Android

# De-Google and De-Bloat

you may write a script to remove all unnecessary apps(especially those which do not respect your privacy) from your phone

[example](../resources/debloat_xiaomi.py)

Look into custom ROMs for higher security and more control over your device and data. Some are listed below.

## [LineageOS](https://lineageos.org/)

> A free and open-source operating system for various devices, based on the Android mobile platform.

## [GrapheneOS](https://grapheneos.org/)

> GrapheneOS is a privacy and security focused mobile OS with Android app compatibility developed as a non-profit open source project

> ...focused on the research and development of privacy and security technology including substantial improvements to sandboxing, exploit mitigations and the permission model.

# Termux

Terminal emulator for Android

from the wiki,

> Termux is not FHS compliant.

## Setting up SSH/SFTP

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

## Set up FTP

alternatively set up an FTP server and add

```
sv up ftpd
```

to your `.bash_profile`. Default port is 8021.
