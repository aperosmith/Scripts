# ~/.bashrc: executed by bash(1) for non-login shells.

# Note: PS1 and umask are already set in /etc/profile. You should not
# need this unless you want different defaults for root.
# PS1='${debian_chroot:+($debian_chroot)}\h:\w\$ '
# umask 022

# You may uncomment the following lines if you want `ls' to be colorized:
# export LS_OPTIONS='--color=auto'
# eval "`dircolors`"
# alias ls='ls $LS_OPTIONS'
# alias ll='ls $LS_OPTIONS -l'
# alias l='ls $LS_OPTIONS -lA'
#
# Some more alias to avoid making mistakes:
# alias rm='rm -i'
# alias cp='cp -i'
# alias mv='mv -i'


#-------------------------------------------------------------
# Global Variables
#-------------------------------------------------------------

# Do echo after each command
export PROMPT_COMMAND=''

# Path
export PATH=/usr/bin:/bin:/usr/sbin:/sbin
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
export PATH=~/bin:$PATH

# Personal folders
export web=/var/www/html
export logs=/var/log

#-------------------------------------------------------------
# Text and colors
#-------------------------------------------------------------

# Shell colors
export TERM=xterm-color
export CLICOLOR=1
export LS_COLORS='GxFxCxDxBxegedabagaced'


# Colors
export White='\e[1;37m'
export Black='\e[0;30m'
export Blue='\e[0;34m'
export Green='\e[0;32m'
export Cyan='\e[0;36m'
export Red='\e[0;31m'
export Purple='\e[0;35m'
export Brown='\e[0;33m'
export Yellow='\e[1;33m'
export Grey='\e[0;30m'

# Light colors
export LGreen='\e[1;32m'
export LCyan='\e[1;36m'
export LRed='\e[1;31m'
export LPurple='\e[1;35m'
export LGrey='\e[1;30m'
export LBlue='\e[1;34m'

# Reset
export NC='\e[39m' # No Color

# LESS man page colors (makes Man pages more readable).
export LESS_TERMCAP_mb=$'\e[1;32m'
export LESS_TERMCAP_md=$'\e[1;32m'
export LESS_TERMCAP_me=$'\e[0m'
export LESS_TERMCAP_se=$'\e[0m'
export LESS_TERMCAP_so=$'\e[01;33m'
export LESS_TERMCAP_ue=$'\e[0m'
export LESS_TERMCAP_us=$'\e[1;4;31m'

#-------------------------------------------------------------
# Alias
#-------------------------------------------------------------

alias l='ls -AF'                # Sort by hidden files and show info
alias ll='ls -AFg'              # Sort by hidden file
alias lk='ls -AFgSr'            # Sort by size, biggest last.
alias lt='ls -AFgtr'            # Sort by date, most recent last.
alias lc='ls -ltcr'             # Sort by/show change time,most recent last.
alias lu='ls -ltur'             # Sort by/show access time,most recent last.
alias lr='ls -RAl'              # Recursive ls show hidden files and info

alias sizes='du -m --max-depth 1 | sort -rn'   # List all directories and sort by size

alias cp='cp -v'                        # Copy vebose mode
alias cpr='cp -v -r'            # Copy a directory verbose
alias mv='mv -v -f'             # Move vebose
alias rm='rm -v -f'             # Remove verbose without asking
alias rmr='rm -v -r -f'         # Remove directory verbose

cd() { builtin cd "$@"; ls; }               # Always list directory contents upon 'cd'
alias cd..='cd ../'                         # Go back 1 directory level (for fast typers)
alias ..='cd ../'                           # Go back 1 directory level
alias ...='cd ../../'                       # Go back 2 directory levels
alias .3='cd ../../../'                     # Go back 3 directory levels
alias .4='cd ../../../../'                  # Go back 4 directory levels
alias .5='cd ../../../../../'               # Go back 5 directory levels
alias .6='cd ../../../../../../'            # Go back 6 directory levels

alias f='open -a Finder ./'                 # f:            Opens current directory in MacOS Finder

alias k='kill $!'       # Kill lhe last process opened

alias c='clear'         # Clear the screen

alias root='sudo -i'    # Root shell

zipf () { zip -r "$1".zip "$1" ; }          # zipf:         To create a ZIP archive of a folder

alias numFiles='echo $(ls -1 | wc -l)'      # numFiles:     Count of non-hidden files in current dir
alias make1mb='mkfile 1m ./1MB.dat'         # make1mb:      Creates a file of 1mb size (all zeros)
alias make5mb='mkfile 5m ./5MB.dat'         # make5mb:      Creates a file of 5mb size (all zeros)
alias make10mb='mkfile 10m ./10MB.dat'      # make10mb:     Creates a file of 10mb size (all zeros)

alias openPorts='sudo lsof -i | grep LISTEN'        # openPorts:    All listening connections
alias editHosts='sudo nano /etc/hosts'                  # editHosts:        Edit /etc/hosts file


#-------------------------------------------------------------
# Functions
#-------------------------------------------------------------

# Find a file with a pattern in name
function ff() { find . -type f -iname '*'"$*"'*' -ls ; }

# Creates an archive (*.tar.gz) from given directory.
function maketar() { tar cvzf "${1%%/}.tar.gz"  "${1%%/}/"; }

# Create a ZIP archive of a file or folder.
function makezip() { zip -r "${1%%/}.zip" "$1" ; }

# Make your directories and files access rights sane.
function sanitize() { chmod -R u=rwX,g=rX,o= "$@" ;}

# Calculates the gzip compression of a file
function gzipsize(){
         echo $((`gzip -c $1 | wc -c`/1024))"KB"
}

# rename all the files which contain uppercase letters to lowercase in the current folder
function filestolower(){
  read -p "This will rename all the files and directories to lowercase in the current folder, continue? [y/n]: " letsdothis
  if [ "$letsdothis" = "y" ] || [ "$letsdothis" = "Y" ]; then
    for x in `ls`
      do
      skip=false
      if [ -d $x ]; then
        read -p "'$x' is a folder, rename it? [y/n]: " renamedir
        if [ "$renamedir" = "n" ] || [ "$renameDir" = "N" ]; then
          skip=true
        fi
      fi
      if [ "$skip" == "false" ]; then
        lc=`echo $x  | tr '[A-Z]' '[a-z]'`
        if [ $lc != $x ]; then
          echo "renaming $x -> $lc"
          mv $x $lc
        fi
      fi
    done
  fi
}


# Create standard .sh file
function msh()
{
    if [ "$1" ]; then
        if [ ! -f "$1.sh" ]; then
            printf "${Green}Creating ${NC}$1\n"
            echo "#!/bin/bash" > $1
            echo "# " >> $1
            chmod +x $1
            nano $1
        else
            printf "${Green}File already exist.\n"
        fi
    else
        printf "${Green}Give me a filename.\n"
    fi
}


#-------------------------------------------------------------
# Prompt
#-------------------------------------------------------------

whoami=$(whoami)

# If id command returns zero, you have root access.
if [ $(id -u) -eq 0 ]; then
    # Root
    PS1="${TITLEBAR}${LGrey} [${Red}root${Green} \w${LGrey}]${NC} "
else
    # Normal
    PS1="${TITLEBAR}${LGrey} [${Yellow}${whoami}${Green} \w${LGrey}]${NC} "
fi
