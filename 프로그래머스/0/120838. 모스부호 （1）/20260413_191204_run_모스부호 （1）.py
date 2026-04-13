def solution(letter):
    
    # list_letter = list(letter)
    letter.replace('.-','a')
    letter.replace('-...','b')
    letter.replace('-.-.','c')
    letter.replace('-..','d')
    letter.replace('.','e')
    letter.replace('..-.','f')
    letter.replace('--.','g')
    letter.replace('....','h')
    letter.replace('..','i')
    letter.replace('.---','j')
    letter.replace('-.-','k')
    letter.replace('.-..','l')
    letter.replace('--','m')
    letter.replace('-.','n')
    letter.replace('---','o')
    letter.replace('.--.','p')
    letter.replace('--.-','q')
    letter.replace('.-.','r')
    letter.replace('...','s')
    letter.replace('-','t')
    letter.replace('..-','u')
    letter.replace('...-','v')
    letter.replace('.--','w')
    letter.replace('-..-','x')
    letter.replace('-.--','y')
    letter.replace('--..','z')
    return letter

morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}

