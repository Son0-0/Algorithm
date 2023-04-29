#!/bin/bash

if [ $# -eq 2 ]

then

    difficulty=$1
    problem=$2

    echo "solving leetcode difficulty=$difficulty problem=$problem"

    cp template.go ./leetcode/"$difficulty"/"$problem.go"

    echo "create $problem.go file"


else
    echo "Not enough parameter passed"

fi