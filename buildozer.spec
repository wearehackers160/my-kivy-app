[app]

title = Result Checker
package.name = resultchecker
package.domain = org.school

source.dir = .
source.include_exts = py,kv,png,jpg,ttf,wav,mp3,ogg

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 1

android.minapi = 21
android.api = 34
android.ndk = 25b

android.archs = arm64-v8a,armeabi-v7a

android.permissions = INTERNET, VIBRATE

android.accept_sdk_license = True

log_level = 2
warn_on_root = 1
