from venom.models import Club, Logo, MainPage

def clubs_list(request):
    """
    Возвращает список всех клубов для любого шаблона.
    """
    return {
        "all_clubs": Club.objects.all().order_by("name")
    }


def logo(request):
    """
    Возвращает список всех клубов для любого шаблона.
    """
    return {
        "logo": Logo.get_solo,
    }

def main_page(request):
    return {
        "mainpage": MainPage.get_solo
    }
