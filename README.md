# Project: OCR (Optical Character Recognition) 

![image](figs/intro.png)

### [Full Project Description](doc/project4_desc.md)

Term: Fall 2018

+ Team #
+ Team members
	+ Chen, Jannie mc4398
	+ Chen, Sizhu sc4248
	+ Li, Yunfan yl3838
	+ Xu, Zhengyang zx2229
	+ Yu, Chenghao cy2475

+ Project summary: In this project, we created an OCR post-processing procedure to enhance Tesseract OCR output. 
	
**Contribution statement**: ([default](doc/a_note_on_contributions.md)) 

+ Chen, Jannie: Wrote the ground truth dictionaries for each group. Responsible for the evaluation part. Discussed and wrote the word-wise evaluation functions. 

+ Chen, Sizhu: Responsible for the evaluation part. Tested the word-wise evaluation functions and wrote the character-wise evaluation functions. 

+ Li, Yunfan: Create 3-gram and 5-gram candidate sets. Create relaxed-context candidate sets based on ground truth text. 

+ Xu, Zhengyang: Understood and reproduced the detection algorithm, including error detections using 2-gram algorithm and feature extraction for error correction part. 

+ Yu, Chenghao: Understood and reproduced the correction algorithm, including feature candidates search and six feature scores establishment using Python. 

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
