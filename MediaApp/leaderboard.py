def update_outlet_score(outlet, score):
    outlet.score += score
    outlet.save()