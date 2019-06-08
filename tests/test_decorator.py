
def decorate_bold(func):

    def _func(*args, **kwargs):
        return '<b>%s</b>' % func(*args, **kwargs)

    return _func

def decorate_red(func):

    def _func(*args, **kwargs):
        return '<span style="color: red">%s</span>' % func(*args, **kwargs)

    return _func

def render_text(text):
    return '<span>%s</span>' % text

def test_render_text__decorate_red_and_then_bold():
    @decorate_bold
    @decorate_red
    def _render_text(text):
        return render_text(text)

    assert _render_text('hello') == \
        '<b><span style="color: red"><span>hello</span></span></b>'

def test_render_text__decorate_bold_and_then_red():
    @decorate_red
    @decorate_bold
    def _render_text(text):
        return render_text(text)

    assert _render_text('hello') == \
        '<span style="color: red"><b><span>hello</span></b></span>'


# vi:et:ts=4:sw=4:cc=80
