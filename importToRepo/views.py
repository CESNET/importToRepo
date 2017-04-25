from django.http import HttpResponse

from importToRepo.models import Reaction


def getReactions(request):
    # r = Reaction(reaction_carried_out_by="Testovaci uzivatel")
    # r.save()

    reactions = Reaction.objects.get(pk=122)

    html = "<html><body><h1>Reactions</h1></body></html>"
    return HttpResponse(html)