#!/bin/sh
# Rasterise the exported SVGs. Run from the repo root, after the three
# assets/*.svg have been written by scripts/export_wheels.js.
#
#   brew install librsvg imagemagick
#
# 1600px is large enough for Wikipedia and for print at a sensible size, and
# the PNG8 pass takes each file from ~800KB to ~220KB with no visible loss:
# these are flat colour with no gradients.
set -e
cd "$(dirname "$0")/.."
for f in bhava odalu rasa; do
  rsvg-convert -w 1600 -h 1600 -o "assets/$f.png" "assets/$f.svg"
  magick "assets/$f.png" -strip -colors 256 "PNG8:assets/$f.png"
  echo "assets/$f.png  $(du -h "assets/$f.png" | cut -f1)"
done
