[app]

title = Result Checker
package.name = resultchecker
package.domain = org.school.result

source.dir = .
source.include_exts = py,kv,png,jpg,ttf,mp3,ogg

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 1

# =========================
# ANDROID CONFIG (IMPORTANT)
# =========================

android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

# 🔥 CRITICAL FIX
android.build_tools_version = 33.0.2

android.archs = arm64-v8a, armeabi-v7a
android.permissions = INTERNET, VIBRATE

# =========================
# BUILD SETTINGS
# =========================

log_level = 2
warn_on_root = 1
