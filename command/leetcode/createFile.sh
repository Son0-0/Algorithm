#!/bin/bash

if [ $# -eq 3 ]

then

    difficulty=$1
    problem=$2
    lang=$3

    echo "solving leetcode difficulty=$difficulty problem=$problem lang=$lang"

    if [ "$lang" = "go" ]

    then

        cp ./template/template.go ./leetcode/"$difficulty"/"$problem.go"

        echo "create $problem.go file"
    
    elif [ "$lang" = "py" ]

    then 

        cp ./template/template.py ./leetcode/"$difficulty"/"$problem.py"

        echo "create $problem.py file"

    elif [ "$lang" = "cpp" ]

    then

        cp ./template/template.cpp ./leetcode/"$difficulty"/"$problem.cpp"

        echo "create $problem.cpp file"

    else

        echo "Unexpected Language"
    
    fi

else
    echo "Not enough parameter passed"

fi