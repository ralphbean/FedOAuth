from time import time
from datetime import datetime
import sys
from urlparse import urljoin
from uuid import uuid4 as uuid

from flask import Flask, request, g, redirect, url_for, \
    abort, render_template, flash, Response
from flaskext.babel import gettext as _

from model import FASOpenIDStore
from fas_openid import APP as app, get_session, log_debug, \
    log_info, log_warning, log_error, get_auth_module
from views_openid import view_openid_main


@app.route('/robots.txt')
def view_robots():
    return 'User-Agent: *\nDisallow: /'


@app.route('/', methods=['GET', 'POST'])
def view_main():
    # We are using view_openid_main because this makes sure that the
    #  website root is also a valid OpenID endpoint URL
    return view_openid_main()


@app.route('/logout/')
def auth_logout():
    # No check if we are logged in, as we can always delete the session
    get_session().delete()
    flash(_('You have been logged out'))
    return redirect(url_for('view_main'))
