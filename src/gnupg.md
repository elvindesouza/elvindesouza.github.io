---
title: "File Encryption with GPG"
permalink: /security/GPG
---

# Single file encryption with GPG:

There are many ways to encrypt/lock files, folders and drives on Linux. I was looking for a method in which individual files were encrypted, most encryption software talked about online had full-disk encryption and container encryption. Then I realized I already had GPG set up after I stopped using GNU Pass. After completing the GPG key generation again(RSA-RSA 4096, no expiry), I put all the files I wanted to encrypt(documents, important photographs) in a folder and ran

`gpg --encrypt-files <files> -r myadd@email.com`

This encrypted all the files with the .gpg suffix, and deleted the original ones. I could then unencrypt the files(w/the correct credentials) with

`gpg -o filename.ext -d filename.ext.gpg`

(This could easily be scripted with python, but the tediousness was intentional)

You can use symmetric encryption on a file too, with

`gpg -c file`

Decryption for symmetrically encrypted files follows the same process

Symmetric encryption has its advantages, and you can feel free to use it with archiving less important data(vacation photos, etc.). Then in this case, you could just use 7zip instead.

The GPG documentation is FANTASTIC, btw

_This is a precursor to my next project, where I create a simple frontend for GPG **asymmetric** encryption, link below_

## [GPG-GUI ](https://elvindsouza.github.io/GPG-GUI/)
