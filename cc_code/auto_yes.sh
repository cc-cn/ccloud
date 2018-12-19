#!/bin/bash
passwd=cc123456



expect << EOF

set timeout 5 
spawn ssh -X chencheng@192.168.3.111

expect { 
"yes/no)?"  { send "yes\r";exp_continue }
"assword:"  { send   "$passwd\r" }
}

expect  "Enter file in which to save the key*"
send  "\r"
expect {
 "(y/n)?"  { send  "yes\r";exp_continue }
 "Enter passphrase*"  { send  "\r";exp_continue }
}
interact
EOF
