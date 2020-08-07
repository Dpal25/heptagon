# heptagon

Run the Django server:

```
python manage.py runserver
```

Get all posts
```
curl -X get http://localhost:8000/blog/post/read/
```
Create a post
```
curl -X put -d "title=Hello&body=World" http://localhost:8000/blog/post/create/
```
Get a single post with comments
```
curl -X get http://localhost:8000/blog/post/7/
```
Delete a post
```
curl -X delete http://localhost:8000/blog/post/get/7/
```
Update a post
```
curl -X update http://localhost:8000/blog/post/update/7/
```

Add a comment on a post with id 5
```
curl -X post -d "author=pallavi&body=hello" http://localhost:8000/blog/post/get/5/comment/create/
```
Delete comment with id 8 for post with id 5
```
curl -X delete http://localhost:8000/blog/post/get/5/comment/delete/8/
```
Update comment with id 8 for post with id 5
```
curl -X update http://localhost:8000/blog/post/get/5/comment/update/8/
```



