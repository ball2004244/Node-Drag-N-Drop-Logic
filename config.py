
KEYWORDS = {
    'print': 'print(%s)',
    'comment': '# %s',
}

START_KEYWORDS = {
    'for': 'for %s:',
    'while': 'while %s:',
    'if': 'if %s:',
    'else': 'else: %s',
    'func': 'def %s:',
    'class': 'class %s:',
}

END_KEYWORDS = {
    'endfor': '%s',
    'endwhile': '%s',
    'endif': '%s',
    'endelse': '%s',
    'endfunc': 'return %s',
    'endclass': '%s',
}

ALL_KEYWORDS = {
    **KEYWORDS,
    **START_KEYWORDS,
    **END_KEYWORDS,
}
