from functools import singledispatch
from utilidades import cut_symbol
import re

pseudoinstrucciones = {
    "^nop\\s*$": "addi x0, x0, 0",
    "^mv\\s+(?P<rd>\\w+),\\s*(?P<rs>\\w+)\\s*$": "addi {rd}, {rs}, 0",
    "^not\\s+(?P<rd>\\w+),\\s*(?P<rs>\\w+)$": "xori {rd}, {rs}, -1",
    "^neg\\s+(?P<rd>\\w+),\\s*(?P<rs>\\w+)$": "sub {rd}, x0, {rs}",
    "^negw\\s+(?P<rd>\\w+),\\s*(?P<rs>\\w+)$": "subw {rd}, x0, {rs}",
    "^seqz\\s+(?P<rd>\\w+),\\s*(?P<rs>\\w+)$": "sltiu {rd}, {rs}, 1",
    "^snez\\s+(?P<rd>\\w+),\\s*(?P<rs>\\w+)$": "sltu {rd}, x0, {rs}",
    "^sltz\\s+(?P<rd>\\w+),\\s*(?P<rs>\\w+)$": "slt {rd}, {rs}, x0",
    "^sgtz\\s+(?P<rd>\\w+),\\s*(?P<rs>\\w+)$": "slt {rd}, x0, {rs}",
    "^beqz\\s+(?P<rs>\\w+),\\s*(?P<offset>\\w+)\\s*$": "beq {rs}, x0, {offset}",
    "^bnez\\s+(?P<rs>\\w+),\\s*(?P<offset>\\w+)\\s*$": "bne {rs}, x0, {offset}",
    "^blez\\s+(?P<rs>\\w+),\\s*(?P<offset>\\w+)\\s*$": "bge x0, {rs}, {offset}",
    "^bgez\\s+(?P<rs>\\w+),\\s*(?P<offset>\\w+)\\s*$": "bge {rs}, x0, {offset}",
    "^bltz\\s+(?P<rs>\\w+),\\s*(?P<offset>\\w+)\\s*$": "blt {rs}, x0, {offset}",
    "^bgtz\\s+(?P<rs>\\w+),\\s*(?P<offset>\\w+)\\s*$": "blt x0, {rs}, {offset}",
    "^bgt\\s+(?P<rs>\\w+),\\s*(?P<rt>\\w+),\\s*(?P<offset>\\w+)\\s*$": "blt {rt}, {rs}, {offset}",
    "^ble\\s+(?P<rs>\\w+),\\s*(?P<rt>\\w+),\\s*(?P<offset>\\w+)\\s*$": "bge {rt}, {rs}, {offset}",
    "^bgtu\\s+(?P<rs>\\w+),\\s*(?P<rt>\\w+),\\s*(?P<offset>\\w+)\\s*$": "bltu {rt}, {rs}, {offset}",
    "^bleu\\s+(?P<rs>\\w+),\\s*(?P<rt>\\w+),\\s*(?P<offset>\\w+)\\s*$": "bgeu {rt}, {rs}, {offset}",
    "^j\\s+(?P<offset>\\w+)\\s*$": "jal x0, {offset}",
    "^jal\\s+(?P<offset>\\w+)\\s*$": "jal x1, {offset}",
    "^jr\\s+(?P<rs>\\w+)\\s*$": "jalr x0, {rs}, 0",
    "^jalr\\s+(?P<rs>\\w+)\\s*$": "jalr x1, {rs}, 0",
    "^ret\\s*$": "jalr x0, x1, 0",
    "^call\\s*(?P<symbol>\\w+)\\s*$": ["auipc x1, {symbol1}", "jalr x1, x1, {symbol2}"],
    "^tail\\s*(?P<symbol>\\w+)\\s*$": ["auipc x6, {symbol1}", "jalr x0, x6, {symbol2}"],
    "^li\\s+(?P<rd>\\w+),\\s*(?P<symbol>[+-]?\\d+|0[xX][0-9a-fA-F]+)\\s*$": ["lui {rd}, {symbol1}", "addi {rd}, {symbol2}"],
    "^l(?P<letter>[bhwd])\\s+(?P<rd>\\w+),\\s*(?P<symbol>[+-]?\\d+|0[xX][0-9a-fA-F]+)\\s*$": ["auipc {rd}, {symbol1}", "l{letter} {rd}, {symbol1}({rd})"],
    "^s(?P<letter>[bhwd])\\s+(?P<rd>\\w+),\\s*(?P<symbol>[+-]?\\d+|0[xX][0-9a-fA-F]+),\\s*(?P<rt>\\w+)\\s*$": ["auipc {rt}, {symbol1}", "s{letter} {rd}, {symbol2}({rt})"],
    "^la\\s+(?P<rd>\\w+),\\s*(?P<symbol>[+-]?\\d+|0[xX][0-9a-fA-F]+)\\s*$": ["auipc {rd}, {symbol1}", "addi {rd}, {rd}, {symbol2}"]
}

def is_pseudo(instruction: str):
    
    for pattern, equivalence in pseudoinstrucciones.items():
        match = re.match(fr"{pattern}", instruction)
        if match:
            return match.groupdict(), equivalence
    return False, False

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