"""Arquivo que estudantes devem editar"""

# key lambda --> https://iq.opengenus.org/python-max-lambda/


def show_deepest_file(context):
    if not context["all_files"]:
        print("No files found")
    else:
        deepest_file = max(
            context["all_files"], key=lambda string: len(string.split("/"))
        )
        print(f"Deepest file: {deepest_file}")


def find_file_by_name(context, search_term, case_sensitive=True):
    if not search_term:
        return []

    found_files = []

    for path in context["all_files"]:
        file_name = path.split("/")[-1]

        if not case_sensitive and search_term.lower() in file_name.lower():
            found_files.append(path)

        if case_sensitive and search_term in file_name:
            found_files.append(path)

    return found_files
