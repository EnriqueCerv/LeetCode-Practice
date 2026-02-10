# %%


def parsing(dic, targets):
    to_return = []
    targets = set(targets)
    # Termination
    def parsing_rec(d):
        if not isinstance(d, dict):
            return
        
        for key, val in d.items():
            if key in targets:
                to_return.append(val)

            if isinstance(val, dict):
                parsing_rec(val)
            elif isinstance(val, list):
                for ele in val:
                    parsing_rec(ele)

    parsing_rec(dic)
    return to_return