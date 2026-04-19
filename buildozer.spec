[app]

# =========================
# BASIC APP INFO
# =========================

title = Result Checker
package.name = resultchecker
package.domain = org.school

source.dir = .
source.include_exts = py,kv,png,jpg,ttf,wav,mp3,ogg

version = 1.0

# =========================
# PYTHON REQUIREMENTS
# =========================

requirements = python3,kivy,kivy_deps.sdl2,kivy_deps.glew

# =========================
# APP SETTINGS
# =========================

orientation = portrait
fullscreen = 1

# =========================
# ANDROID CONFIG (STABLE)
# =========================

android.minapi = 21
android.api = 31
android.ndk = 25b

android.archs = arm64-v8a, armeabi-v7a

android.permissions = INTERNET, VIBRATE

# =========================
# BUILD SETTINGS
# =========================

log_level = 2
warn_on_root = 1

# IMPORTANT: DO NOT set build_tools_version manually
# Let Buildozer handle it automatically
