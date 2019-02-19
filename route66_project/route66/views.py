# importing the respons function

from django.http import HttpResponse

# defining the reponse on each of the paths

def index(request):
    return HttpResponse("Please follow one of the following routes: mycity/ myeats/")

def gogetthegood(request):
    return HttpResponse("Here you go! My music is super important to me go check out my song on youtube! I'Tayanna Its over")

def happyhappyjoyjoy(request):
    return HttpResponse("I love ren and stipmy too. But that show is not for kids")