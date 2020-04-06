## Django backend for aution house

### To install the requirements
pip install -r requirements.txt

## To start the backend
python manage.py runserver

## Django Admin Page, super user details
http:127.0.0.1:8000/admin

login details: sha/sha

##Implemented
1. API to add a product to the database
2. API to view all the products in the db.
3. API to bid for the product. 
4. Multiple users can bid for the product.
5. If the same users bids for a product multiple times, the latest value will be considered.

###After starting the backend the API are available at
[GET] http://127.0.0.1:8000/api/ 

[POST] http://127.0.0.1:8000/api/create/

Example:

```json
{
        "name": "abcd",
        "description": "abcd",
        "starting_bid": "100",
        "deadline": "2020-04-05",
        "contact": "9876543210",
        "image": "/media/images/Bat_logo_2.jpg",
        "bids": "{}",
        "uploaded_by": "sha"
    }
```


[PUT] http://127.0.0.1:8000/api/update/<pk> (For updating the bid)

Example:

```json
{"username":  100}
```

##Not implemented
1. Login/signup functionality
2. API to claim the Product.

##Bugs
1. Image upload is having issues.