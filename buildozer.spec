[app]

title = Result Checker
package.name = resultchecker
package.domain = org.school

source.dir = .
source.include_exts = py,kv,png,jpg,kv,ttf,wav,mp3,ogg

version = 1.0

requirements = python3,kivy,kivy_deps.sdl2,kivy_deps.glew

orientation = portrait
fullscreen = 1

# =========================
# ANDROID SETTINGS
# =========================

android.minapi = 21
android.api = 33
android.ndk = 25b

android.archs = arm64-v8a, armeabi-v7a

android.permissions = INTERNET,VIBRATE

log_level = 2
warn_on_root = 1
