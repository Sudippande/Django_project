from django.shortcuts import render,redirect
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login
#like session jsare security add garna we can use deco to protect the routes
# Create your views here.


def home(request):
    return render(request,'index.html')

def tweet_list(request):
    
    tweets = Tweet.objects.all().order_by("-created_at")  # correct order_by usage
    return render(request, 'tweet_list.html', {'tweets': tweets})




#Form handling in django Customize  way
#Tweet creation
@login_required
def tweet_create(request):
    if request.method=="POST":
        form=TweetForm(request.POST,request.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form=TweetForm()
    return render(request,'tweet_form.html',{'form':form})



#Edition of Tweet
@login_required
def tweet_edit(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method =='POST':
        form=TweetForm(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweet_list')
    
    else:
        form=TweetForm(instance=tweet)
    return render(request,'tweet_form.html',{'form':form})


#delete tweet
@login_required
def tweet_delete(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method =='POST':
        tweet.delete()
        return redirect("tweet_list")
    
    return render(request,'tweet_conform_delete.html',{'tweet':tweet})

def register(request):
    if request.method =='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1']) # Here i have set the password from user
            # data collection through user form
            user.save()
            login(request,user)
            return redirect('tweet_list')
    else:
        form=UserRegistrationForm()

    return render(request,'registration/register.html',{'form':form})