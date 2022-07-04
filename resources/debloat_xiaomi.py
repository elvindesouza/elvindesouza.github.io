from time import sleep
from subprocess import run

"""
    Requires adb on $PATH, and (USB) debugging enabled
    Debloat a XIAOMI/MIUI Android phone running Android 9/10/11
    This should be your base benchmark for a Xiaomi device

    WILL REMOVE ALL GOOGLE APPS AND SERVICES
    WILL REMOVE ALMOST ALL XIAOMI APPS AND SERVICES
"""

disable = [
    "com.mi.android.globalminusscreen",
    "com.miui.global.packageinstaller",
    "com.android.thememanager",
    "com.xiaomi.account",
    "com.miui.android.fashiongallery",
    "com.google.android.gms",
    "com.google.android.gsf",
]

uninstall = [
    "cn.wps.xiaomi.abroad.lite",
    "code.name.monkey.retromusic",
    "com.android.bookmarkprovider",
    "com.android.browser",
    "com.android.calendar",
    "com.android.chrome",
    "com.android.dreams.basic",
    "com.android.dreams.phototable",
    "com.android.email",
    "com.android.hotwordenrollment.okgoogle",
    "com.android.hotwordenrollment.xgoogle",
    "com.android.providers.calendar",
    "com.android.soundrecorder",
    "com.android.vending",
    "com.android.wallpaper.livepicker",
    "com.android.wallpaperbackup",
    "com.autonavi.minimap",
    "com.bsp.catchlog",
    "com.caf.fmradio",
    "com.dsi.ant.server",
    "com.duokan.phone.remotecontroller",
    "com.duokan.phone.remotecontroller.peel.plugin",
    "com.facebook.appmanager",
    "com.facebook.katana",
    "com.facebook.services",
    "com.facebook.system",
    "com.google.android.apps.docs",
    "com.google.android.apps.googleassistant",
    "com.google.android.apps.maps",
    "com.google.android.apps.messaging",
    "com.google.android.apps.nbu.paisa.user",
    "com.google.android.apps.photos",
    "com.google.android.apps.subscriptions.red",
    "com.google.android.apps.tachyon",
    "com.google.android.apps.wellbeing",
    "com.google.android.contacts",
    "com.google.android.dialer",
    "com.google.android.feedback",
    "com.google.android.gm",
    "com.google.android.gms",
    "com.google.android.gms.location.history",
    "com.google.android.googlequicksearchbox",
    "com.google.android.gsf",
    "com.google.android.inputmethod.latin",
    "com.google.android.marvin.talkback",
    "com.google.android.music",
    "com.google.android.projection.gearhead",
    "com.google.android.syncadapters.calendar",
    "com.google.android.syncadapters.contacts",
    "com.google.android.talk",
    "com.google.android.tts",
    "com.google.android.videos",
    "com.google.android.youtube",
    "com.google.ar.lens",
    "com.hampusolsson.abstruct",
    "com.huaqin.diaglogger",
    "com.mfashiongallery.emag",
    "com.mi.android.globalFileexplorer",
    "com.mi.android.globalpersonalassistant",
    "com.mi.global.bbs",
    "com.mi.global.shop",
    "com.mi.globalbrowser",
    "com.mi.webkit.core",
    "com.milink.service",
    "com.mipay.wallet.id",
    "com.mipay.wallet.in",
    "com.miui.analytics",
    "com.miui.android.fashiongallery",
    "com.miui.antispam",
    "com.miui.backup",
    "com.miui.bugreport",
    "com.miui.calculator",
    "com.miui.cleanmaster",
    "com.miui.cloudbackup",
    "com.miui.cloudservice",
    "com.miui.cloudservice.sysbase",
    "com.miui.compass",
    "com.miui.documentsuioverlay",
    "com.miui.fm",
    "com.miui.fmservice",
    "com.miui.gallery",
    "com.miui.hybrid",
    "com.miui.hybrid.accessory",
    "com.miui.klo.bugreport",
    "com.miui.micloudsync",
    "com.miui.miservice",
    "com.miui.mishare.connectivity",
    "com.miui.miwallpaper",
    "com.miui.msa.global",
    "com.miui.newmidrive",
    "com.miui.notes",
    "com.miui.phrase",
    "com.miui.player",
    "com.miui.providers.weather",
    "com.miui.qr",
    "com.miui.screenrecorder",
    "com.miui.touchassistant",
    "com.miui.translation.kingsoft",
    "com.miui.translation.youdao",
    "com.miui.translationservice",
    "com.miui.videoplayer",
    "com.miui.virtualsim",
    "com.miui.weather2",
    "com.miui.wmsvc",
    "com.miui.yellowpage",
    "com.netflix.mediaclient",
    "com.netflix.partner.activation",
    "com.opera.app.news",
    "com.opera.branding",
    "com.opera.branding.news",
    "com.opera.mini.native",
    "com.opera.preinstall",
    "com.samsung.aasaservice",
    "com.swiftkey.languageprovider",
    "com.swiftkey.swiftkeyconfigurator",
    "com.syberia.SyberiaPapers",
    "com.syberia.ota",
    "com.tencent.soter.soterserver",
    "com.xiaomi.account",
    "com.xiaomi.calendar",
    "com.xiaomi.discover",
    "com.xiaomi.glgm",
    "com.xiaomi.joyose",
    "com.xiaomi.location.fused",
    "com.xiaomi.mi_connect_service",
    "com.xiaomi.micloud.sdk",
    "com.xiaomi.midrop",
    "com.xiaomi.mipicks",
    "com.xiaomi.miplay_client",
    "com.xiaomi.mircs",
    "com.xiaomi.mirecycle",
    "com.xiaomi.oversea.ecom",
    "com.xiaomi.payment",
    "com.xiaomi.scanner",
    "com.xiaomi.simactivate.service",
    "com.xiaomi.xmsf",
    "com.xiaomi.xmsfkeeper",
    "in.amazon.mShop.android.shopping",
    "org.lineageos.recorder",
    "org.lineageos.snap",
    "org.simalliance.openmobileapi.service",
    "pl.zdunex25.updater",
    "ros.ota.updater",
    "com.mint.keyboard",
    "com.android.contacts",
    "com.android.mms",
    "com.android.providers.downloads.ui",
    "com.android.deskclock",
]

