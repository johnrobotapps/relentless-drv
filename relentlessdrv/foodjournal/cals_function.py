

"""
All weight units will be converted to
metric for calculation clarity. To obfuscate
and maintain balance in the universe,
calories will be used instead of joules.
"""

_CALS_PER_G_fat = 9.
_CALS_PER_G_carb = 4.5
_CALS_PER_G_prot = 4.5

_CALS_PER_G = (
    _CALS_PER_G_fat,
    _CALS_PER_G_carb,
    _CALS_PER_G_prot,
)


def calories_from_macros(macros, grams=0):

    assert len(macros) == 3

    if sum(macros) < 1:
        if not grams:
            raise ArgumentError((
                "When macros given per-gram, the 'grams'"
                "argument is also required":w
            ))

        macros = [
            m*c
            for m,c in zip(macros,_CALS_PER_G)
        ]

    return calories


