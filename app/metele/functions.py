import random

def generate_hale(nu: int):
    sologe = [
        "ma","na","va","fa","da","ta","ya","ha","ga","ka","ba","pa","za","sa","la","ra",
        "me","ne","ve","fe","de","te","ye","he","ge","ke","be","pe","ze","se","le","re",
        "mo","no","vo","fo","do","to","yo","ho","go","ko","bo","po","zo","so","lo","ro",
        "mu","nu","vu","fu","du","tu","yu","hu","gu","ku","bu","pu","zu","su","lu","ru",
    ]
    return ''.join(random.choice(sologe) for i in range(nu))