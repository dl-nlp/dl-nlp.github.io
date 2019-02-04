- Zeit: Mi. 9-11 (VL), Mi. 11-12 (Ü)
- Raum: 131
- Start: 17.10.2018

Sie erreichen Dozent und Tutor unter profilmodul1819 (at) cis (dot) lmu (dot) de

## Topics

The topics of this lecture are the foundations of deep learning, with a particular focus on practical aspects and applications to natural language processing and knowledge representation.

- Foundations of machine learning:
  - Loss functions
  - linear regression
  - logistic regression
  - gradient-based optimization
  - neural networks and backpropagation
- Deep learning tools:
  - Numpy, PyTorch, Keras
- Applications:
  - Tagging, Sentiment-Prediction, Relation extraction
- Practical projects (NLP related, to be agreed on during the course)


## Abgabetermine
- Implementierungen: 28.1.2019
  - Bitte geben Sie Ihre Implementierung auf eine der folgenden Arten ab:
    - als Email-Anhang in einer Archiv-Datei (.zip oder .tar.gz)
    - als Git-Repository auf [github.com](https://github.com/){:target="_blank"} oder auf [gitlab.cip.ifi.lmu.de](https://gitlab.cip.ifi.lmu.de/){:target="_blank"} (öffentlich lesbar, oder mit Leseberechtigung für User `beroth`)
    - Senden Sie die Archiv-Datei oder die URL des Git-Repositorys an profilmodul1819 (at) cis (dot) lmu (dot) de
    - falls Daten größer 10MB Teil Ihres Projektes sind, legen Sie bitte ein Verzeichnis `/big/b/beroth/abgaben/<your_username>` auf den CIP pool-Rechnern an (remote.cip.ifi.lmu.de) und legen Sie die Daten dort ab.
- Pojektvorstellungen am 30.1.2019, 6.2.2019 und 13.2.2019
  - Alle Teilnehmer sind eingeladen, bei den Präsentationen dabeizusein
  - Bitte senden Sie die Slides vor der Präsentation an profilmodul1819 (at) cis (dot) lmu (dot) de
  - Dauer der Präsentationen: 5-10 Minuten/pro Person + 5 Minuten Diskussion
  - **30.1.**
    - 9:15 Robin Rojowiec (Question answering with BiLSTM)
    - 9:30 Sabrina Jacob (Relation classification with piecewise CNNs)
    - 9:45 Yannick Kaiser (Inference in Knowledge Graphs)
    - 10:00 Ziad Elsayes (Natural language generation from structured data with attention)
    - 10:15 Anastasiya Kryvosheya (Antonym-Klassifikation: Keras Architekturen)
    - 10:30 Julius Tutz (Antonym-Klassifikation: Qualitative Analyse)
    - 11:00 Sophia Antonin (multilingual Misogyny detection using multilingual embeddings)
    - 11:15 Agata Barcik (multilingual Misogyny detection: Keras)
    - 11:30 Anna Steinberg (FoFe Encodings/PyTorch)
  - **6.2.**
    - 9:15 Steffen Freisinger (FoFe Encodings/Keras)
    - 9:30 Mustafa Öztürk (Natural language generation from structured data/PyTorch)
    - 9:45 Anotonio Bikic (Text summarization with Seq2seq)
    - 10:00 Sameh Metias (hyper-parameter optimization: random search vs. gaussian processes)
    - 10:15 Verena Pongratz (Detecting insincere questions on Quora/Keras)
    - 10:30 Marina Speranskaya (Detecting insincere questions on Quora/Keras using pre-trained language models)
    - 10:55 Janina Kraus (Insincere Question Detection with PyTorch)
    - 11:10 Christoph Papadatos (Irony dection with pre-trained language models)
    - 11:25 Phillip Fuchs (Irony dection with different encoders and weighting schemes)
    - 11:40 Jannis Vamvas (Prediction of scent profiles from perfume descriptions) 
  - **13.2.**
    - **9:00** Michael Strohmayer (Irony detection in Keras with pretraining)
    - 9:15 Yen Ho (Relation argument extraction: combining text encoders)
    - 9:30 Nadine Sauermann (Relation argument extraction: combining argument extractors)
    - 9:45 Armela Meleqi (Relation classification: examining the impact of negative instances)
    - 10:00 Benjamin Plötz (Irony detection: L2 regularization with pre-trained parameters)
    - 10:15 Ines Röhrer (Irony detection: transfer learning via pre-training)
    - 10:45 Yiyi Chen (Paraphrase embeddings)
    - 11:00 Iryna Matviienko (multilingual antonym detection)
    - 11:15 Ira Maier (German Part-of-speech tagging using pre-trained ressources)
    - 11:30 Jann Paul Engler (Common-sense Reasoning I / Keras)
- Schriftliche Ausarbeitungen: 27.2.2019
    - Sie können die Springer LNCS-Vorlage verwenden [link](https://www.springer.com/gp/computer-science/lncs/new-latex-templates-available/15634678){:target="_blank"}
- Sprache für Präsentation / schriftliche Ausarbeitung ist **Englisch oder Deutsch**.

## Course Material

| Date | slides | homework | materials |
|-----------------------------|:--------------------------------:|:------:|:-------------------------------------------------------------------|
| Oct. 17, 2018 | Machine learning overview [pdf](ml_basics_I.pdf)| [Linear Algebra](ex01_linalg.pdf) | |
| Oct. 24, 2018 | Machine learning overview II [pdf](ml_basics_II_short.pdf)| [Probability](ex02_probability.pdf) | |
| Oct. 31, 2018 | Machine learning overview III [pdf](ml_basics_III.pdf); Numpy [pdf](numpy_intro.pdf) | [Numpy](numpy.ipynb) - Abgabe gerne zu zweit oder zu dritt |  |
| Nov. 07, 2018 | Machine learning rest [pdf](ml_basics_rest.pdf); CIP guide [pdf](guide_cip.pdf); Pytorch [pdf](pytorch_intro.pdf) | [Pytorch](pytorch_intro.ipynb) - Abgabe bitte zu zweit oder zu dritt | Merging of Variable and Tensor [http](https://pytorch.org/blog/pytorch-0_4_0-migration-guide/) |
| Nov. 14, 2018 | Word2Vec [pdf](word2vec.pdf) | [Word Embeddings](pytorch_wordEmbeddings.ipynb) - Abgabe bitte zu zweit oder zu dritt | |
| Nov. 21, 2018 | RNNs [pdf](rnn.pdf) | [LSTMs and GRUs](ex06_lstm.pdf) | |
| Nov. 28, 2018 | Keras [pdf](keras.pdf); Convolution and Pooling [pdf](convolution_pooling.pdf) | [Keras](argument_tagging.ipynb), [Data](atis.json) | [Link zur Mittsemester-Evaluation](https://www.lehrevaluation.uni-muenchen.de/evasys/online/){:target="_blank"} (bitte benutzen Sie die in der VL ausgeteilete TAN - Danke!) |
| Dec. 05, 2018 | Keras (extended) [pdf](keras_extended.pdf); Attention [pdf](attn.pdf) | [Sentiment](keras_sentiment.ipynb) | |
| Dec. 12, 2018 | Projects [pdf](projects.pdf) |  | [Using ssh and GPU](ssh_gpu.txt) |
| Jan. 09, 2019 | Hyperparameters [pdf](hyper_params.pdf) |  | [hyperorpt script](hyperopt.py) |
| Jan. 16, 2019 | Self-Attention (Google Transformer)|  |  "Vaswani et al., 2017: Attention is all You need" [paper](https://arxiv.org/abs/1706.03762), [illustration](http://jalammar.github.io/illustrated-transformer/) |

## More materials
- Jupyter Notebooks Tips and Tricks: [http](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)
- Essence of Linear Algebra: [youtube](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- Keras functional API: [http](https://keras.io/getting-started/functional-api-guide/)
- Bengio: Practical recommendations ... [arXiv](https://arxiv.org/abs/1206.5533)
- Socher: Neural Tips and Tricks [pdf](http://cs224d.stanford.edu/lectures/CS224d-Lecture6.pdf)
- Regularisierung: [reg](reg.md)
