from ui_parser import extract_text


def generate_html(
    image_path
):

    text = extract_text(
        image_path
    )

    lines = [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]

    html = """
<!DOCTYPE html>
<html>
<head>

<title>
Generated UI
</title>

<style>

body {

font-family: Arial;
padding: 40px;

}

input {

display: block;
margin: 10px 0;
padding: 10px;
width: 300px;

}

button {

padding: 10px 20px;

}

</style>

</head>

<body>
"""

    for line in lines:

        lower = line.lower()

        if (
            "email" in lower
            or
            "username" in lower
        ):

            html += (
                "<input "
                "type='text' "
                f"placeholder='{line}'>"
            )

        elif (
            "password"
            in lower
        ):

            html += (
                "<input "
                "type='password' "
                f"placeholder='{line}'>"
            )

        elif (
            "login"
            in lower
            or
            "sign in"
            in lower
            or
            "submit"
            in lower
        ):

            html += (
                f"<button>{line}"
                "</button>"
            )

        else:

            html += (
                f"<h2>{line}</h2>"
            )

    html += """

</body>

</html>
"""

    with open(
        "generated_ui.html",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(html)

    return (
        "generated_ui.html"
    )


if __name__ == "__main__":

    image_path = input(
        "Enter UI Screenshot Path: "
    )

    output = generate_html(
        image_path
    )

    print(
        "\nGenerated:"
    )

    print(output)
