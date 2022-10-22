# pylint: disable=missing-module-docstring

from duty import duty

@duty
def bsd(ctx):
    '''
    Build & Serv the Documentation.
    '''

    ctx.run(
        'mkdocs build --config-file mkdocs.yml --site-dir .html',
        title='Building documentation'
    )

    ctx.run(
        'mkdocs serve --config-file mkdocs.yml --dev-addr 0.0.0.0:8008',
        title='Serving on http://localhost:8008/'
    )
