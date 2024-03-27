# Vietnamese-noun-phrase-chunking
* Generate an IOB2-formatted dataset in CONLL2000 format to facilitate Vietnamese NLP tasks. Demo:
 
|       Word       |      POS tags        | Labels     |
| :------------:|:-------------:|:-----:|
|    Sẽ        |        R      |  O   |
|     tổ_chức         |        M      |   O  |
|     phố         | N            |   B-NP  |
|    đi        |        V      |  I-NP   |
|     bộ        |        N      |   I-NP   |
|    tại        | E             |    O  |
|    Hội        | N             |    B-NP  |
|    An    | Np             |    I-NP  |
* Build a model for chunking Vietnamese noun phrases with an F1-score of 91.34% and Bleu-score of 85.89%, and apply it effectively to the Vitta Person search model.
  ![image]
  (https://github.com/LuongKhanhToann/Vietnamese-noun-phrase-chunking/assets/127384944/a3af30e6-c7a5-46ff-b219-21918a649cf5)


The project is further described in the paper: [link](https://www.overleaf.com/read/ccmnfqywqbzn#d6105a) (currently in the submission process).
