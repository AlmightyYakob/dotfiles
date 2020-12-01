#!/bin/bash

# DOESN'T CURRENTLY FILTER SINK PROPERLY
# DEFAULT_SINK=$(pacmd list-sinks | grep "*" | sed -E "s/\s+\* index: (\d+)/\1/")
DEFAULT_SINK=$(pacmd list-sinks | grep "*" | sed -E "s/  \* index: (\d+)/\1/")

echo "$DEFAULT_SINK"

if [ "$1" == "up"  ]; then
    pactl set-sink-volume $DEFAULT_SINK +5%
fi

if [ "$1" == "down"  ]; then
    pactl set-sink-volume $DEFAULT_SINK -5%
fi



