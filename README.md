# Vietnamese-noun-phrase-chunking
Public Paper:  [Improvement of Vietnamese noun phrases chunking in text-based person image search](https://ieeexplore.ieee.org/document/10634596?fbclid=IwY2xjawJ8D3tleHRuA2FlbQIxMABicmlkETFpQWw5MXVueEtxdnVKbmF4AR640-7DViVh2mhSTbHAE0hlb8YZyrJwWANJ2NHw5XUPsYzP02wsvVSz9VO3Eg_aem_InroLJBBNkbCwkqb-H3vNw)

Using CRF (Conditional Random Field) as a sequential machine learning model yields good performance for chunking tasks. In addition, research has supplemented several rules to make chunking more suitable for Vietnamese, especially in the Person search task. 
* Generate an IOB2-formatted dataset in CONLL2000 format to facilitate Vietnamese NLP tasks (8969 sentences ~ 187263 tokens). 
Input: "Sẽ tổ chức phố đi bộ tại Hội An" -> Output:
 
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
>Input: Nữ đội mũ màu vàng nhạt rộng vành, mặc áo màu đỏ, quần dài màu vàng nâu nhạt, đi giày bệt màu đen, tay cầm túi xách đen

>Output: nữ , mũ màu vàng nhạt rộng vành , áo màu đỏ , quần dài màu vàng nâu nhạt , giày bệt màu đen , túi xách đen

* And apply it effectively to the Vitta Person Search model. Demo:
  
  ![image](https://github.com/LuongKhanhToann/Vietnamese-noun-phrase-chunking/assets/127384944/a3af30e6-c7a5-46ff-b219-21918a649cf5)
