#!/bin/bash
git add .
MESSAGE="solve: leetcode $(date +'%y/%m/%d')"
echo $MESSAGE
git commit -m "${MESSAGE}"
git push origin main