# DO NOT UNINSTALL THESE
# "com.miui.securitycenter",
# "com.miui.securityadd",

sleep(5)
for app in disable:
    run(["adb", "shell", "pm", "disable-user", f"{app}"])

for app in uninstall:
    ps = run(
        ["adb", "shell", "pm", "uninstall", "--user", "0", f"{app}"],
        capture_output=True,
        encoding="utf-8",
    )
    print(ps.stdout, end="")
    if "-1000" in ps.stdout:
        print(f"Couldnt uninstall {app}\n")

# com.android.chrome | Chrome Browser (you may loose webview)
# com.android.deskclock | Stock Clock app
# com.mi.android.globalFileexplorer| Mi File Manager
# com.mi.android.globallauncher | POCO Launcher
# com.mi.globalbrowser | Mi Browser
# com.mipay.wallet.in | Mi Wallet (India)
# com.miui.analytics | MIUI Analytics (spyware)
# com.miui.backup | Backup app
# com.miui.bugreport | Bug reporting app
# com.miui.calculator | Mi Calculator
# com.miui.cloudbackup | Cloud Backup service
# com.miui.cloudservice | Cloud service
# com.miui.micloudsync | Cloud Sync
# com.miui.cloudservice.sysbase | Cloud service
# com.miui.freeform | MIUI Picture in Picture service
# com.miui.touchassistant | Quick Ball feature
# com.miui.videoplayer | MIUI Video player
# com.miui.weather2 | Weather app
# com.miui.yellowpage | Yellow Page app
# com.xiaomi.account | Mi Account
# com.xiaomi.mirecycle | Mi Recycle (MIUI Security)
# com.xiaomi.misettings | Mi Settings
# com.xiaomi.scanner | Scanner app
# com.tencent.soter.soterserver | Chinese Payment service
