
def get_possible_dencodings(strd):
    if len(strd) < 2:
        return len(strd)
    return get_possible_decodings_h(strd)
   
def get_possible_decodings_h(strd):
    if len(strd) < 2:
        return 1
    acomulated = get_possible_decodings_h(strd[1:])
    val = int(strd[:2])
    if val < 27 :
        acomulated += get_possible_decodings_h(strd[2:])
    return acomulated
    
print(get_possible_dencodings('1111'))
