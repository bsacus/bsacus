import subprocess

def create_note_in_notes_app(note_title, note_body):
    """
    Create a new note in the Notes app on a Mac.

    Parameters:
    - note_title (str): The title of the note.
    - note_body (str): The body of the note.

    Returns:
    - None.
    """
    # Use AppleScript to open the Notes app
    subprocess.call(['osascript', '-e', 'tell application "Notes" to activate'])

    # Use AppleScript to create a new note with the specified title and body
    script = f'tell application "Notes" to make new note with properties {{name:"{note_title}", body:"{note_body}"}}'
    subprocess.call(['osascript', '-e', script])

# Example usage
note_title = "Test Note7778"
note_body = "This is a test note created with Python."
create_note_in_notes_app(note_title, note_body)
