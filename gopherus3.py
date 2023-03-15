#!/usr/bin/env python3
import argparse
import sys
sys.path.insert(0, './scripts/')
from scripts import FastCGI, MySQL, PostgreSQL, DumpMemcached, PHPMemcached, PyMemcached, RbMemcached, Redis, SMTP, Zabbix


class colors:
    reset='\033[0m'
    red='\033[31m'
    green='\033[32m'
    orange='\033[33m'
    blue='\033[34m'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--exploit",
                        help="mysql,\n"
                             "postgresql,\n"
                             "fastcgi,\n"
                             "redis,\n"
                             "smtp,\n"
                             "zabbix,\n"
                             "pymemcache,\n"
                             "rbmemcache,\n"
                             "phpmemcache,\n"
                             "dmpmemcache")
    args = parser.parse_args()
    print(colors.green + """
      ________              .__                                ________  
     /  _____/  ____ ______ |  |__   ___________ __ __  ______ \_____  \ 
    /   \  ___ /  _ \\\\____ \|  |  \_/ __ \_  __ \  |  \/  ___/   _(__  < 
    \    \_\  (  <_> )  |_> >   Y  \  ___/|  | \/  |  /\___ \\   /       \\
     \______  /\____/|   __/|___|  /\___  >__|  |____//____  > /______  /
            \/       |__|        \/     \/                 \/         \/ 
    """+ "\n\t\t" + colors.blue + "author: " + colors.orange + "$_SpyD3r_$" + "\n" + colors.reset)

    if(not args.exploit):
        print(parser.print_help())
        sys.exit(1)
    
    if(args.exploit=="mysql"):
        MySQL.MySQL()
    elif(args.exploit=="postgresql"):
        PostgreSQL.PostgreSQL()
    elif(args.exploit=="fastcgi"):
        FastCGI.FastCGI()
    elif(args.exploit=="redis"):
        Redis.Redis()
    elif(args.exploit=="smtp"):
        SMTP.SMTP()
    elif(args.exploit=="zabbix"):
        Zabbix.Zabbix()
    elif(args.exploit=="dmpmemcache"):
        DumpMemcached.DumpMemcached()
    elif(args.exploit=="phpmemcache"):
        PHPMemcached.PHPMemcached()
    elif(args.exploit=="rbmemcache"):
        RbMemcached.RbMemcached()
    elif(args.exploit=="pymemcache"):
        PyMemcached.PyMemcached()
    else:
        print(parser.print_help())

if __name__ == "__main__":
    main()