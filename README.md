## Goal of this project  

Most of the offers follow a simple pattern: *Destination - Origin - Price - Extras*, while extracting this may seem easy for a regular expression, it is not (see this notebook for reference). 

The idea is to create a tagger that will be able to extract this information, however, one first tag is to identify the information that we want to extract. Following the pattern described above: 

 - **o**: Origin 
 - **d**: Destination 
 - **s**: Token between Origin and Destination
 - **p**: Price 
 - **f**: Flag
 - **n**: Irrelevant token
 
| Text 	| d 	| o 	| p 	| n 	|
|------	|-----	|-----	|-----	|-----	|
| ¡CUN a Holanda \$8,885! Sin escala EE.UU | CUN | Holanda | 8,885 | Sin escala EE.UU |   
| ¡CDMX a Noruega <span>$</span>10,061! (Y agrega 9 noches de hotel por \$7,890!) | CDMX | Noruega | 10,061 | Y agrega 9 noches de hotel por \$7,890!| 
| ¡Todo México a Pisa, Toscana Italia \$12,915! Sin escala EE.UU (Y por \$3,975 agrega 13 noches hotel) | México | Pisa, Toscana Italia | 12,915 | Sin escala EE.UU (Y por \$3,975 agrega 13 noches hotel) |


## POS Tagging  

To perform the Part-Of-Speech tagging we'll be using the [Stanford POS Tagger](https://nlp.stanford.edu/software/tagger.shtml); this tagger (or at least the interface to it) is available to use through Python's NLTK library, however, we need to download some models from the [Stanford's download page](https://nlp.stanford.edu/software/tagger.shtml#Download). In our case, since we are working with spanish we should download the full model under the *"2017-06-09 	new Spanish and French UD models"* subtitle.

Once downloaded, it is necessary to unzip it, and keep track of where the files end up being. You could just execute:

```shell script
make models/stanford
```  

To get the necessary files inside a folder called `stanford-models`.

Now we can jump to the `Part-Of-Speech Tagging.ipynb` notebook.

## Obtaining Ground Truth  

**We do not need POS Tagging to generate a tagged dataset!**, however, this is how I implemented it in the beginning, so that is how I am going to explain it.

As detailed at the top of this file, we need to get some labels from *"expert"* users. These labels will be used to train the algorithm to produce predictions. The task for the users will be simple: assign one of the following letters to each token: `{ o, d, s, p, f, n }`. While there are many ways to obtain these labels, I decided to follow a more rustic approach, check what I did in the `Obtaining ground truth.ipynb` notebook.


## Feature extraction  

While having the POS tags is good and valuable information, it may not be enough to get valuable predictions for our task. However, we can provide our algorithm with more information such as the length of the token, the length of the sentence, the position within the sentence, whether the token is a number or all uppercase...

In the `Extracting other features.ipynb` notebook you can see the features I have decided to extract.

## Conditional random fields for sequence labelling  

Once we have our dataset with all the features we want to include, as well as all the labels for our sequences, we can move on to the actual training of our algorithm. For this task we'll be using the [`python-crfsuite`](https://python-crfsuite.readthedocs.io/en/latest/) package. To train this algorithm we should modify a bit the inputs to it, see what modifications and how to train the algorithm in the `CRF.ipynb` notebook.

## Label new sentences!

What good is our system if we can not use it to predict the labels of new sentences. Before that, though, we need to make sure to set up a complete pipeline to go from having a new offer as displayed in the VuelaX site to have a fully labelled offer on our python scripts, head over to the `Putting everything together.ipynb` notebook to learn more. 