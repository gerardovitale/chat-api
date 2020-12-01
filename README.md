
# API project with sentiment analysis
## Overview 
This work corresponds to the fifth project at IronHack. We were basically asked to create an API capable of managing data. 

![api-project-1](images/api-project.png)

The application take advantage of the Instagram API and the mongoDB; what means that the data, which the created API handles, comes from the Instagram API and then is properly stored in mongoDB.

Additionally, some comments would be collected from Instagrams  in order to perform a sentiment analysis using ```nltk, SentimentIntensityAnalyzer```.

The constructed API is able to perform some basic opperations. These are listed below:
1. Recieves data from Instagram API, and then store it in mongoDB, locally.
2. Displays data that is locally stored in mongoDB.
3. Adds, deletes and even modifies data stored in mongoDB, locally.

The following are some methods and their endpoints that the created API has:
- ```/users/``` accepts GET and POST
- ```/users/<username>``` accepts GET and DELETE
- ```/publications``` accepts GET, POST and PUT; additionally, the GET method can recieve querys using the parameters shown below:
    - ```'id'``` Instagram id
    - ```'username'``` Instagram username
    - ```'timestamp'``` DateTime publication
    - ```'_id'``` mongoDb Object id

In order to develop this project, it has been taken into account some packages and libraries that are listed next:
- Flask
- flask_restful
- nltk, SentimentIntensityAnalyzer
- textblob
- requests
- pymongo
- bson
- json


# Development process 

1. The first step to develop this project was to sketch out an outline and define how the API would work, what data base would be better to use, and how the data would be structured and how would go throughout the process.

    In that sense, having into consideration the basic requirements of the project, the following points were set:
    - The API (```myAPI```) would be created on Flask and flask_restful, and methods as GET, POST, DELETE, and PUT would be added as ```def``` of ```Class```.
    - The DataBase selected was MongoDB due to its flexibility; to me, it seems perfect to work with data from API and JSON.
    - Convenience, personal preference and previous experience with google APIs have told me to structure the data as follow:
        - Users collection, that is feed by POST method, and the data displayed by the GET method (both ```/users/```) have this structure:
        ```json
            {
                "result": [
                    {
                        "_id": "5fc51a1fdc7664ad0a03925a",
                        "username": "gerardovitale",
                        "name": "Gerardo Vitale Errico",
                        "ig_id": "188386175",
                        "id": "17841401025252943",
                        "profile_picture_url": "https://scontent-cdt1-1.xx.fbcdn.net/v/t51.2885-15/26870954_2063787480522883_2226548549900828672_n.jpg?_nc_cat=105&ccb=2&_nc_sid=86c713&_nc_ohc=082u-OGHlm4AX99Qjk7&_nc_ht=scontent-cdt1-1.xx&oh=cb0afcac0cb86ef724503545491b7e12&oe=5FE7DCC8",
                        "biography": "🤷🏼‍♂️",
                        "follows_count": "986",
                        "followers_count": "1181",
                        "media_count": "102"
                    },
                ],
                "status": 200
            }
        ```
        - Publications collection, that is feed by POST method, and the data displayed by the GET method (both ```/publications```) have this structure:
        ```json
            {
                "result": [
                    {
                        "_id": "5fc445e07ecf6dea227e7894",
                        "id": "17851991654381629",
                        "username": "gerardovitale",
                        "caption": "I’m running out the time‼️ 🚗💨\n•\n•\n•\n#madrid #spain #españa #love #photography #picoftheday #comunidaddemadrid #driving #drivesmecrazy #drivingperformance #smartcar #mercedes  #mercedesbenz #instagood #photooftheday #travel #style #photo #instagram #model #fitness #music #smile #photographer #me #europe #lifestyle #instadaily #sunday #sundaymood☀️",
                        "timestamp": "2020-11-22T21:45:48+0000",
                        "comments": [
                            {
                                "timestamp": "2020-11-23T13:55:29+0000",
                                "text": "¿Rápido y furioso? Ó ¿a todo gas?",
                                "id": "18052759243265491"
                            }, ...
                    }, ...
                ],
                "status": 200
            }
        ```
2. Secondly, a database was created in mongoDB and it was filled in with some info in order to test the methods and functions that would be written in any moment.
3. In third place, while the scripts located in ```/api``` and ```/helpers``` were being written, some basic test were carried out in google chrome and in the postman extension. At this point, myAPI and mongoDB were connected and exchanging data.
4. Then, when myAPI seemed ro be ready to managed some data flow, the focus turned into collecting some info from Instagram API. It should be noted that the request to instagrams were and are set to be made by the API. At this point, it was clear that it has been set a connection between myAPI and Instagram, and another one between myAPI and mongoDB.
5. Finally, the comments collected from the Instagram API response were analysed using ```nltk, SentimentIntensityAnalyzer```, so that it could be possible to know if those comments were either positive, negative or even neutral. This analysis was performed just considering my instagram account (**@gerardovitale**) and for the latest posts. the result are shown below:
```
                neg         neu         pos    compound
    count  182.000000  182.000000  182.000000  182.000000
    mean     0.019912    0.848044    0.071610    0.066964
    std      0.075549    0.291162    0.182128    0.249331
    min      0.000000    0.000000    0.000000   -0.732600
    25%      0.000000    0.826750    0.000000    0.000000
    50%      0.000000    1.000000    0.000000    0.000000
    75%      0.000000    1.000000    0.000000    0.000000
    max      0.524000    1.000000    1.000000    0.947600
```


Readers should consider that ```nltk, SentimentIntensityAnalyzer``` has not been optimise to treat emojis and other languages but english, and both are present in my instagram account comment.
