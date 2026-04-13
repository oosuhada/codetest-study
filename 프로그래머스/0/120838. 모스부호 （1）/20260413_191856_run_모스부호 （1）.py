def solution(letter):
    
    # list_letter = list(letter)
    letter1 = letter
    
    letter1 = letter1.replace('.-','a')
    letter1 = letter1.replace('-...','b')
    letter1 = letter1.replace('-.-.','c')
    letter1 = letter1.replace('-..','d')
    letter1 = letter1.replace('.','e')
    letter1 = letter1.replace('..-.','f')
    letter1 = letter1.replace('--.','g')
    letter1 = letter1.replace('....','h')
    letter1 = letter1.replace('..','i')
    letter1 = letter1.replace('.---','j')
    letter1 = letter1.replace('-.-','k')
    letter1 = letter1.replace('.-..','l')
    letter1 = letter1.replace('--','m')
    letter1 = letter1.replace('-.','n')
    letter1 = letter1.replace('---','o')
    letter1 = letter1.replace('.--.','p')
    letter1 = letter1.replace('--.-','q')
    letter1 = letter1.replace('.-.','r')
    letter1 = letter1.replace('...','s')
    letter1 = letter1.replace('-','t')
    letter1 = letter1.replace('..-','u')
    letter1 = letter1.replace('...-','v')
    letter1 = letter1.replace('.--','w')
    letter1 = letter1.replace('-..-','x')
    letter1 = letter1.replace('-.--','y')
    letter1 = letter1.replace('--..','z')
    
    return letter1

morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}


# letter1.replace('.-','a') -> 변환된 문자열을 반환만 하고, letter1 자체는 바뀌지 않음
# letter1 = letter1.replace('.-','a') -> 결과값을 다시 넣어줘야 함
