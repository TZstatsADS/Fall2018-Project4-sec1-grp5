## positional bniary ngram: 2 grams


# ### build ground truth matrix
# 
# ground_truth_matrix = matrix(0,nrow = 26, ncol = 26)
# 
# colnames(ground_truth_matrix) = letters
# 
# rownames(ground_truth_matrix) = letters
# 
# ### orc file matrix
# 
# orc_matrix = matrix(0,nrow = 26, ncol = 26)
# 
# colnames(orc_matrix ) = letters
# 
# rownames(orc_matrix ) = letters


## position of binary words

binary_gram = function(word){
  
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



## detect error

error_detect = function(word){
  orc_position = binary_gram(word)
  row = nrow(orc_position)
  
  if(sum(ground_truth_matrix[orc_position]) != sum(rep(1,row))){
    return (FALSE)
  }
  else {return(TRUE)}
}

#### test when length of word is 5


ground_truth_matrix[binary_gram(dic[nchar(dic)==5])] = 1

s = sapply(tes[nchar(tes)==5],error_detect)

orc = dict$dictionary[nchar(dict$dictionary)>=2]

truth = dict_tesseract$dictionary[nchar(dict_tesseract$dictionary)>=2]



############### for all words in orc txt

error_detect_txt = function(orc,truth){
  
  result = c()
  
  # orc_df = data.frame(orc = as.character(orc),length = nchar(orc))
  # truth_df = data.frame(truth = as.character(truth),length = nchar(truth))
  
  for (i in unique(nchar(orc))){
  
    ### build ground truth matrix
    
    ground_truth_matrix = matrix(0,nrow = 26, ncol = 26)
    
    colnames(ground_truth_matrix) = letters
    
    rownames(ground_truth_matrix) = letters
    
    ground_truth_matrix[binary_gram(truth[nchar(truth)==i])] = 1
    
    result = c(result,sapply(orc[nchar(orc)==i],error_detect))
  }
  return(result)
  
}
