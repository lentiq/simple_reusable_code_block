#!/bin/bash

export MODE=codeblock
#initialize the environment
. /entrypoint.sh

/opt/conda/bin/python $@ 
