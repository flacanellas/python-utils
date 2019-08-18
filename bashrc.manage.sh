# Python Utilities repo
# Author: Federico Cañellas
# Email: federico.leandro.c@gmail.com
# Date: 17-08-2019
# Version: 0.1

# VARIABLES AT PARENT BASH FILE
# $py_utils Path to this directory

#################################################
# Copy files to this local directory 
function _pyu_add {
    for argv in "$@"
    do
        [[ -e "$argv" ]] && [[ ! -e "$py_utils/$argv" ]] && \
	cp -fr "$argv" "$py_utils/$argv"
    done
}
alias py-utils:add='_pyu_add'

# Copy and push new file to this repo
# $1 Commit message
# $2+ Files to push
function _pyu_push {
    commit_msg="$1"
    shift

    while (( "$#" ))
    do
	_pyu_add "$1"
	pushd "$py_utils" > /dev/null

	[[ ! -n $(git status -s "$1" | grep "[AM]") ]] && \
	git add "$1"
	popd > /dev/null
        shift
    done
    
    pushd "$py_utils" > /dev/null
    if [[ -n $(git status -s | grep "[AM]") ]]
    then
        git commit -m "${commit_msg}" && git push && popd > /dev/null
    else
        popd > /dev/null
    fi
}
#################################################
