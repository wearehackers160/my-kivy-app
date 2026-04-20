[app]

title = Result Checker
package.name = resultchecker
package.domain = org.school.result

source.dir = .
source.include_exts = py,png,jpg,kv,mp3,ogg,wav,atlas

version = 0.1

# IMPORTANT: pin versions for compatibility
requirements = python3,kivy==2.0.0,kivymd,pillow

orientation = portrait
fullscreen = 0

# Permissions
android.permissions = INTERNET,VIBRATE

# API settings (safe combo)
android.api = 33
android.minapi = 21

# REMOVE deprecated sdk line (this was causing warning)
# android.sdk = 20  ❌ REMOVE THIS

# NDK (let buildozer manage it OR use stable one)
android.ndk = 25b

# Architectures
android.archs = arm64-v8a, armeabi-v7a

# Fix common build issues
android.allow_backup = True
android.copy_libs = 1

# Use stable python-for-android branch
p4a.branch = stable

[buildozer]

log_level = 2
warn_on_root = 1
