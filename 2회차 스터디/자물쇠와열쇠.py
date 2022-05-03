def match_key(block, key, rotate, x, y) :
    
    l_key = len(key)
    
    for i in range(l_key):
        for j in range(l_key):
            if rotate ==0:
                block[x+i][y+j] += key[i][j]
            elif rotate==1:
                block[x+i][y+j] += key[l_key-1 - j][i] #열이 올라(상승)갈수록 행 상승(우측으로)
            elif rotate ==2:
                block[x+i][y+j] += key[l_key - 1 - i] [l_key-1 - j]
            elif rotate == 3:
                block[x+i][y+j] += key[j][l_key-1-i]
                


def check(block, spareblock, l_lock):
    for i in range(l_lock):
        for j in range(l_lock):
            if block[spareblock + i][spareblock+j] !=1:
                return False
            else:
                return True
    

def solution(key, lock) :
    
    l_lock = len(lock)        #몇x몇 사격형인지
    l_key = len(key)          #몇x몇 사격형인지
    
    spareblock = l_key -1
    

    
    for x in range(spareblock + l_key):
        for y in range(spareblock + l_lock):
            for rotate in range(4):
                block =  [ [0] * (l_key*2+l_lock) for _ in range(l_key*2 + l_lock) ] #전체블럭
            
                for i in range(l_lock) :                              #자물쇠
                   for j in range(l_lock) :
                       block[i + spareblock][j+spareblock] = lock[i][j]
                
                match_key(block, key, rotate, x, y)
                
                if ( check(block, spareblock, l_lock) ) :
                    return True
                else:
                    return False
                
                
  