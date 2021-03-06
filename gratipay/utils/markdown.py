import misaka as m  # http://misaka.61924.nl/

def render(markdown):
    return m.html( markdown
                 , extensions=m.EXT_AUTOLINK | m.EXT_STRIKETHROUGH
                 , render_flags=m.HTML_SKIP_HTML | m.HTML_TOC | m.HTML_SMARTYPANTS
                  )
