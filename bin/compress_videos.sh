#!/usr/bin/env bash
# Compress raw research videos into short, silent, web-ready loops (<5 MB each)
# (H.264 MP4 + VP9 WebM) plus a JPEG poster frame.
# Output: assets/video/research/<name>.{mp4,webm} + assets/img/research/<name>_poster.jpg
# Usage: bash bin/compress_videos.sh [clip names...]   (run from repo root; no args = all clips)
set -euo pipefail
cd "$(dirname "$0")/.."
SRC="port stuff"
OUTV="assets/video/research"
OUTP="assets/img/research"
mkdir -p "$OUTV" "$OUTP"

# name | source | start(s) | duration(s) | speed factor | optional crop (w:h:x:y, removes letterbox bars)
CLIPS=(
  "cap_realworld|$SRC/cov_stuff/SingleRobotRealWorldResults.mp4|13|14|1"
  "convoy_decentralized|$SRC/MMPUG Videos-selected/Decentralized Convoy.mp4|22|12|1|1872:1053:0:0"
  "convoy_heterogeneous|$SRC/MMPUG Videos-selected/Heterogenous  Convoy.mp4|2.5|14|1"
  "global_planner_sim|$SRC/MMPUG Videos-selected/Global Planner in Simulation.mov|2.5|26|1.6"
  "global_planner_wheeled|$SRC/MMPUG Videos-selected/Global Planner on Wheeled Robot.mp4|2|18|1.2"
  "legged_local_planner|$SRC/MMPUG Videos-selected/Legged Robot Local Planner.mp4|6|14|1"
  "voxel_perception|$SRC/MMPUG Videos-selected/3D Voxel Grid - Environment Perception.mp4|4|14|1"
  "hil_docking|$SRC/hil_vid_v0.mov|3.6|18|1.2"
  "snake_reaching|$SRC/_review/snake/media3.mp4|0|22|1.3"
  "highspeed_autonomy|$SRC/MMPUG Videos-selected/MMPUG Highspeed  autonomy.mov|14|14|1"
)

for row in "${CLIPS[@]}"; do
  IFS='|' read -r name src start dur speed crop <<<"$row"
  pre=""; [ -n "${crop:-}" ] && pre="crop=$crop,"
  # optional filter: bash bin/compress_videos.sh name1 name2 ...
  if [ "$#" -gt 0 ] && [[ ! " $* " =~ " $name " ]]; then continue; fi
  out="$OUTV/$name.mp4"
  echo ">> $name"
  ffmpeg -v error -y -ss "$start" -t "$dur" -i "$src" -an \
    -vf "${pre}setpts=PTS/$speed,fps=24,scale=1280:-2:flags=lanczos,format=yuv420p" \
    -c:v libx264 -preset slow -crf 24 -profile:v high -movflags +faststart "$out"
  # poster = frame at 40% of the clip (skips title cards at the start)
  pdur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$out")
  pt=$(python3 -c "print(round(float('$pdur')*0.4,2))")
  ffmpeg -v error -y -ss "$pt" -i "$out" -frames:v 1 -q:v 4 "$OUTP/${name}_poster.jpg"
  # WebM (VP9) companion for browsers without H.264
  ffmpeg -v error -y -i "$out" -an -c:v libvpx-vp9 -crf 36 -b:v 0 -row-mt 1 \
    -deadline good -cpu-used 4 "$OUTV/$name.webm"
  sz=$(du -k "$out" | cut -f1)
  if [ "$sz" -gt 4900 ]; then
    echo "   $sz KB > 5 MB, re-encoding at crf 33"
    ffmpeg -v error -y -ss "$start" -t "$dur" -i "$src" -an \
      -vf "${pre}setpts=PTS/$speed,fps=24,scale=854:-2:flags=lanczos,format=yuv420p" \
      -c:v libx264 -preset slow -crf 33 -movflags +faststart "$out"
  fi
  du -h "$out" "$OUTV/$name.webm"
done
