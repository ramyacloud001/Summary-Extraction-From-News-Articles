
<h1 align="center"> Summary Extraction of News Articles </h1>

<hr>

<div align="center">
  <img src="https://user-images.githubusercontent.com/88481845/216892198-cf099b93-f47e-4ca1-8719-bb77e88cde28.jpg">
</div>

<hr>

Summary Extraction is the technique for generating meaningful and complete information of the text while focusing on the sections that convey useful information, and without losing the overall meaning of the text. Summary Extraction aims to transform lengthy Text into shortened versions, which makes it easy to understand. 

For Summary extraction from the News Articles we are usin a Library called nwewspaper3k . Where we can collect the urls of the article and collect the text 

## Summary Extracting newspaper3k Library.

Using the newspaper Library we can collect the complete text of the Article just by using a predefined function called Article. There are some advantages and disadvantages to using the newspaper3k library.


```bash
from newspaper import Article
url = “Enter the url”
article = Article(url)
```
The complete text of an article was in a variable called article. 

## Advantages of using newspaper3k
1. Predefined functions
2. Easy to access the complete text of an Article
3. Easy to collect the Author names and Publish dates of an article with authors and publish_date functions.
4. Using the newspaper3k library it is very easy to collect the summary of an article using a variable. summary function. 

## Disadvantages of using newspaper3k

1. Cannot download the complete URLs of the website if we run the code n number of times
2. The summary collected using newspaper3k was not as expected
3. Using a newspaper library becomes difficult during the time of deployment on Heroku. Because Heroku has no corpora keywords as the default installed, we need to provide corpora keywords in a text file while deployment. 

# Implementation 

Punkt can pick its first 5 tokenized sentences and string them together to form a complete summary. Punkt helps us to divide the complete text into a list of sentences.
To overcome the disadvantages of newspapers 3k and to collect meaningful summaries. Now we are using a Library called spacy.

Before using the techniques of the spacy library we just took the help of the nltk library to convert the complete text into sentences. For this purpose, we are using a function called tokenizer.

With the help of spacy the collected text and the individual words where given some importance based on there embedding vectors results and findiing the performance of each word  compare to the entire length. By doing this technique we can collect the probability percentage of text as a summary .

# REGEX

<img src="https://user-images.githubusercontent.com/88481845/216893150-a844a5dd-af22-4ca1-8000-90eaba8e8e84.png" width="700" height="400">

Using regex we just clean the data .using meta characters and spatial sequential for cleaning purpose 

<h3> Meta characters </h3> 

                          1 . [] -> returns a match if contains patterns / character specified in []
                          2 . ^ -> string starts with given patterns 
                          3 . $ -> ends with 
                          4 . . -> any character except new line 
                          5 . * -> Zero or more occurences 
                          6 . + -> one or more occurences 
                          7 . {} -> specified number of occurences 

                          

<h3> special sequences </h3> 

                            1 . \d -> if a given string has digits (0-9)
                            2 . \D -> if the given string does not have strings
                            3 . \w -> if a given string has word characters(a-z,A-Z,0-9)
                            4 . \W -> if a given string does not have word characters
                            5 . \s -> if given string has spaces
                            6 . \S -> if given string has no spaces

                         

<p> Techniques used for cleaning </P> 


                         1 . Removing unwanted Punctuation for the text
                         2 . Removing URLS from the text 
                         3 . Removing hashtags 
                         4 . Removing Extra white spaces 
                         5 . Lowering the text 
                         6 . removing the own mentions 
                      


# Outputs

<table>
  <tbody>
  <tr>
    <th>Article URL</th>
    <th>Summary Extracted</th>
  </tr>
    <tr>
      <td align="center">
       <a href="https://timesofindia.indiatimes.com/city/hyderabad/pochampally-indias-silk-city-is-worlds-best-tourism-village/articleshow/87746860.cms">Telangana's Pochampally, India’s silk city, is world’s best tourism village</a> 
      </td>
      <td>This style Pochampally Ikat received a Geographical Indicator GI status in 2004 and is also known as Bhoodan Pochampally to commemorate the Bhoodan movement that was launched by Acharya Vinobha Bhave from this village on April 18 1951.The ministry of tourism said it has drafted a rural tourism policy which will not only promote tourism within our villages but also revitalise local arts and crafts and promote the rural economy. The best tourism villages by UNWTO pilot initiative aims to award those villages which are outstanding examples of rural destinations and showcases good practices in line with its specified evaluation areas. HYDERABAD: Pochampally village in Yadadri Bhuvanagiri district known for its famous hand-woven Ikat saris was on Tuesday selected as one of the best tourism villages by the United Nations World Tourism Organisation UNWTO.The award will be given at the 24th session of the UNWTO general assembly on December 2 in Madrid. </td>
    </tr>
    <tr>
      <td align="center">
      <a href="https://timesofindia.indiatimes.com/india/bjp-to-retain-up-sp-to-be-distant-second-survey/articleshow/87747004.cms">BJP to retain UP, SP to be distant second</a> 
      </td>
      <td>BSP is projected to lose a significant share of its votes to both SP and BJP and finish third with around 30 seats while Congress could end up with five to eight seats not very different from the seven it won in 2017.If the projections turn out to be aurate Yogi Adityanath would become the first chief minister in Uttar Pradesh to serve two consecutive terms. The opinion poll indicated strong support for the Yogi government’s hard-line approach on law and order as well as to a lesser extent for its legal route to countering ‘forced’ conversions. </td>
    </tr>
    <tr>
      <td align="center">
      <a href="https://timesofindia.indiatimes.com/india/air-pollution-thermal-plants-closed-trucks-cant-enter-delhi/articleshow/87745983.cms">Air pollution: Thermal plants closed, trucks can’t enter Delhi</a> 
      </td>
      <td>These include shutting down all except five thermal power plants within a 300km radius of Delhi till November 30 stopping entry of trucks in Delhi except for those carrying essential commodities keeping diesel and petrol vehicles more than 10 and 15 years old respectively in NCR off the road and banning construction and demolition activities in NCR till November 21 except for some government and infrastructure projects. This followed a meeting with NCR states earlier in the day with the focus on vehicular pollution dust pollution from construction activities and roads and emissions from thermal power plants and industrial pollution. At least 50 of the government staff across NCR will work from home and private establishments will be encouraged to do so till November 21.Among other measures announced by the commission are banning of DG sets in entire NCR except for emergency services and ensuring that all industries in NCR with gas connections are run only on gas failing which they are to be shut down. Delhi’s air quality deteriorated on Tuesday again entering the severe category at 403.Of the 11 thermal power plants the five that have been allowed to function are NTPC Jhajjar Mahatma Gandhi TPS CLP Jhajjar Panipat TPS HPGCL Nabha Power Ltd TPS Rajpura and Talwandi Sabo TPS Mansa. </td>
    </tr>
  </tbody>
</table>


## 🛠 Skills

        1.Python 
        2.Machine learning 
        3.Statistics
        4.Mathematics
        5.Numpy 
        6.Neural Networks
        7.Deep Learning Multilayer Perceptron concepts 
        8.Computer Vision
    


## Support

For support, email ramyasri.adepu1601@gmail.com .


## Acknowledgements

 - [Documentation](https://www.bluetickconsultants.com/summary-extraction-of-an-article-using-experimental-NLP-techniques.html)


## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ramyasri-adepu-a30958166/)
