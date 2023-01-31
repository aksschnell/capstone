from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms   
from django.http import JsonResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.paginator import Paginator
import urllib.parse

from .models import User, Movie, Genre, Review, Reaction


def index (request):
        
    genres = Genre.objects.all()

    genre = request.GET.get("genre")    
    sort = request.GET.get("sort") 
    search = request.GET.get("q")  

    if search:
        _search = search
    else:
        _search = ""

    if genre:
        genre = int(genre)   

        if genre > 0:        
            current_genre = Genre.objects.get(id=genre)
            movies = Movie.objects.filter(genre=genre)      
    else:
        movies = Movie.objects.all() 

    if 'movies' in locals():
            print()
    else:
        movies = Movie.objects.all()
    

    if sort == "rating":       
        
        movies = sorted(movies, key=lambda x: x.average_score, reverse=True)
        
    elif sort == "release_year":
        movies = sorted(movies, key=lambda x: x.release_year, reverse=True)
    

    if search:
            
        if 'movies' in locals():

            allEntries = movies

        else:
            allEntries = Movie.objects.all()
            movies = Movie.objects.all()
        
        find_entries = list()
        find_entries_index = list()    
        final_result = list()


        #Sets the entries variable equal to all the entries in lower case
        for i in range(len(movies)):
            movies[i].title2 = movies[i].title.lower()    

        #Sets whatever the user searched to lower (I do this so the user still will be able to find the HTML page if they were to e.g search for html instead of HTML)
        search_box = request.GET.get("q").lower()      
        
        #If there is an immediate match, the user gets redirected to that page
        if search_box in movies:
            return HttpResponseRedirect("movie/" + search_box)      
        
        
        #Looks through each entry and checks for matches, if there is a match, the match gets added to the find_entries list and the index gets added to the find_entries_index list for later use
        for i in range(len(movies)):
            if search_box in movies[i].title2:
                find_entries.append(movies[i])  
                find_entries_index.append(i)

            
        #Makes sure that the user is presented with the matching entries in the original written way e.g CSS and not css as would otherwise happen since i lowered the entries
        for i in range(len(find_entries_index)):
            final_result.append(allEntries[find_entries_index[i]])    
            
            
        movies = final_result

    movie_paginator = Paginator(movies, 9)       
    page_number = request.GET.get("page") 
    page = movie_paginator.get_page(page_number)  
             

    return render(request, "movies/index.html",{
        "movies" : movies,
        "sort" : sort,
        "search" : search,
        "genres" : genres,
        "current_genre" : genre,
        "search" : _search,
        "page" : page
    })


def profile (request, id):

    user_profile = User.objects.get(id=id)
    reviews = Review.objects.filter(creator=user_profile)
    
    user_profile.total_reviews = len(reviews)

    totalscore = 0

    if len(reviews) > 0:

        for review in reviews:
            totalscore += review.score
        
        user_profile.average = str(round((totalscore/user_profile.total_reviews),2))        

    else:
        user_profile.average = "Invalid"

    if request.user.is_authenticated:
        _user = User.objects.get(id=request.user.id)
        all_reactions = Reaction.objects.filter(creator=_user)        
    
        for reaction in all_reactions:              
            for review in reviews:                
                if reaction.review == review:                    
                    if reaction.reaction == 1:
                        review.liked = True
                        review.latest = "l"
                                                
                    elif reaction.reaction == 2:
                        review.disliked = True
                        review.latest = "d"     

    
    return render(request, "movies/profile.html",{

        "user_profile" : user_profile,
        "reviews" : reviews
    })    


