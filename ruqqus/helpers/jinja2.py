import time

from ruqqus.classes.user import User
from ruqqus.classes.ips import IP
from ruqqus.__main__ import app, db, cache

@app.template_filter("users_here")
def users_here(x):

    now=time.time()

    cutoff=now-300

    return db.query(User).join(IP).filter(IP.created_utc>=cutoff).count()

@app.template_filter("total_users")
def total_users(x):

    return db.query(User).filter_by(is_banned=False).count()
