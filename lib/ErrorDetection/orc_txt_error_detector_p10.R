#### ground truth dictionary zx2229

ground_truth_dict = function(orc_word,truth){
  
  if((nchar(orc_word)>1) == TRUE){
    
  word_length = nchar(orc_word)
  
  ground_truth_matrix = matrix(0,nrow = 26, ncol = 26)
  
  colnames(ground_truth_matrix)=letters
  
  rownames(ground_truth_matrix) = letters
  
  for (word in truth[nchar(truth)==word_length]){
    
    pos_truth = binary_gram(word)
    
    ground_truth_matrix[pos_truth] = 1
  }
  
  return(ground_truth_matrix)}
  
  else {return(ground_truth_matrix = matrix(0,nrow = 26, ncol = 26))}
  
  
}

############### for all words in orc txt



error_detect_txt = function(orc,truth){
  
   word_list = c()
  
   for (word in orc){
     
     if((nchar(word)>1)==TRUE){
     #ground_truth_matrix = ground_truth_dict(word,truth)
     
     if_wrong = error_detect(word,truth)
     
      word_list = c(word_list,list(c(word,if_wrong)))
     
     }
     
     else {word_list = list.append(word_list,c(word,TRUE))}}
     
    return (word_list )
     
 }
    











neighbor_words = function(orc,truth){
  
  word_list = error_detect_txt(orc,truth)
  
  word_list = c(rep("*",4),word_list,rep("*",4))
  
  for(i in 5:(length(word_list)-4)){
    #& i <= (length(word_list) - 4) & i >= 5#
    if(word_list[[i]][2]==FALSE)
      {
      
      word_list[[i]] = list.append(word_list[[i]], word_list[[i-4]][1],word_list[[i-3]][1],word_list[[i-2]][1],
                                   word_list[[i-1]][1],word_list[[i+1]][1],word_list[[i+2]][1],word_list[[i+3]][1],
                                   word_list[[i+4]][1],truth[[i]])
    }
    
    else{ word_list[[i]] = list.append(word_list[[i]],rep(0,8),truth[[i]])}
    
   
  
  }
  word_list = word_list[-c(1:4,(length(word_list)-3):length(word_list))]
  return(word_list)
}







