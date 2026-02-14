def validate_input(name, location, issue):

    if not name.strip():
        return False, "Please enter your name"

    if not location.strip():
        return False, "Please enter your location"

    if not issue.strip():
        return False, "Please describe your issue"

    return True, ""
