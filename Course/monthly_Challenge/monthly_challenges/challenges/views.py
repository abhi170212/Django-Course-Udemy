from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect,Http404;
from django.urls import reverse
from django.template.loader import render_to_string


# Create your views here.

# def january(request):
#      return HttpResponse("Take a cold🧊 shower🚿 everyday");

# def february(request):
#      return HttpResponse("Walk🚶🏽20 minutes everyday");

## class work
user_name={
    "user":"Abhishek"
}
def user_name(request):
    try:
        return render(request,user_name)
    except:
        HttpResponseNotFound("no user");
##


monthly_challenges_dict = {
    "january": "Take a cold🧊 shower🚿 everyday",
    "february": "Walk🚶🏽 20 minutes everyday",
    "march": "No🙅🏽 meat🍖 this month.",
    "april": "Read📖 10 pages of a book daily",
    "may": "No☕ caffeine☕ for 30 days",
    "june": "Wake up🌅 before 6 AM everyday",
    "july": "Write✍🏽 a journal🗒️ daily",
    "august": "Learn📚 one new thing everyday",
    "september": "Do📴 digital detox🧘🏽 every Sunday",
    "october": "Workout🏋🏽‍♂️ 4 times a week",
    "november": None,
    "december": "Reflect🪞 on the year and plan📝 next year"
}

def list_of_students(request):
    students=["Fatimah","Nasrin","Fiza","Stacy","julia"];
    return render(request,"challenges/class.html",{
        "name_of_students":students
    })

def index(request):
    #  list_items=""
     months = list(monthly_challenges_dict.keys())
     return render(request,'challenges/index.html',{
         "names_of_mon":months,
     })
     
    #  for month in months:
    #       capitalized_month = month
    #       month_path = reverse("month-challenge",args=[month])
    #       list_items += f"<li>  <a href=\"{month_path}\">{capitalized_month}</a></li>/"
    #  # loops khatm ho gya 
    #  response_data = f"<h1><ul>{list_items}</ul></h1>"
    #  return HttpResponse(response_data)
    






def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_dict[month]
        back_to_index = reverse("index")  # Ye index page ka URL dega
      
        # response_data = render_to_string("challenges/challenge.html") # idhar me jo challenges folder hai wo template ke baad wala hai 
        # return HttpResponse(response_data)
        # alternative to the above two lines 
        # lg_month = month.capitalize()
        return render(request,'challenges/challenge.html',{
            "text":challenge_text,
            "month_name":month
        })
    except:
        # response_data =render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404()


def monthly_challenge_by_number(request,month):
     months = list(monthly_challenges_dict.keys());
     if month > len(months) :
          return HttpResponseNotFound("Invalid Month");
     forward_month = months[month-1];
     redirect_path= reverse("month-challenge",args=[forward_month]) #/challenge/january
     # return HttpResponseRedirect("/challenges/"+forward_month);   
     return HttpResponseRedirect(redirect_path);

def regex(request,username):
    return HttpResponse(f"the username is {username} and the length is {len(username)} characters long")