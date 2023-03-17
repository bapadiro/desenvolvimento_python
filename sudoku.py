
enquanto haCasasEmBranco(sudoku):
    pega uma casa em branco
    resp = tentaColocarNumero(sudoku, casa, num)
    if resp == True:
       guarda na pilha essa casa 
       e vai para a proxima
    else:
       volta para casa anterior
       limpa o numero do jogo do sudoku
       tenta colocar outro numero nessa 
       casa    
    