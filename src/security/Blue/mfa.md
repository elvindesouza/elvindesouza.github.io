# Multi-Factor Authentication

A list of websites and services offering MFA is available [here](https://2fa.directory/)

_"Combine a thing you can forget with a thing you can lose"_

## SMS 2FA

SMS 2FA is better than nothing, but should not be used when better alternatives are available. Not only is SMS not end-to-end encrypted, but SMS 2FA is a target for phishing

## TOTP

A universal standard that any authenticator app can handle, can be done offline, can make backups, etc. As of 2023, you should be using this.

On smartphones, the QR code provided, which is just a visual representation of the string/seed, and can be scanned

FreeOTP provides implementations of HOTP (RFC 4226) and TOTP (RFC 6238). FreeOTP+ is a fork of FreeOTP

You can use the app offline, and backup(!) your seeds in case you want to switch devies.

Android(F-Droid): https://f-droid.org/en/packages/org.liberty.android.freeotpplus/

## Hardware security keys

A YubiKey can be pricey and for most of the general population, not suit their use case.

