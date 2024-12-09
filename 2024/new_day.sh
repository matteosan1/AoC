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
            touch input_${DAY}_prova.txt
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

    if [[ -f aoc_2023/src/day$DAY.rs ]]; then
	echo "File day$DAY.rs already eists."
    else
	cp template.rs aoc_2023/src/day$DAY.rs
	cp template_main.rs aoc_2023/src/main.rs
	if [[ ${machine} == "Mac" ]]; then
	    sed -i '' -e "s/DAY/${DAY}/g" aoc_2023/src/day$DAY.rs
	    sed -i '' -e "s/DAY/${DAY}/g" aoc_2023/src/main.rs
        else
            sed -i "s/DAY/${DAY}/g" aoc_2023/src/day$DAY.rs
	    sed -i "s/DAY/${DAY}/g" aoc_2023/src/main.rs
        fi

	echo "New day ($DAY.rs) template created."
    fi
fi
