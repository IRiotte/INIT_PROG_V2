#7.1 excès de vitesse de l'util, limite de vitesse lors de l'exces de vitesse
#7.2 85kmh, 570 --> 68, 1, 0 / 45kmh, 30 --> 135, 1, 0
#    145, 100 --> 135, 4, 3 / 180, 100 --> 1500, 6, 3
#
def sanction_vitesse(exces_vitesse_util, limit_vitesse):
    """fonction qui donne la santion adaptée selon l'excès de vitesse de l'utilisateur

    Args:
        vitesse_util (int): l'excès de vitesse de l'utilisateur en km/h
        limit_vitesse (int): limitaion de vitesse lors de l'excès

    Returns:
        n-uplet: triplet contenant le montant de l'ammande encourue (int),
                 le nombre de points perdus (int),
                 et la durée de suspension de permis en année (int)
    """
    if exces_vitesse_util == 0:
         sanction = (0,0,0)
    elif exces_vitesse_util <= 20:
        if limit_vitesse <= 50:
            sanction = (135,1,0)
        else:
            sanction = (68,1,0)
    elif exces_vitesse_util <= 30:
            sanction = (135,2,0)
    elif exces_vitesse_util <= 40:
         sanction = (135,3,3)
    elif exces_vitesse_util <=50:
         sanction = (135,4,3)
    else:
         sanction = (1500,6,3)
    return sanction

print (sanction_vitesse(0, 50))

def test():
     assert sanction_vitesse(10,70) == (68,1,0)
     assert sanction_vitesse(10,50) == (135,1,0)
     assert sanction_vitesse(25,90) == (135,2,0)
     assert sanction_vitesse(35,130) == (135,3,3)
     assert sanction_vitesse(45,110) == (135,4,3)
     assert sanction_vitesse(55,80) == (1500,6,3)






def securite(vitesse, limite):
    point = 0
    amende = 0
    suspension = 0
    depassement = vitesse-limite
    if depassement > 0:
        if depassement <= 20:
            point = 1
            if limite:
                amende = 135
            else:
                amende = 68
        else:
            if depassement <= 30:
                point = 2
                amende = 135
            else:
                suspension = 3
                if depassement <= 40:
                    point = 3
                    amende = 135
                else:
                    if depassement <= 50:
                        point = 4
                        amende = 135
                    else:
                        point = 6
                        amende = 1500
    return (point, amende, suspension)
    
