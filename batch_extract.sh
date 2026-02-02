#!/bin/bash

mkdir -p frames

for f in *.mp4 *.webm; do
  # make safe name (no spaces/symbols)
  base=$(basename "$f")
  name=$(echo "$base" | sed 's/\.[^.]*$//' | tr -cd '[:alnum:]_')

  mkdir -p "frames/$name"

  ffmpeg -i "$f" -vf fps=2 "frames/$name/frame_%05d.jpg"
done


