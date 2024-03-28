# Vietnamese-noun-phrase-chunking
Using CRF (Conditional Random Field) as a sequential machine learning model yields good performance for chunking tasks. In addition, research has supplemented several rules to make chunking more suitable for Vietnamese, especially in the Person search task.
* Generate an IOB2-formatted dataset in CONLL2000 format to facilitate Vietnamese NLP tasks (8969 sentences ~ 187263 tokens). Demo:
 
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
* Build a model for chunking Vietnamese noun phrases with an F1-score of 91.34% and Bleu-score of 85.89%. Demo:
>Input: Người phụ nữ đội mũ rộng vành màu vàng nâu, mặc áo dài màu xanh lá cây, quần dài đen, đeo túi đeo chéo màu đỏ pha trắng, đi giày đen

>Output: người phụ nữ , mũ rộng vành màu vàng nâu , áo dài màu xanh lá cây , quần dài đen , chéo màu đỏ pha trắng , giày đen

* And apply it effectively to the Vitta Person Search model. Demo:
  
  ![image](https://github.com/LuongKhanhToann/Vietnamese-noun-phrase-chunking/assets/127384944/a3af30e6-c7a5-46ff-b219-21918a649cf5)


The project is further described in the paper: [link](https://www.overleaf.com/read/ccmnfqywqbzn#d6105a) (currently in the submission process).
