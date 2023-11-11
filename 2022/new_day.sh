#!/bin/bash

unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     machine=Linux;;
    Darwin*)    machine=Mac;;
    CYGWIN*)    machine=Cygwin;;
    MINGW*)     machine=MinGw;;
    *)          machine="UNKNOWN:${unameOut}"
esac

DAY=$1

if [[ -z $DAY ]]; then
    echo "Need to specify a day."
else
    if [[ -f $DAY.jl ]]; then
	    echo "File $DAY.jl already exists."
    else
	    cp template.jl $DAY.jl
        if [[ ${machine} == "Mac" ]]; then
	    sed -i '' -e "s/DAY/${DAY}/" $DAY.jl
        else
            sed -i "s/DAY/${DAY}/" $DAY.jl
        fi
        if [[ -f $DAY.txt ]]; then
            echo "File $DAY.txt already exists."
        else
            touch input_$DAY.txt
        fi
    	echo "New day ($DAY.jl) template created."
    fi
    
    if [[ -f $DAY.py ]]; then
	echo "File $DAY.py already exists."
    else
	    cp template.py $DAY.py
        if [[ ${machine} == "Mac" ]]; then
	    sed -i '' -e "s/DAY/${DAY}/" $DAY.py
        else
            sed -i "s/DAY/${DAY}/" $DAY.py
        fi
	    echo "New day ($DAY.py) template created."
    fi
fi
