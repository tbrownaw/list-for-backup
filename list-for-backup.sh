#!/bin/bash
set -e

pushd "$(dirname "$(which "$0")")" >/dev/null
DIR="$(pwd)"
popd >/dev/null

. "$DIR/env/bin/activate"

python3 "$DIR/list-for-backup.py" "$@"
