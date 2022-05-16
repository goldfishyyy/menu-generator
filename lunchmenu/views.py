from django.shortcuts import render
import random
# import lunchmenu.read_files
from lunchmenu.read_files import get_file_content

# Create your views here.
def homepage(request):
    return render(request, 'lunchmenu/homepage.html')


def display(request):
    chicken_menu = []
    pork_menu = []
    seafood_menu = []
    beef_menu = []
    main_choice = request.GET.get("main")
    # with open("lunchmenu/chicken", "r") as f:
    #     for line in f:
    #         chicken_menu.append(line.rstrip("\n"))
    # chicken_menu = lunchmenu.read_files.get_file_content("lunchmenu/chicken")
    chicken_menu = get_file_content("lunchmenu/chicken")
    pork_menu = get_file_content("lunchmenu/pork")
    seafood_menu = get_file_content("lunchmenu/seafood")
    beef_menu = get_file_content("lunchmenu/beef")
    if main_choice == "chicken":
        main_dish = random.choice(chicken_menu)
    elif main_choice == "pork":
        main_dish = random.choice(pork_menu)
    elif main_choice == "seafood":
        main_dish = random.choice(seafood_menu)
    elif main_choice == "beef":
        main_dish = random.choice(beef_menu)

    return render(request, "lunchmenu/display.html", {"main": main_dish})

def about(request):
    return render(request, 'lunchmenu/about.html')
