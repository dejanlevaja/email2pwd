#!/usr/bin/env python
__author__ = "Dejan Levaja"
__license__ = "GPL"
__version__ = "0.1"

import sys
import time
import argparse
import codecs

year = str(time.localtime().tm_year)
pwds_all = []
pwds = []



def passgen_words(words):
    # original
    pwds.append('.'.join(words))
    # join all
    pwds.append(''.join(words))
    # capitalize
    caps = [x.capitalize() for x in words]
    pwds.append(''.join(caps))
    pwds.append('.'.join(caps))
    # per word
    for word in words:
        pwds.append(word.capitalize())
        pwds.append(word.upper())
        pwds.append(word+year)
        pwds.append(word.capitalize()+year)
        pwds.append(word.capitalize()+str(int(year)-1))
        pwds.append(word+'123')
        pwds.append(word+'123456')
        pwds.append(word.capitalize()+'123')
        pwds.append(word.capitalize()+'123456')
    


def passgen_domain(domain):
    pwds.append(domain)
    pwds.append(domain.upper())
    pwds.append(domain.capitalize())
    pwds.append(domain+'123')
    pwds.append(domain+'123456')
    pwds.append(domain+year)
    pwds.append(domain+str(int(year)-1))



def separator(email):
    if '@' in email:
        raw = email.split('@')
        domain = ((raw[1]).split('.'))[0]
        passgen_domain(domain)
        if '.' in raw[0]:
            words = raw[0].split('.')
            passgen_words(words)
        else:
            words = [raw[0]]
            passgen_words(words)
            
            

def write_pwds(passwords):
    if common:
        with codecs.open(common, encoding='utf-8') as c:
            com = c.readlines()
        for rec in com:
            passwords.append(rec.strip())
            
    if not output:
        for rec in passwords:
            print rec
    else:
        print '[!] Writing passwords to "%s"' % output
        with codecs.open(output, 'w', encoding = 'utf-8') as f:
            for rec in passwords:
                f.write(rec+'\n')
                


def write_special(email, passwords):
    if common:
        with codecs.open(common, encoding='utf-8') as c:
            com = c.readlines()
        for rec in com:
            passwords.append(rec.strip())
    
    fname = email+'.txt'
    print '[!] Writing passwords to "%s"' % fname
    with codecs.open(fname, 'w', encoding = 'utf-8') as f:
        for rec in passwords:
            f.write(rec+'\n')



def main():
    print '\n**** email2pwd ****\n'
    with codecs.open(input,  encoding='utf-8') as f:
        emails = f.readlines()
        
    for email in emails:
        separator(email.strip().lower())
        passwords_special = sorted(set(pwds))
        pwds_all.extend(passwords_special)
        del pwds[:]
        
        if special:
            write_special(email.strip(), passwords_special)
            
    write_pwds(pwds_all)
    
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'email2pwd is a simple password generator')
    parser.add_argument('-e','--emails', help = 'Txt file containing emails', required = True)
    parser.add_argument('-c','--common', help = 'File containing list of common passwords', required = False)
    parser.add_argument('-o','--output', help = 'File to wtite generated passwords to. If omitted, pwds are written to STDOUT', required = False)
    parser.add_argument('-s','--special', help = 'For each email passwords are written to a separate file', required=False, action = 'store_true')
    args = vars(parser.parse_args())
    
    if args['emails']:
        input = args['emails']
    if args['common']:
        common = args['common']
    else:
        common = False
    if args['output']:
        output = args['output']
    else:
        output = False
    if args['special']:
        special = True
    else:
        special = False
        
    main()
    print '\n[!] Done! '
    sys.exit()
