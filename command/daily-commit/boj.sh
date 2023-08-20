#!/bin/bash
git add .
MESSAGE="solve: boj $(date +'%y/%m/%d')"
echo $MESSAGE
git commit -m "${MESSAGE}"
git push origin main