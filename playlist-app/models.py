"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    # ADD THE NECESSARY CODE HERE

    __tablename__ = "playlists"

    def __repr__(self):
        '''Better Representation of the class'''
        p = self
        return f'<Playlist id={p.id} name={p.name} description={p.description}>'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    name = db.Column(db.String(50),
                     nullable=False,
                     unique=True)

    description = db.Column(db.Text,
                            nullable=True)

    songs = db.relationship('PlaylistSong', backref='playlists')


class Song(db.Model):
    """Song."""

    # ADD THE NECESSARY CODE HERE

    __tablename__ = "songs"

    def __repr__(self):
        '''Better Representation of the class'''
        s = self
        return f'<Song id={s.id} title={s.title} artis={s.artis}>'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    title = db.Column(db.String(50),
                      nullable=False,
                      unique=True)

    artis = db.Column(db.String(50),
                      nullable=False,
                      unique=False)

    playlists = db.relationship('PlaylistSong', backref='songs')


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    # ADD THE NECESSARY CODE HERE

    __tablename__ = 'playlistsongs'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    playlist_id = db.Column(db.Integer, db.ForeignKey(
        'playlists.id', ondelete='CASCADE'))

    song_id = db.Column(db.Integer, db.ForeignKey(
        'songs.id', ondelete='CASCADE'))


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
