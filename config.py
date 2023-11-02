        
KEYWORDS = {
    'print': 'print(%s)',
}

START_KEYWORDS = {
    'for': 'for %s:',
    'while': 'while %s:',
    'if': 'if %s:',
}

END_KEYWORDS = {
    'endfor': '%s',
    'endwhile': '%s',
    'endif': '%s',
}

ALL_KEYWORDS = {
    **KEYWORDS,
    **START_KEYWORDS,
    **END_KEYWORDS,
}