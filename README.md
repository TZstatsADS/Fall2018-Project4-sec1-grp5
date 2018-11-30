# Project: OCR (Optical Character Recognition) 

![image](figs/intro.png)

### [Full Project Description](doc/project4_desc.md)

Term: Fall 2018

+ Team #5
+ Team members
	+ Chen, Jannie mc4398
	+ Chen, Sizhu sc4248
	+ Li, Yunfan yl3838
	+ Xu, Zhengyang zx2229
	+ Yu, Chenghao cy2475

+ Project summary: In this project, we created an OCR post-processing procedure to enhance Tesseract OCR output. We understood and discussed the assigned paper D2 and C2, for the detection algorithm and correction algorithm separately. For D2, the detection part, 2-gram was adopted to detect the word errors and we figured out the former 4 words and the latter 4 words of the detected word. For C2, at first found correction candidates by Damerau Levenshtein distance ascendingly. Then six functions were defined to calculate the feature scores for each candidate correction words. Finally, an AdaBoost model was applied to regress the labels on the six feature scores. The candidate correction word with highest probability will be chosen to replace the wrong word. The evaluation part contains the word-wise evaluation and character-wise evaluation. After post-processing, the recall and precision increases a lot especially in word level. 
	
**Contribution statement**: ([default](doc/a_note_on_contributions.md)) 

+ Chen, Jannie: Understood and discussed paper D2. Wrote the ground truth dictionaries for each group. Responsible for the evaluation part. Discussed and wrote the word-wise evaluation functions. Applied the AdaBoost model in the correction part. Organized the Github and wrote the readme file.  

+ Chen, Sizhu: Understood and discussed paper D2. Cleaned the ground truth texts and tesseract texts, and filtered the useless txt pairs and the lines in different length. For evaluation part, established the character-wise evaluation methods and coded the entire part. Organized the Github folders and made the summary. 

+ Li, Yunfan: Understood and discussed paper C2. Create 3-gram and 5-gram candidate sets. Create relaxed-context candidate sets based on ground truth text. Helped to debug the AdaBoost regressions in correction algorithm. Applied the AdaBoost model in the correction part.

+ Xu, Zhengyang: Understood and discussed paper D2. Understood and reproduced the detection algorithm, including error detections using 2-gram algorithm and feature extraction for error correction part. Discussed and corrected the regression part of correction algorithm.

+ Yu, Chenghao: Understood and discussed paper C2. Understood and reproduced the correction algorithm, including feature candidates search and six feature scores establishment using Python. Applied the AdaBoost model in the correction part using Python. Prepared the presentation and drew the slides.

All team members contributed equally in all stages of this project. All team members approve our work presented in this GitHub repository including this contributions statement. 

Following [suggestions](http://nicercode.github.io/blog/2013-04-05-projects/) by [RICH FITZJOHN](http://nicercode.github.io/about/#Team) (@richfitz). This folder is orgarnized as follows.

```
proj/
├── lib/
├── data/
├── doc/
├── figs/
└── output/
```

Please see each subfolder for a README file.
