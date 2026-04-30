def solution(letter):
    
    # list_letter = list(letter)
    letter1 = ''
    letter1 = letter
    letter1.replace('.-','a')
    letter1.replace('-...','b')
    letter1.replace('-.-.','c')
    letter1.replace('-..','d')
    letter1.replace('.','e')
    letter1.replace('..-.','f')
    letter1.replace('--.','g')
    letter1.replace('....','h')
    letter1.replace('..','i')
    letter1.replace('.---','j')
    letter1.replace('-.-','k')
    letter1.replace('.-..','l')
    letter1.replace('--','m')
    letter1.replace('-.','n')
    letter1.replace('---','o')
    letter1.replace('.--.','p')
    letter1.replace('--.-','q')
    letter1.replace('.-.','r')
    letter1.replace('...','s')
    letter1.replace('-','t')
    letter1.replace('..-','u')
    letter1.replace('...-','v')
    letter1.replace('.--','w')
    letter1.replace('-..-','x')
    letter1.replace('-.--','y')
    letter1.replace('--..','z')
    
    letter2 = letter1
    return letter2

morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}

