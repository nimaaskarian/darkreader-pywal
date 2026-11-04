# darkreader-pywal
this fork exists only to have the feature of getting color values from a native
messaging host. 

an example of this can be found in [this native messaging host](theme_sync.py)
and its [manifest](org.darkreader.theme_sync.json). copy the manifest to
`~/.config/chromium/NativeMessagingHosts/` or `~/.mozilla/native-messaging-hosts/`.

note that for using this as an unloaded chromium extension, you should put `"allowed_origins": ["chrome-extension://<that-id>/"]` in the manifest.
