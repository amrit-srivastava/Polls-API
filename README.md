# App to generate questions with multiple choices in JSON format
It uses Django Rest Frameworks to create APIs (GET and POST requests).  
Available at : [https://django-polls-api.herokuapp.com/](https://django-polls-api.herokuapp.com/)

# Api Documentation 

URL 1 :https://django-polls-api.herokuapp.com/  
Method : POST   
format :  
{  
    "choice_set": [{"SetOfDictionary":"hey"}],  
    "question_text": "Sample Text",  
    "pub_date": "12/12/2020"  
}  