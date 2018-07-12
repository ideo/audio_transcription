### Google Cloud
Follow the instructions in `google_cloud_instructions.md`.

### Audio Data
Edit `make_symlinks.sh` for your directory setup, then run with `source make_symlinks.sh` to access the audio files stored on Dropbox.

### Audiotools Library
Download the [`audiotools`](http://audiotools.sourceforge.net/install.html) package and follow the installation guide.

Audiotools works with `.wav` files by default. In order to support `.m4a` files, install `FAAC` and `FAAD2` with:
* `brew install faac`
* `brew install faad2`

Check Audiotools configurations by running `audiotools-config`. This will list supported types, e.g.:
```
extraction arguments
  Format Readable Writable Default Quality
  ────── ──────── ──────── ───────────────
    aiff      yes      yes
    alac      yes      yes
      au      yes      yes
    flac      yes      yes               8
     m4a      yes      yes             100
     mp2       no       no             192
     mp3       no      yes               2
     ogg       no       no               3
    opus       no       no              10
     tta      yes      yes
     wav      yes      yes
      wv       no       no        standard
```
