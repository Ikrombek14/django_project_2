from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def first_page(requests):
    html = """ <h1> salom dunyo </h1>
                <a href="second/">Ikkinci</a>
    """

    return HttpResponse(html)

def second_page (requests):
    html = """ <h1> Xayr dunyo </h1>
           <a href="../">Birinchi</a>
           
           
           <a href="three/">Uchinchi</a>"""



    return HttpResponse(html)

def three_page(requests):
    html="""<h1> Bu mening 1 proyektim </h1> 
            <a href="../">Birinchi</a>
    """

    return HttpResponse(html)