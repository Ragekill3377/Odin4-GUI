#!/bin/bash
# Odin4 install, any linux system.

ODIN_BINARY="odin4"


if [[ $EUID -ne 0 ]]; then
   echo "Use sudo or root to run this." 
   exit 1
fi

if command -v odin4 &> /dev/null; then
    if odin4 -h &> /dev/null; then
        echo "Odin4 already installed. You can directly run python script."
        exit 0
    fi
fi

if [[ ! -f ./$ODIN_BINARY ]]; then
    echo "Error: $ODIN_BINARY not found in the current directory."
    exit 1
fi


chmod +x ./$ODIN_BINARY


mv ./$ODIN_BINARY /usr/local/bin/


if [[ $? -ne 0 ]]; then
    echo "[INSTALLER]: Failed. Couldn't move odin4 to /usr/local/bin."
    exit 1
fi

echo "[INSTALLER]: Success."
