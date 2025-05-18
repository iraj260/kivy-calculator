
[app]
title = calculator
package.name = calculator
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1

[android]
title = calculator
package.name = calculator
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0
android.permissions = INTERNET

log_level = 2
warn_on_root = 1

android.sdk = 24
android.ndk = 23b
android.api = 30
android.build_tools_version = 30.0.3
# این قسمت می‌تونه برای آیکون سفارشی استفاده بشه:
# icon.filename = %(source.dir)s/icon.png
# این قسمت می‌تونه برای آیکون سفارشی استفاده بشه:
# icon.filename = %(source.dir)s/icon.png
