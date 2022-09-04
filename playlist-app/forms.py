from turtle import title
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Length


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    # Add the necessary code to use this form

    name = StringField("Name", validators=[
        InputRequired(), Length(min=3, max=50)])
    description = TextAreaField("Description", validators=[
        InputRequired(), Length(min=3, max=250)])


class SongForm(FlaskForm):
    """Form for adding songs."""

    # Add the necessary code to use this form

    title = StringField("Title", validators=[
                        InputRequired(), Length(min=3, max=50)])
    artis = StringField("Artis", validators=[
                        InputRequired(), Length(min=3, max=50)])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