def movie (request, id):

    movie = Movie.objects.get(id=id)
    reviews = Review.objects.filter(movie=movie)  

    
    already_reviewed = False

    if request.user.is_authenticated == True:
        users_reviews = Review.objects.filter(creator=request.user, movie=movie) 
        if(len(users_reviews) > 0):
            already_reviewed = True
    else:
        already_reviewed = False


    if request.user.is_authenticated:
        _user = User.objects.get(id=request.user.id)
        all_reactions = Reaction.objects.filter(creator=_user)        
    
        for reaction in all_reactions:              
            for review in reviews:                
                if reaction.review == review:                    
                    if reaction.reaction == 1:
                        review.liked = True
                        review.latest = "l"
                                                
                    elif reaction.reaction == 2:
                        review.disliked = True
                        review.latest = "d"      
    

    return render(request, "movies/movie.html",{

        "id" : id,
        "already_reviewed" : already_reviewed,
        "reviews" : reviews,        
        
    })


def api_movie (request, id):

    if request.method == "GET":

        movie = Movie.objects.get(id=id)
        return JsonResponse([movie.serialize()], safe=False)


@login_required
@csrf_exempt
def reaction (request):

    if request.method == "POST":

        already_reacted = False
        current_user = User.objects.get(id=request.user.id)


        data = json.loads(request.body)        
        review_id = data.get("review_id", "")
        review = Review.objects.get(id=review_id)  

        users_reactions = Reaction.objects.filter(creator=current_user,review=review)

        if(len(users_reactions) > 0):
            already_reacted = True
                
        if already_reacted == False and review.creator != current_user:   
            
            reaction = data.get("reaction", "")      

            reaction_type = reaction
            reaction = Reaction(review=review,creator=current_user,reaction=reaction)
            
            if reaction_type == 1:
                review.likes_amount = review.likes_amount + 1
            elif reaction_type == 2:
                review.dislikes_amount = review.dislikes_amount + 1

            reaction.save()
            review.save()

            return JsonResponse({"message": "reaction was sent succesfully."}, status=201) 

        else:
            return JsonResponse({"message": "User already has reacted to this review."}, status=500)

    if request.method == "DELETE":

        already_reacted = False
        current_user = User.objects.get(id=request.user.id)

        data = json.loads(request.body)     
        
        review_id = data.get("review_id", "")
        review = Review.objects.get(id=review_id)  

        users_reactions = Reaction.objects.filter(creator=current_user,review=review)

        if(len(users_reactions) > 0):
            already_reacted = True

        if already_reacted == True:

            reaction_to_delete = Reaction.objects.get(creator=current_user,review=review)

            reaction_type = reaction_to_delete.reaction

            if reaction_type == 1:
                review.likes_amount = (review.likes_amount -1)
            elif reaction_type == 2:
                review.dislikes_amount = (review.dislikes_amount -1)

            reaction_to_delete.delete()
            review.save()
            return JsonResponse({"message": "Reaction was deleted succesfully."}, status=201)  

        else:
            return JsonResponse({"message": "User has no reaction."}, status=500)  

@login_required
@csrf_exempt
def review (request):
    
    if request.method == "POST":

        data = json.loads(request.body) 

        _creator = User.objects.get(id=request.user.id)    
        _movie = data.get("id", "")

        movieobject = Movie.objects.get(id=_movie)

        already_reviewed = False
        users_reviews = Review.objects.filter(creator=request.user, movie=movieobject) 
        if(len(users_reviews) > 0):
            already_reviewed = True

        if already_reviewed == False:

            _movie = Movie.objects.get(id=_movie)
            _content = data.get("content", "")

            _score = data.get("score", "")

            review = Review(creator=_creator,movie=_movie,content=_content,score=_score)        

            review.save()      

            #Average score for movie
            all_reviews = Review.objects.filter(movie=_movie)
            average_score = 0.0
            total_score = 0.0
            length = 0.0
            length = len(all_reviews)

            for review in all_reviews:
                total_score+= review.score

            average_score = total_score / length
            _movie.average_score = average_score

            _movie.save()       
            return JsonResponse({"message": "Review was sent succesfully."}, status=201)  

            

    else:

        return JsonResponse({"message": "User already has already reviewed this movie."}, status=500)  
            

def login_view(request):
    if request.method == "POST": 

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "movies/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "movies/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "movies/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "movies/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "movies/register.html")
