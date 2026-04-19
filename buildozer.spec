[app]

# (str) Application title
title = Result Checker

# (str) Package name (no spaces, no caps)
package.name = resultchecker

# (str) Package domain
package.domain = org.school

# (str) Source folder
source.dir = .

# (list) Files to include
source.include_exts = py,wav,mp3,ogg,png,jpg,kv

# (str) App version
version = 1.0

# (list) Requirements
requirements = python3,kivy

# =========================
# ANDROID CONFIG
# =========================

# Minimum Android version (4.4.4 = API 19)
android.minapi = 21

# Target Android version (modern stable)
android.api = 33

# Build tools version
android.build_tools_version = 33.0.2

# Android NDK version
android.ndk = 25b

# Supported CPU architectures (important for all phones)
android.archs = armeabi-v7a, arm64-v8a

# Permissions (minimal safe set)
android.permissions = INTERNET, VIBRATE

# Fullscreen app
fullscreen = 1

# =========================
# AUDIO / FILE SUPPORT
# =========================

# Ensure sound files are included
source.include_patterns = *.py,*.kv,*.wav,*.ogg,*.mp3

# =========================
# OPTIONAL SETTINGS
# =========================

# Orientation
orientation = portrait

# Log level
log_level = 2

# Warn on root
warn_on_root = 1


# =========================
# BUILD SECTION
# =========================

[buildozer]

# Build verbosity
log_level = 2

# Output directory (optional)
# bin_dir = ./bin
