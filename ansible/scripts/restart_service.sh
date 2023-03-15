#!/bin/bash
python -m http.server >/dev/null 2>&1 &
echo $! > process_pidfile
