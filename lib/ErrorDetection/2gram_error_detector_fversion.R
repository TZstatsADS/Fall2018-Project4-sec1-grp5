## positional bniary ngram: 2 grams zx2229

## position of binary words

binary_gram = function(word){
  
  if (nchar(word)>1){
    
  word_ch = unlist(strsplit(word,""))
  
  position = matrix(0,ncol = 2, nrow = choose(length(word_ch),2) )
  
  count = 1
  
  for(i in 1:(length(word_ch)-1)){
    
    for(j in (i+1):length(word_ch)){
      
      position[count,] = c(which(letters == word_ch[i]),which(letters == word_ch[j]))
      
      count = count + 1
    }
    
  }
  
  return(position)
  
  }
  
  else{return(NULL)}
  
} 
 

####### detect error zx2229

error_detect = function(orc_word,truth){
  
  if(nchar(orc_word)>1){
  
  orc_position = binary_gram(orc_word)
  
  row = nrow(orc_position)
  
  ground_truth_matrix = ground_truth_dict(orc_word,truth)
  
  if(sum(ground_truth_matrix[orc_position]) != sum(rep(1,row))){
    
    return (FALSE)
  }
  else {return(TRUE)}}
  
  else{return (TRUE)}
}


