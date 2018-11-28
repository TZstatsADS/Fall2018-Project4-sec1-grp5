
intersect_number<-function(a,b){
  ta<-data.frame(table(a))
  tb<-data.frame(table(b))
  mt<-merge(ta,tb,by.x = "a",by.y = "b")
  mt$min_freq<-apply(mt[,c(2,3)],1,min)
  return(sum(mt$min_freq))
}

#input: a row with a truth word and a prediction word
compare_word<-function(bi_words){
  if(nchar(bi_words[1])==0 |nchar(bi_words[2])==0 ){
    return(0)
  }else{
    a<-strsplit(bi_words[1],split="")[[1]]
    b<-strsplit(bi_words[2],split="")[[1]]
    return(intersect_number(a,b))
  }
}
############try#######################################


gt<-paste(ground_truth[[1]],collapse = " ")
gt<-strsplit(gt,split = " ")[[1]]#convert a ground_truth to a vector

ot<-paste(orc_txt[[1]],collapse = " ")
ot<-strsplit(ot,split = " ")[[1]]#convert a ground_truth to a vector

example1<-cbind(gt,ot)

rt<-apply(example1,1,compare_word)#
sum(rt)/sum(nchar(gt))#ratio of correct with ground_truth
sum(rt)/sum(nchar(ot))#ratio of correct with ORC output

