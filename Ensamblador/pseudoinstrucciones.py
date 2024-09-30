from functools import singledispatch
from utilidades import cut_symbol

@singledispatch
def compile_pseudo(equivalence: str, match: dict, line: str|int):
    equivalence = equivalence.format(**match)
    return [equivalence]

@compile_pseudo.register
def _(equivalence: list, match: dict, line: str|int):
    equivalence = "|".join(equivalence)
    match.update(cut_symbol(match["symbol"], line))
    del match["symbol"]
    equivalencias = equivalence.format(**match)
    return equivalencias.split("|")