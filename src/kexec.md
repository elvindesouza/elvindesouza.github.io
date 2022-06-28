---
title: "kexec-booting into a new kernel"
permalink: /security/kexec
---

# kexec

from the [manpage](https://linux.die.net/man/8/kexec),

> kexec is a system call that enables you to load and boot into another kernel from the currently running kernel.

> kexec performs the function of the boot loader from within the kernel

There are two steps,

1. loading a new kernel
2. rebooting into the new kernel(preferably gracefully)

To load the kernel,

```
kexec  [-l (--load) kernel-image [--append=command-line-options] [--reuse-cmdline][--initrd=initrd-image]
        ]
 [-u  (--unload)]
 [-e  (--exec)]

where kernel-image is the kernel file
initrd is the initial ramdisk
```

A simple "reboot" for an archlinux system can be

`# kexec -l /boot/vmlinuz-linux --initrd=/boot/initramfs-linux.img --reuse-cmdline && sudo systemctl kexec`

where `systemctl kexec` would terminate services and shutdown gracefully

## Scope of a physical attack?

This highlights the importance of [Physical Security](https://en.wikipedia.org/wiki/Physical_security).
This system call lets you bypass the BIOS password and bootloader on UNIX-like systems. This is ripe for physical attacks and perpetrators who want to carry out an attack (persistent) on many systems from the inside while remaining relatively undetected.

An attacker wanting to set up exfil/C&C the easy way can just bring along a flash drive containing a linux environment and applications, scripts, tools of their choosing, and `kexec` into it. A familiar environment now lies before them, and they can carry out attacks from this system and remain undetected, and unperturbed by firewalls and other gateway-facing measures.

## Prevention?

1. disable the root account
2. principle of least privilege, [here is a quick rundown](https://elvindsouza.github.io/hardening/#least-privilege) on implementation, from a project of mine
3. physical security measures
4. manage hubs and disable unused USB/SATA ports from the BIOS
5. set up firewall rules to account for these kinds of attacks from systems on the local network
