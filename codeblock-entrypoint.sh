#!/bin/bash

export MODE=codeblock
. /entrypoint.sh

/opt/conda/bin/python $@ 
